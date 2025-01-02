import sys
import argparse

import giquant.trade.yf as yf
import giquant.trade.cot as cot


def create_args_parser():
    parser = argparse.ArgumentParser(prog='dwnl.py', description='Download files.')
    subparsers = parser.add_subparsers(help='GiQuant Trade Download Command help.')

    parser_yf = subparsers.add_parser('yf', description=yf.desc_)
    parser_yf = yf.create_args_parser(parser_yf)
    parser_yf.set_defaults(main=yf.main)

    parser_cot = subparsers.add_parser('cot', description=cot.desc_)
    parser_cot = cot.create_args_parser(parser_cot)
    parser_cot.set_defaults(main=cot.main)

    return parser


def main(args):
    if bool(set(['main']) & set(args.__dict__.keys())):
      args.main(args)
    else:
        print('Please select a program to run: yf,cot,...(more to come)')

if __name__ == "__main__":
    parser = create_args_parser()
    args = parser.parse_args()
    print(args)
    main(args)





