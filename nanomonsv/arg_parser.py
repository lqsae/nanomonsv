#! /usr/bin/env python

import argparse

from .run import *
from .version import __version__

def create_parser():

    parser = argparse.ArgumentParser(prog = "nanomonsv")

    parser.add_argument("--version", action = "version", version = "%(prog)s " + __version__)

    subparsers = parser.add_subparsers()

    ##########
    # parse
    parse = subparsers.add_parser("parse",
                                help = "Parse supporting reads for candidate structural variations")


    parse.add_argument("bam_file", default = None, type = str,
                     help = "Path to input BAM file")

    parse.add_argument("output_prefix", type = str,
                       help = "Prefix of the pathes of output files")

    parse.add_argument("--debug", default = False, action = 'store_true', help = "keep intermediate files")

    parse.set_defaults(func = parse_main)
    

    return parser

