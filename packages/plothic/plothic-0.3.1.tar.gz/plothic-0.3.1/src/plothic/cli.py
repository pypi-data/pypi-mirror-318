#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@Author: Zijie Jiang
@Contact: jzjlab@163.com
@File: cli.py
@Time: 2024/11/15 11:47
@Function: Main function of PlotHiC
"""
import argparse

from .PlotBed import plot_bed
from .PlotHiC import plot_hic


def main():
    parser = argparse.ArgumentParser(description='Plot Whole genome Hi-C contact matrix heatmap')
    parser.add_argument('-hic', '--hic-file', type=str, help='Path to the Hi-C file')
    parser.add_argument('-chr', '--chr-txt', type=str, default=None, help='Path to the chromosome text file')
    parser.add_argument('--matrix', type=str, default=None, help='Path to the HiCPro matrix file')
    parser.add_argument('--abs-bed', type=str, default=None, help='Path to the HiCPro abs bed file')
    parser.add_argument('--abs-order', type=str, default="", help='Path to the HiCPro abs order file')
    parser.add_argument('-o', '--output', type=str, default='GenomeContact.pdf',
                        help='Output file name, default: GenomeContact.pdf')
    parser.add_argument('-r', '--resolution', type=int, default=None, help='Resolution for Hi-C data')
    parser.add_argument('-d', '--data-type', type=str, default='observed',
                        help='Data type for Hi-C data or "oe" (observed/expected), default: observed')
    parser.add_argument('-n', '--normalization', type=str, default='NONE',
                        help='Normalization method for Hi-C data (NONE, VC, VC_SQRT, KR, SCALE, etc.), default: NONE')
    parser.add_argument('-g', '--genome-name', type=str, default=None, help='Genome name')
    parser.add_argument('-f', '--fig-size', type=int, default=6, help='Figure size, default: 6')
    parser.add_argument('--order', action='store_false', help='Order the heatmap by specific order')
    parser.add_argument('--log', action='store_false', help='Log2 transform the data')
    parser.add_argument('--dpi', type=int, default=300, help='DPI for the output figure, default: 300')
    parser.add_argument('--bar_min', type=int, default=0, help='Minimum value for color bar, default: 0')
    parser.add_argument('--bar_max', type=int, default=None, help='Maximum value for color bar')
    parser.add_argument('--cmap', type=str, default='YlOrRd', help='Color map for the heatmap, default: YlOrRd')
    parser.add_argument('--rotation', type=int, default=45, help='Rotation for the x and y axis labels, default: 45')

    args = parser.parse_args()

    if args.matrix and args.hic_file:
        raise ValueError("Please provide either Hi-C file or HiCPro matrix file")

    if args.matrix and args.abs_bed:
        plot_bed(args.matrix, args.abs_bed, order_bed=args.abs_order, output=args.output, genome_name=args.genome_name,
                 fig_size=args.fig_size, dpi=args.dpi, bar_min=args.bar_min, bar_max=args.bar_max, cmap=args.cmap,
                 log=args.log, rotation=args.rotation)
    else:
        plot_hic(args.hic_file, chr_txt=args.chr_txt, output=args.output, resolution=args.resolution,
                 data_type=args.data_type, normalization=args.normalization, genome_name=args.genome_name,
                 fig_size=args.fig_size, dpi=args.dpi, bar_min=args.bar_min, bar_max=args.bar_max, cmap=args.cmap,
                 order=args.order, log=args.log, rotation=args.rotation)


if __name__ == '__main__':
    main()
