#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: Created on 22 Jul 2024 13:30
# @Author: Yao LI
# @File: SpaGRN/main_revision.py
import os
import sys
sys.path.append('/dellfsqd2/ST_OCEAN/USER/liyao1/07.spatialGRN/')
import argparse
import pandas as pd
from multiprocessing import cpu_count
from spagrn_debug.regulatory_network import InferNetwork as irn
import spagrn_debug.plot as prn
import scanpy as sc


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    sys.path.insert(0, parent_dir)

    parser = argparse.ArgumentParser(description='spaGRN')
    parser.add_argument("--data", '-i', type=str, help='experiment data file, in h5ad/loom format')
    parser.add_argument("--tf", '-t', type=str, help='TF list file')
    parser.add_argument("--database", '-d', type=str, help='ranked motifs database file, in feather format')
    parser.add_argument("--motif_anno", '-m', type=str, help='motifs annotation file, in tbl format')
    # parser.add_argument("--method", type=str, default='grnboost', choices=['grnboost', 'spg', 'scc'], help='method to calculate TF-gene similarity')
    parser.add_argument("--output", '-o', type=str, help='output directory')
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

    fn = args.data
    tfs_fn = args.tf
    database_fn = args.database
    motif_anno_fn = args.motif_anno
    out_dir = args.output
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    prefix = os.path.join(out_dir, method)

    # load data
    data = irn.read_file(fn)
    data = irn.preprocess(data)
    sc.tl.pca(data)

    # create grn
    grn = irn(data, pos_label='spatial')

    # set parameters
    grn.add_params({'prune_auc_threshold': 0.05, 'rank_threshold': 9000, 'auc_threshold': 0.05})

    # niche data
    niche_human = pd.read_csv('/dellfsqd2/ST_OCEAN/USER/liyao1/07.spatialGRN/resource/lr_network_human.csv')
    niche_mouse = pd.read_csv('/dellfsqd2/ST_OCEAN/USER/liyao1/07.spatialGRN/resource/lr_network_mouse.csv')
    niches = pd.concat([niche_mouse, niche_human])

    # mouse_brain: cluster_label='annotation', layers='counts'

    # run analysis
    grn.infer(database_fn,
              motif_anno_fn,
              tfs_fn,
              niche_df=niches,
              num_workers=(cpu_count()//2),
              cache=False,
              save_tmp=True,
              layers='counts',
              latent_obsm_key='spatial',
              model='bernoulli',
              n_neighbors=10,  # TODO:
              weighted_graph=False,
              combine=False,
              local=False,
              methods=None,  #['FDR_I','FDR_C','FDR_G'],  # TODO:
              operation='intersection',  # TODO:
              mode='moran',  # TODO:
              somde_k=20,
              cluster_label='annotation',
              project_name=prefix,
              noweights=False,
              rho_mask_dropouts=False)

    # PLOTing
    regs = grn.regulon_dict
    for reg in list(regs.keys()):
        print(f'plotting {reg}')
        prn.plot_2d(grn.data, grn.auc_mtx, pos_label='spatial', reg_name=reg, fn=f'{out_dir}/{reg.strip("(+)")}.png')

    auc_mtx = grn.auc_mtx
    print(f'auc_mtx: {auc_mtx}')
    prn.auc_heatmap(data,
                    auc_mtx,
                    cluster_label='annotation',
                    rss_fn=f'{out_dir}/{method}_regulon_specificity_scores.txt',
                    topn=10,
                    subset=False,
                    save=True,
                    fn=f'{out_dir}/{method}_clusters_heatmap_top10.png',
                    legend_fn=f"{out_dir}/{method}_rss_celltype_legend_top10.png")
