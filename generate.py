#!/usr/bin/env python3

from dsa.utils import DSADataGen
import pandas as pd
import argparse

VERSION = 1.0


def parse_arguments():
    # Initiate the parser
    parser = argparse.ArgumentParser()

    parser.add_argument("-V", "--version",
                        help="show program version", action="store_true")

    parser.add_argument("-o", "--outputfile",
                        help="The name of the output excel file.", required=True)

    parser.add_argument("-n", "--numrows", type=int,
                        help="The number of rows to generate.", required=True)
    parser.add_argument("-s", "--summary",
                        help="Display a summary to stdout.", action="store_true")

    # Read arguments from the command line
    args = parser.parse_args()

    # Check for --version or -V
    if args.version:
        print("This is {} version {}".format("generate.py", VERSION))

    if args.outputfile:
        print("Writing to output file \"{}\"".format(args.outputfile))

    if args.numrows:
        print("Writing {} rows".format(args.numrows))

    return args


if __name__ == '__main__':

    # Parse the command line arguments
    args = parse_arguments()

    # Generate the data
    dgen = DSADataGen()

    # Format the athlete data and store it in a dataframe (excel sheet-ish)
    athletes = dgen.getAthletes(args.numrows)
    df = pd.DataFrame(athletes)
    if args.summary:
        print(df)

    # Write the excel file.
    writer = pd.ExcelWriter(args.outputfile, engine='xlsxwriter')
    df.to_excel(writer)
    writer.save()
