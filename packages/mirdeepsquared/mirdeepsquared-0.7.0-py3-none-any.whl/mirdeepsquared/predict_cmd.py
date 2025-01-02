#!/usr/bin/env python3
import os
import sys

from mirdeepsquared.common import float_range
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import argparse


def parse_args(args):
    parser = argparse.ArgumentParser(prog='MirDeepSquared-predict', description='Classifies novel miRNA sequences either as false positive or not based on the result.csv and output.mrd files from MiRDeep2. Each row of the standard output represents the location name of the true positives', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('result_csv')  # positional argument
    parser.add_argument('output_mrd')  # positional argument
    parser.add_argument('-m', '--models', help="The path to the trained .keras/.pkl model files to use for the predictions",
                        default=os.path.join(os.path.dirname(__file__), 'models/'))
    parser.add_argument('-w', '--weights', help="The path to the relative weights amongst the models used",
                        default=os.path.join(os.path.dirname(__file__), 'model_weights.yaml'))
    parser.add_argument('-t', '--threshold', type=float_range(0, 1), help="Threshold to use for determining if predictions are treated as true positives or not, between 0 and 1. A higher number means more samples reported as true positives.", default=0.5)
    # TODO: add batch-size as argument or automatically calculate it?
    return parser.parse_args(args)


def main():
    # args = parse_args(["resources/not_version_controlled/zebrafish_result_13_11_2023_t_18_47_00.csv", "resources/not_version_controlled/zebrafish_13_11_2023_t_18_47_00_output.mrd", "-m", "models/"])
    args = parse_args(sys.argv[1:])
    # Avoid booting tensorflow until the correct params have been given
    from mirdeepsquared.predict import predict_main
    true_positives = predict_main(args)
    for true_positive in true_positives:
        print(true_positive)


if __name__ == '__main__':
    main()
