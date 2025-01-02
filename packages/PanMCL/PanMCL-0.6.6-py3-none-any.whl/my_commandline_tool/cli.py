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
import os
import time
import glob
import shutil
import argparse
import concurrent.futures
from .core_test_3 import GeneIdProcessor, CodeEditor, FileProcessor, PfamCounter
from .run_blast_diamond import RunBioSoftware
from .run_interproscan_2 import deduplicate_fasta, split_fasta, run_interproscan  # 导入你的函数


# 1. 实现批量进行序列比对的功能
def run_blast_diamond(args):
    process = args.process
    thread = args.thread
    repeat = args.repeat
    software = args.software
    add_species = args.add_species

    species = []
    files = glob.glob('*.pep')
    for fn in files:
        species.append(fn.split('.')[0])

    sub = []
    if add_species:
        for na in add_species:
            for spec in species:
                sub.append(f'{na}_{spec}')
                sub.append(f'{spec}_{na}')
        sub = list(set(sub))
    RunBioSoftware(species, repeat, sub, [], software, process, thread)


# 2. 对序列的pep文件，进行去重、分割，然后批量的调用interproscan软件
def run_interproscan_command(args):
    start_time = time.time()

    # 解析参数
    input_fasta = args.input_fasta
    output_fasta = args.output_fasta
    number_of_splits = args.number_of_splits
    process_interpro = args.process_interpro
    thread_interpro = args.thread_interpro

    output_disassemble = "output_disassemble"
    output_interproscan_result = "output_interproscan_result"

    # 清理并创建输出目录
    shutil.rmtree(output_disassemble, ignore_errors=True)
    os.makedirs(output_disassemble)
    shutil.rmtree(output_interproscan_result, ignore_errors=True)
    os.makedirs(output_interproscan_result)

    # 1. 去重
    deduplicate_fasta(input_fasta, output_fasta)
    print("Deduplication completed.")

    # 2. 分割
    split_fasta(output_fasta, output_disassemble, number_of_splits)
    print("Splitting completed.")

    # 3. 调用 InterProScan
    pep_files = glob.glob(f"{output_disassemble}/*.fasta")
    with concurrent.futures.ProcessPoolExecutor(max_workers=process_interpro) as executor:
        for file in pep_files:
            executor.submit(run_interproscan, file, thread_interpro)
    print("InterProScan analysis completed.")

    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")


# 3. 实现鉴定四类基因的功能，并进行提取相关的基因
def process_pangenes(args):
    start_time = time.time()

    sp_name = ["Bva", "Sto", "Psa", "Aip", "Amo", "Ahy", "Adu", "Lal", "Lan", "Aev", "Dod", "Apr", "Lja", "Aed", "Cca", "Gma", "Gso", "Mtr", "Car", "Mal", "Tpr", "Tsu", "Vra", "Ssu"]  # 改 - 需要优化！
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


# 主要的代码部分
def main():
    parser = argparse.ArgumentParser(description="A simple command-line tool.")
    subparsers = parser.add_subparsers(help='sub-command help')

    # 1. 实现批量进行序列比对的功能
    parser_run = subparsers.add_parser('runbd', help='Run BLAST or DIAMOND for sequence alignment')
    parser_run.add_argument('-p', '--process', type=int, default=4, help='Number of processes (default: 4)')
    parser_run.add_argument('-t', '--thread', type=int, default=4, help='Number of threads per process (default: 4)')
    parser_run.add_argument('-r', '--repeat', action='store_true', default=True, help='Allow repeated comparisons (default: True)')
    parser_run.add_argument('-s', '--software', choices=['blast', 'diamond'], default='diamond', help='Software to use: blast or diamond (default: diamond)')
    parser_run.add_argument('-a', '--add-species', nargs='+', default=[], help='Additional species pairs to compare (e.g., Tpr)')
    parser_run.set_defaults(func=run_blast_diamond)


    # 2. 对序列的pep文件，进行去重、分割，然后批量的调用interproscan软件
    parser_run = subparsers.add_parser('runinter', help='Run InterProScan for sequence analysis')
    parser_run.add_argument('-i', '--input-fasta', required=True, help='Input FASTA file (e.g., genome_s.fasta)')
    parser_run.add_argument('-o', '--output-fasta', default="unique.fasta", help='Output deduplicated FASTA file (default: unique.fasta)')
    parser_run.add_argument('-n', '--number-of-splits', type=int, default=100, help='Number of splits (default: 100)')
    parser_run.add_argument('-p', '--process-interpro', type=int, default=3, help='Number of processes for InterProScan (default: 3)')
    parser_run.add_argument('-t', '--thread-interpro', type=int, default=4, help='Number of threads per process (default: 4)')
    parser_run.set_defaults(func=run_interproscan_command)


    # 3. 实现鉴定四类基因的功能，并进行提取相关的基因
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



