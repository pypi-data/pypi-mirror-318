# Copyright 2020 resspect software
# Author: Rupesh Durgesh, Emille Ishida, and Amanda Wasserman
#
# created on 14 April 2022
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import multiprocessing
import logging
import os
from copy import copy
from itertools import repeat
from typing import IO, List, Union

import numpy as np
import pandas as pd

from resspect.lightcurves_utils import (
    read_plasticc_full_photometry_data,
    find_available_key_name_in_header,
    PLASTICC_TARGET_TYPES,
    PLASTICC_RESSPECT_FEATURES_HEADER,
)
from resspect.feature_handling_utils import save_features
from resspect.filter_sets import FILTER_SETS
from resspect.plugin_utils import fetch_feature_extractor_class
from resspect.tom_client import TomClient

__all__ = ["fit_snpcc", "fit_plasticc", "fit_TOM", "request_TOM_data", "fit"]


MAX_NUMBER_OF_PROCESSES = 8


def _snpcc_sample_fit(
        file_name: str, path_to_data_dir: str, feature_extractor: str):
    """
    Reads SNPCC file and performs fit.
    
    Parameters
    ----------
    file_name
        SNPCC file name
    path_to_data_dir
         Path to directory containing the set of individual files,
         one for each light curve.
    feature_extractor
        Function used for feature extraction.
    """
    feature_extractor_class = fetch_feature_extractor_class(feature_extractor)
    light_curve_data = feature_extractor_class()
    light_curve_data.load_snpcc_lc(
        os.path.join(path_to_data_dir, file_name))
    light_curve_data.fit_all()
    
    return light_curve_data


def fit_snpcc(
        path_to_data_dir: str, features_file: str,
        file_prefix: str = "DES_SN", number_of_processors: int = MAX_NUMBER_OF_PROCESSES,
        feature_extractor: str = 'Bazin'):
    """
    Perform fit to all objects in the SNPCC data.

     Parameters
     ----------
     path_to_data_dir: str
         Path to directory containing the set of individual files,
         one for each light curve.
     features_file: str
         Path to output file where results should be stored.
     file_prefix: str
        File names prefix
     number_of_processors: int, default 1
        Number of cpu processes to use.
     feature_extractor: str, default Bazin
        Function used for feature extraction.
    """
    feature_extractor_class = fetch_feature_extractor_class(feature_extractor)
    header = feature_extractor_class.get_feature_header(filters=FILTER_SETS['SNPCC'])

    files_list = os.listdir(path_to_data_dir)
    files_list = [each_file for each_file in files_list
                  if each_file.startswith(file_prefix)]
    multi_process = multiprocessing.Pool(number_of_processors)
    logging.info("Starting SNPCC " + feature_extractor + " fit...")

    feature_data = []
    for light_curve_data in multi_process.starmap(
        _snpcc_sample_fit,
        zip(
            files_list,
            repeat(path_to_data_dir),
            repeat(feature_extractor)
        )
    ):
        if 'None' not in light_curve_data.features:
            feature_data.append(light_curve_data.get_features_to_write())
    features_df = pd.DataFrame(feature_data, columns=header)
    save_features(features_df, location="filesystem", filename=features_file)


def _plasticc_sample_fit(
        index: int, snid: int, path_photo_file: str,
        sample: str, light_curve_data,
        meta_header: pd.DataFrame):
    """
    Performs fit for PLAsTiCC dataset with snid

    Parameters
    ----------
    index
        index of snid
    snid
        Identification number for the desired light curve.
    path_photo_file: str
        Complete path to light curve file.
    sample: str
        'train' or 'test'. Default is None.
    light_curve_data
        light curve class
    meta_header
        photometry meta header data
    """
    light_curve_data.load_plasticc_lc(path_photo_file, snid)
    light_curve_data.fit_all()
    light_curve_data.redshift = meta_header['true_z'][index]
    light_curve_data.sncode = meta_header['true_target'][index]
    light_curve_data.sntype = PLASTICC_TARGET_TYPES[
        light_curve_data.sncode]
    light_curve_data.sample = sample
    light_curve_data_copy = copy(light_curve_data)
    light_curve_data.clear_data()
    return light_curve_data_copy


def fit_plasticc(path_photo_file: str, path_header_file: str,
                 output_file: str, sample='train',
                 feature_extractor: str = "Bazin",
                 number_of_processors: int = MAX_NUMBER_OF_PROCESSES):
    """
    Perform fit to all objects in a given PLAsTiCC data file.
    Parameters
    ----------
    path_photo_file: str
        Complete path to light curve file.
    path_header_file: str
        Complete path to header file.
    output_file: str
        Output file where the features will be stored.
    sample: str
        'train' or 'test'. Default is 'train'.
    number_of_processors: int, default 1
        Number of cpu processes to use.
    feature_extractor: str, default Bazin
        feature extraction method
    """

    name_list = ['SNID', 'snid', 'objid', 'object_id']
    meta_header = read_plasticc_full_photometry_data(path_header_file)
    meta_header_keys = meta_header.keys().tolist()
    id_name = find_available_key_name_in_header(
        meta_header_keys, name_list)
    feature_extractor_class = fetch_feature_extractor_class(feature_extractor)
    light_curve_data = feature_extractor_class()

    if sample == 'train':
        snid_values = meta_header[id_name]
    elif sample == 'test':
        light_curve_data.full_photometry = read_plasticc_full_photometry_data(
            path_photo_file)
        snid_values = pd.DataFrame(np.unique(
            light_curve_data.full_photometry[id_name].values),
            columns=[id_name])[id_name]
    snid_values = np.array(list(snid_values.items()))
    multi_process = multiprocessing.Pool(number_of_processors)
    logging.info("Starting PLAsTiCC " + feature_extractor + " fit...")
    # TODO: Current implementation uses bazin features header for
    #  all feature extraction
    feature_data = []
    iterator_list = zip(
        snid_values[:, 0].tolist(),
        snid_values[:, 1].tolist(),
        repeat(path_photo_file),
        repeat(sample),
        repeat(light_curve_data),
        repeat(meta_header)
    )
    for light_curve_data in multi_process.starmap(_plasticc_sample_fit, iterator_list):
        if 'None' not in light_curve_data.features:
            feature_data.append(light_curve_data.get_features_to_write())
    features_df = pd.DataFrame(feature_data, header=PLASTICC_RESSPECT_FEATURES_HEADER)
    save_features(features_df, location="filesystem", filename=output_file)

def _TOM_sample_fit(
        obj_dic: dict, feature_extractor: str):
    """
    Reads TOM file and performs fit.
    
    Parameters
    ----------
    id
        SNID
    feature_extractor
        Function used for feature extraction.
    """
    feature_extractor_class = fetch_feature_extractor_class(feature_extractor)
    light_curve_data = feature_extractor_class()
    light_curve_data.photometry = pd.DataFrame(obj_dic['photometry'])
    light_curve_data.dataset_name = 'TOM'
    light_curve_data.filters = ['u', 'g', 'r', 'i', 'z', 'Y']
    light_curve_data.id = obj_dic['objectid']
    light_curve_data.redshift = obj_dic['redshift']
    light_curve_data.sntype = 'unknown'
    light_curve_data.sncode = obj_dic['sncode']
    light_curve_data.sample = 'N/A'

    light_curve_data.fit_all()
    
    return light_curve_data

def fit_TOM(data_dic: dict, output_features_file: str,
            number_of_processors: int = MAX_NUMBER_OF_PROCESSES,
            feature_extractor: str = 'Bazin'):
    """
    Perform fit to all objects from the TOM data.

     Parameters
     ----------
     data_dic: str
         Dictionary containing the photometry for all light curves.
     output_features_file: str
         Path to output file where results should be stored.
     number_of_processors: int, default 1
        Number of cpu processes to use.
     feature_extractor: str, default Bazin
        Function used for feature extraction.
    """

    feature_extractor_class = fetch_feature_extractor_class(feature_extractor)
    header = feature_extractor_class.get_feature_header(filters=FILTER_SETS['LSST'])

    multi_process = multiprocessing.Pool(number_of_processors)
    logging.info("Starting TOM " + feature_extractor + " fit...")
    feature_data = []
    for light_curve_data in multi_process.starmap(
        _TOM_sample_fit,
        zip(
            data_dic,
            repeat(feature_extractor)
        )
    ):
        if 'None' not in light_curve_data.features:
            feature_data.append(light_curve_data.get_features_to_write())
    features_df = pd.DataFrame(feature_data, columns=header)
    save_features(features_df, location="filesystem", filename=output_features_file)

def _sample_fit(
        obj_dic: dict, feature_extractor: str, filters: list, type: str, one_code: list,
        additional_info: list):
    """
    Reads general file and performs fit.
    
    Parameters
    ----------
    id
        SNID
    feature_extractor
        Function used for feature extraction.
    """
    feature_extractor_class = fetch_feature_extractor_class(feature_extractor)
    light_curve_data = feature_extractor_class()
    light_curve_data.photometry = pd.DataFrame(obj_dic['photometry'])
    light_curve_data.filters = filters
    light_curve_data.id = obj_dic['objectid']
    light_curve_data.redshift = obj_dic['redshift']
    light_curve_data.sncode = obj_dic['sncode']
    if light_curve_data.sncode in one_code:
        light_curve_data.sntype = 'Ia' #just labeling all positive classes as Ia
                                       #unsure what changing this might affect in database.py
    else:
        light_curve_data.sntype = 'other'
    light_curve_data.sample = type
    light_curve_data.additional_info = {}
    for info in additional_info:
        light_curve_data.additional_info[info] = obj_dic[info]
    light_curve_data.fit_all()
    
    return light_curve_data

def fit(
        data_dic: dict,
        output_features_file: str,
        number_of_processors: int = MAX_NUMBER_OF_PROCESSES,
        feature_extractor: str = 'Bazin',
        filters: Union[str, List[str]] = 'SNPCC',
        type: str = 'unspecified',
        one_code: list = [10],
        additional_info: list = []
    ):
    """
    Perform fit to all objects from a generalized dataset.

     Parameters
     ----------
     data_dic: list
         List of dictionaries containing the photometry for each light 
         curve. Example provided below.
     output_features_file: str
         Path to output file where results should be stored.
     number_of_processors: int, default 1
        Number of cpu processes to use.
     feature_extractor: str, default Bazin
        Function used for feature extraction.
    filters: list
        List of filters to be used, or a key in FILTER_SETS.
    type: str
        Type of data: train, test, validation, pool
    one_code: list
        List of codes to be used to define a positive class. 
        Default is 10 from ELAsTiCC type Ia SN.
    additional_info: list
        List of additional header information to be used in other classifiers.
        For example, RA and dec for GHOST feature extraction

    Example of a data_dic element:
    ------------------------------
        Required keys
            'objectid'
                object id
            'photometry'
                dictionary containing keys ''mjd', 'band', 'flux', 'fluxerr'.
                each entry contains a list of mjd, band, flux, fluxerr for 
                each observation
            'redshift'
                redshift of the object if known, 'unknown' otherwise
            'sncode'
                number to delineate what type of transient the object is. 
                one_code will translate this into '1'/'0' for positive/negative

        Optional keys; anything you might need for your classifier. 
        Need to specify the keys as a list in 'additional_info'. For example
            'RA'
            'dec'
    """

    # if `filters` is a key in FILTER_SETS, then use the corresponding value
    # otherwise, assume `filters` is a list of filter strings like `['g', 'r']`.
    if isinstance(filters, str) and filters in FILTER_SETS:
        filters = FILTER_SETS[filters]

    feature_extractor_class = fetch_feature_extractor_class(feature_extractor)
    header = feature_extractor_class.get_feature_header(filters)
    feature_data = []

    multi_process = multiprocessing.Pool(number_of_processors)
    if feature_extractor != None:
        logging.info("Starting " + feature_extractor + " fit...")
        for light_curve_data in multi_process.starmap(
            _sample_fit, zip(
                data_dic,
                repeat(feature_extractor),
                repeat(filters),
                repeat(type),
                repeat(one_code),
                repeat(additional_info)
            )
        ):
            if 'None' not in light_curve_data.features:
                feature_data.append(light_curve_data.get_features_to_write())

    features_df = pd.DataFrame(feature_data, columns=header)
    save_features(features_df, location="filesystem", filename=output_features_file)

def request_TOM_data(url: str = "https://desc-tom-2.lbl.gov", username: str = None, 
                     passwordfile: str = None, password: str = None, detected_since_mjd: float = None, 
                     detected_in_last_days: float = None, mjdnow: float = None, cheat_gentypes: list = None):
    tom = TomClient(url = url, username = username, passwordfile = passwordfile, 
                    password = password)
    dic = {}
    if detected_since_mjd is not None:
        dic['detected_since_mjd'] = detected_since_mjd
    if detected_in_last_days is not None:
        dic['detected_in_last_days'] = detected_in_last_days
    if mjdnow is not None:
        dic['mjd_now'] = mjdnow
    if cheat_gentypes is not None:
        dic['cheat_gentypes'] = cheat_gentypes
    dic['include_hostinfo'] = True
    res = tom.post('elasticc2/gethottransients', json = dic)
    data_dic = res.json()
    return data_dic


def main():
    return None


if __name__ == '__main__':
    main()
