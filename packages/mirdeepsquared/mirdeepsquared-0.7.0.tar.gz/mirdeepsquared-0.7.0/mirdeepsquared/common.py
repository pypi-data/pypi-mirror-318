# Functions that don't require tensorflow can be placed here. This avoids long boot times for programs that don't use tensorflow
import argparse
import os
import pandas as pd
import glob
import numpy as np
from pathlib import Path
import re
from os import listdir
from os.path import isfile, join

NUCLEOTIDE_NR = 5  # U C A G D (D for Dummy)
EPSILON = 1e-7


def build_structure_1D(pri_struct, exp):
    pri_struct_padded = pri_struct.ljust(111, '-')
    pri_struct_truncated = pri_struct_padded[:111]

    exp_padded = exp.ljust(111, 'f')
    exp_truncated = exp_padded[:111]

    # Defines a vocabalary index for structural information, S = Star, l = loop, M = Mature, f = surrounding precursor / "nothing"
    char_mappings = {}
    char_mappings['f'] = {'-': 0, '.': 1, '(': 2, ')': 3}
    char_mappings['S'] = {'-': 4, '.': 5, '(': 6, ')': 7}
    char_mappings['l'] = {'-': 8, '.': 9, '(': 10, ')': 11}
    char_mappings['M'] = {'-': 12, '.': 13, '(': 14, ')': 15}

    merged_structure_information = [char_mappings[x][pri_struct_truncated[ind]] for ind, x in enumerate(exp_truncated)]
    return merged_structure_information


def save_dataframe_to_pickle(df, pickle_output_file):
    pickle_output_file = Path(pickle_output_file)
    pickle_output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_pickle(pickle_output_file)


def list_of_pickle_files_in(path):
    if isfile(path) and path.endswith('.pkl'):
        return [path]
    return glob.glob(path + "/*.pkl")


def files_in(path):
    if isfile(path):
        return [path]
    onlyfiles = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
    return onlyfiles


def read_dataframes(paths):
    dfs = []
    for path in paths:
        df = pd.read_pickle(path)
        if 'source_pickle' not in df.columns:
            df['source_pickle'] = os.path.basename(path)
        dfs.append(df)

    concatenated = pd.concat(dfs, axis=0)
    concatenated.reset_index(inplace=True, drop=True)
    return concatenated


def calc_percentage_change(numbers):
    # np.diff(numbers) = rate of change
    data_no_zeros = np.where(numbers == 0, EPSILON, numbers)
    percentage_change = np.diff(numbers) / data_no_zeros[:-1] * 100
    return percentage_change


def encode_exp(exp):
    """
    Converts 'fffffffffffffffffffffffffffffffSSSSSSSSSSSSSSSSSSSSSSSllllllllllllllllMMMMMMMMMMMMMMMMMMMMMMffffffffffffffffff' to an array like:
          00000000000000000000000000000001111111111111111111111122222222222222223333333333333333333333000000000000000000
          and then one hot encodes it
    """
    exp_padded = exp.ljust(111, 'f')
    exp_truncated = exp_padded[:111]

    char_mapping = {'f': 0, 'S': 1, 'l': 2, 'M': 3}
    indices = [char_mapping[char] for char in exp_truncated]
    one_hot_encoded = np.eye(len(char_mapping))[indices]
    return one_hot_encoded


def extract_precursor_from_exp_and_pri_seq(exp, pri_seq):
    """Extracts ugcugguuucuuccacagugguacuuuccauuagaacuaucaccggguggaaacuagcagu from
    exp:      fffffffffffffffffffffffffffffffSSSSSSSSSSSSSSSSSSSSSSSllllllllllllllllMMMMMMMMMMMMMMMMMMMMMMffffffffffffffffff
    pri_seq:  caacuauuauucucggaucagaucgagccauugcugguuucuuccacagugguacuuuccauuagaacuaucaccggguggaaacuagcaguggcucgaucuuuuccacu
        """
    beginning = min(exp.find('M'), exp.find('S'))
    end = max(exp.rfind('M'), exp.rfind('S')) + 1
    precursor = pri_seq[beginning:end]
    return precursor


def one_hot_encode_sequence(sequence, max_length=111):
    sequence_padded = sequence.ljust(max_length, 'D')
    sequence_truncated = sequence_padded[:max_length]

    char_mapping = {'D': 0, 'u': 1, 'g': 2, 'c': 3, 'a': 4}
    indices = [char_mapping[char] for char in sequence_truncated]
    one_hot_encoded = np.eye(len(char_mapping))[indices]
    return one_hot_encoded


def loop_length(exp):
    return exp.count('l')


def find_motifs(exp, pri_seq):
    """
    From https://mirgenedb.org/information:
    "Processing motifs are often (but not always) present in the primary microRNA transcript including a UG motif 14 nucleotides upstream of the 5p arm,
    a UGU motif at the 3' end of the 5p arm, and a CNNC motif 17 nucleotides downstream of the 3p arm (22,23).".
    But according to https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4613790/, the CNNC motif can be positioned 16-18 nt downstream
    """
    # exp like: fffffffffffffffffffffffffffffffSSSSSSSSSSSSSSSSSSSSSSSllllllllllllllllMMMMMMMMMMMMMMMMMMMMMMffffffffffffffffff

    star_offset = exp.find('S')
    star_end = exp.rfind('S') + 1
    mature_offset = exp.find('M')
    mature_end = exp.rfind('M') + 1
    star_first = star_offset < mature_offset
    if star_first:
        ug_motif = pri_seq[star_offset - 14: star_offset - 12]
        ugu_motif = pri_seq[star_end: star_end + 3]
        cnnc_motif_range = pri_seq[mature_end + 15: mature_end + 22]
    else:
        ug_motif = pri_seq[mature_offset - 14: mature_offset - 12]
        ugu_motif = pri_seq[mature_end: mature_end + 3]
        cnnc_motif_range = pri_seq[star_end + 15: star_end + 22]
    has_ug_motif = ug_motif == 'ug'
    has_ugu_motif = (ugu_motif == 'ugu' or ugu_motif == 'gug')  # reverse complement of ugu
    has_cnnc_motif = re.search(r"[ucag]*c[ucag][ucag]c[ucag]*", cnnc_motif_range) is not None
    # TODO: mismatched GHG (mGHG) where H is either a, c or u?
    # From https://doi.org/10.1016/j.celrep.2021.110015:
    # the GHG motif, defined as an unmatched nucleotide other than guanosine
    # that is flanked by two base-paired guanosines at position −7 to −5 relative to the Drosha cleavage site,
    # can facilitate miRNA precursor processing efficiency and precision
    return [int(has_ug_motif), int(has_ugu_motif), int(has_cnnc_motif)]


def one_hot_encode(categorical_features, nr_of_categories):
    one_hot_encoded = np.eye(nr_of_categories)[categorical_features]
    return one_hot_encoded


def prepare_data(df):
    # TODO: At least 16-nt complementarity between the two arm sequences. (Fromm 2015) (14 according to Hackenberg 2009)
    # TODO: The loop sequence is at least 8 nt in length (Fromm 2015)
    # TODO: Perfect seed pairing: Conserved Watson–Crick pairing to the 5′ region of the miRNA centered on nucleotides 2–7, which is called the miRNA “seed”, markedly reduces the occurrence of false-positive predictions (https://www-sciencedirect-com.ezp.sub.su.se/science/article/pii/S0092867409000087?via%3Dihub#bib60)
    # TODO: create other features for mature vs star, such as:
    # feature_difference = feature1 - feature2
    # feature_interaction = feature1 * feature2
    # feature_log = np.log(feature1) or np.log(feature1) / np.log(feature2)
    df['mature_vs_star_read_ratio'] = df.apply(lambda x: x['mature_read_count'] / (x['star_read_count'] + EPSILON), axis=1)
    df['structure_as_1D_array'] = df.apply(lambda x: build_structure_1D(x['pri_struct'], x['exp']), axis=1)
    df['read_density_map_percentage_change'] = df.apply(lambda x: calc_percentage_change(x['read_density_map']), axis=1)
    df['location_of_mature_star_and_hairpin'] = df.apply(lambda x: encode_exp(x['exp']), axis=1)
    df['precursor'] = df.apply(lambda x: extract_precursor_from_exp_and_pri_seq(x['exp'], x['pri_seq']), axis=1)
    df['pri_seq_encoded'] = df.apply(lambda x: one_hot_encode_sequence(x['pri_seq']), axis=1)
    # df[['has_ug_motif', 'has_ugu_motif', 'has_cnnc_motif']] = df.apply(lambda x: pd.Series(find_motifs(x['exp'], x['pri_seq'])), axis=1)
    # df['motifs_one_hot_encoded'] = df.apply(lambda x: one_hot_encode(find_motifs(x['exp'], x['pri_seq']), 2), axis=1)
    df['motifs'] = df.apply(lambda x: find_motifs(x['exp'], x['pri_seq']), axis=1)
    df['has_all_motifs'] = df.apply(lambda x: (x['motifs'] == [1, 1, 1]), axis=1)
    df['loop_length'] = df.apply(lambda x: loop_length(x['exp']), axis=1)
    # TODO: add , 'loop_length'
    df['combined_numerics'] = df[['mature_read_count', 'star_read_count', 'significant_randfold', 'mature_vs_star_read_ratio']].apply(lambda row: row.tolist(), axis=1)
    window_size = 5
    df['read_density_map_moving_average'] = df.apply(lambda x: np.convolve(x['read_density_map_percentage_change'], np.ones(window_size) / window_size, mode='same'), axis=1)
    return df


def split_data_once(df, fraction=0.8, random_state=42):
    train = df.sample(frac=fraction, random_state=random_state)
    holdout = df.drop(train.index)
    return (train, holdout)


def split_into_different_files(path_to_pickle_files, pickle_output_path, fraction, random_state):
    list_of_files = list_of_pickle_files_in(path_to_pickle_files)
    print("Splitting " + str([os.path.basename(path) for path in list_of_files]) + " with fraction " + str(fraction) + " and random state " + str(random_state))
    df = read_dataframes(list_of_files)
    train, holdout = split_data_once(df, fraction=fraction, random_state=random_state)
    print("False positives in train:" + str(len(train[(train['false_positive'] == True)])))
    print("True positives in train:" + str(len(train[(train['false_positive'] == False)])))
    save_dataframe_to_pickle(train, pickle_output_path + "/train/train.pkl")
    print("False positives in holdout:" + str(len(holdout[(holdout['false_positive'] == True)])))
    print("True positives in holdout:" + str(len(holdout[(holdout['false_positive'] == False)])))
    save_dataframe_to_pickle(holdout, pickle_output_path + "/holdout/holdout.pkl")


def locations_in(df):
    return df['location'].values.tolist()


def Y_values(df):
    return np.asarray(df['false_positive'].values.astype(np.float32))


def float_range(minimum, maximum):
    """Return function handle of an argument type function for
       ArgumentParser checking a float range: mini <= arg <= ****
         minimum - minimum acceptable argument
         maximum - maximum acceptable argument"""
    # Define the function with default arguments
    def float_range_checker(arg):
        """New Type function for argparse - a float within predefined range."""
        try:
            f = float(arg)
        except ValueError:
            raise argparse.ArgumentTypeError("must be a floating point number")
        if f < minimum or f > maximum:
            raise argparse.ArgumentTypeError("must be in range [" + str(minimum) + " .. " + str(maximum) + "]")
        return f
    # Return function handle to checking function
    return float_range_checker
