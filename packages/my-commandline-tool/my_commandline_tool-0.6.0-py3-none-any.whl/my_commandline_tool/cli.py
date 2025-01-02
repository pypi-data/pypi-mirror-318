#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Author        : yuzijian
# @Email         : yuzijian1010@163.com
# @FileName      : cli.py
# @Time          : 2024-12-30 11:51:41
# @description   :
"""
# my_commandline_tool/cli.py
import argparse
import argparse
import time
import glob
from core_test_3 import GeneIdProcessor, CodeEditor, FileProcessor, PfamCounter  # 替换为你的模块名


def process_pangenes(args):
    start_time = time.time()

    sp_name = ["Bva", "Sto", "Psa", "Aip", "Amo", "Ahy", "Adu", "Lal", "Lan", "Aev", "Dod", "Apr", "Lja", "Aed", "Cca", "Gma", "Gso", "Mtr", "Car", "Mal", "Tpr", "Tsu", "Vra", "Ssu"]
    syn_list = args.file
    gene_id_processor = GeneIdProcessor(sp_name, syn_list)
    gene_id_processor.process_gene_ids()
    print("The first step, extracting the gene id is done")

    editor = CodeEditor()
    editor.generate_private_from_pep(glob.glob("output_1_CSDP_id_file/*"))
    editor.process_files(glob.glob("output_1_CSDP_id_file/*"))
    print("The second step, obtaining the cds and pep sequences of the four types of gene ids has been completed")

    fp = FileProcessor()
    fp.process_files()
    print("The third step, split the file into species and four types, and count the number")

    pfam_counter = PfamCounter()
    pfam_counter.count_pfam_num(glob.glob("output_3_CSDP_all_cds/*.txt"))
    print("The five step, the cds number and total length of the four types of genes were obtained")

    end_time = time.time()
    print(f"End of run, total time is: {end_time - start_time} seconds!")


def main():
    parser = argparse.ArgumentParser(description="A simple command-line tool.")
    subparsers = parser.add_subparsers(help='sub-command help')

    parser_pangenes = subparsers.add_parser('pangenes', help='Process pangenes')
    parser_pangenes.add_argument('-f', '--file', required=True, help='Input file for syn list')
    parser_pangenes.add_argument('-c', '--cds', required=True, help='Input directory for CDS files')
    parser_pangenes.add_argument('-p', '--pep', required=True, help='Input directory for PEP files')
    parser_pangenes.set_defaults(func=process_pangenes)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()


