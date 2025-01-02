#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: Created on 15 Jul 2024 17:23
# @Author: Yao LI
# @File: SpaGRN/new_data.py
"""
Handle new data and
perform new analysis
e.g. plotting
"""
import pandas as pd
import scanpy as sc
import numpy as np
import anndata as ad
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
mpl.rcParams['svg.fonttype'] = 'none'
mpl.rcParams["ytick.labelright"] = True
mpl.rcParams["ytick.labelleft"] = False


def handle_merfish(fn):
    df = pd.read_csv(fn)
    meta_columns = df.columns[:9]
    meta = df[meta_columns].set_index('Cell_ID')
    exp = df.drop(labels=meta_columns, axis=1)
    X = exp.to_numpy()
    adata = ad.AnnData(X, dtype=X.dtype)
    adata.var_names = list(exp.columns)
    adata.obs_names = list(meta.index)
    adata.obs = meta
    adata.obsm['spatial'] = meta[['Centroid_X', 'Centroid_Y']].to_numpy()
    return adata


# def plot_venn(more_stats):
#     from matplotlib_venn import venn3, venn2
#     fdr_threshold=0.05
#     moran_genes = more_stats.loc[more_stats.FDR_I < fdr_threshold].index
#     geary_genes = more_stats.loc[more_stats.FDR_C < fdr_threshold].index
#     getis_genes = more_stats.loc[more_stats.FDR_G < fdr_threshold].index
#     hs_genes = more_stats.loc[(more_stats.FDR < fdr_threshold)].index
#     venn3([set(moran_genes), set(geary_genes), set(getis_genes)], ('morani', 'gearyc', 'getisg'))
#     plt.savefig('venn3.png')
#     plt.close()
#     from venny4py.venny4py import *
#     sets = {
#         'morani': set(moran_genes),
#         'gearyc': set(geary_genes),
#         'getisg': set(getis_genes),
#         'ver1': set(hs_genes)}
#     venny4py(sets=sets)
#     somde_genes = more_stats.loc[more_stats.FDR_SOMDE < fdr_threshold].index
#     global_inter_genes = set.intersection(set(moran_genes), set(geary_genes), set(getis_genes), set(hs_genes))
#     venn2([set(somde_genes), set(global_inter_genes)], ('local', 'global'))
#     plt.savefig('venn2.png')
#     plt.close()


def regulon_venn(regulon_dict1, regulon_dict2):
    from matplotlib_venn import venn2
    venn2([set(regulon_dict1.keys()), set(regulon_dict2.keys())], ('regulon1', 'regulon2'))
    plt.savefig('venn2.png')
    plt.close()


def targets_venn(tf, regulon_dict1, regulon_dict2):
    tf = tf + '(+)' if '(+)' not in tf else tf
    from matplotlib_venn import venn2
    venn2([set(regulon_dict1[tf]), set(regulon_dict2[tf])], ('SpaGRN', 'pySCENIC'))
    plt.title(tf)
    plt.savefig(f'{tf.replace("(+)","")}_targets_venn.pdf', format='pdf')
    plt.close()


def jaccard_similarity(list1, list2):
    set1, set2 = set(list1), set(list2)
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union


def jaccard_heatmap(dict1, dict2, ylabel="moranr", xlabel="gearyc", fn='jaccard_heatmap.png'):
    # Get the list of unique TF names from both lists
    tf_names = sorted(set(dict1.keys()).union(dict2.keys()))
    # Initialize a matrix to hold Jaccard similarity scores
    jaccard_matrix = np.zeros((len(tf_names), len(tf_names)))
    # Calculate Jaccard similarity scores
    for i, tf1 in enumerate(tf_names):
        for j, tf2 in enumerate(tf_names):
            if tf1 in dict1 and tf2 in dict2:
                jaccard_matrix[i, j] = jaccard_similarity(dict1[tf1], dict2[tf2])
    # Plot heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(jaccard_matrix, xticklabels=False, yticklabels=False, cmap="viridis")
    plt.title("Jaccard Similarity Heatmap")
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.savefig(fn)


def get_module_targets(modules):
    """
    同上 (before_cistarget)
    :param modules:
    :return:
    """
    d = {}
    for module in modules:
        tf = module.transcription_factor
        tf_mods = [x for x in modules if x.transcription_factor == tf]
        targets = []
        for i, mod in enumerate(tf_mods):
            targets += list(mod.genes)
        d[tf] = list(set(targets))
    return d


if __name__ == '__main__':
    # Part 1
    # fn = 'Moffitt_and_Bambah-Mukku_et_al_merfish_all_cells.csv'
    # adata = handle_merfish(fn)
    # adata.write('/dellfsqd2/ST_OCEAN/USER/liyao1/07.spatialGRN/exp/13.revision/new_data/Moffitt_and_Bambah-Mukku_et_al_merfish_all_cells.h5ad')

    # Part 2
    # df = pd.read_csv('MB_more_stats.csv', sep='\t', index_col=0)
    # plot_venn(df)

    # Part 3
    tf_fn = '/dellfsqd2/ST_OCEAN/USER/liyao1/06.stereopy/resource/tfs/allTFs_mm.txt'
    with open(tf_fn, 'r') as f:
        tf_list = f.read().splitlines()
    local_correlations = pd.read_csv('/dellfsqd2/ST_OCEAN/USER/liyao1/07.spatialGRN/exp/13.revision/mouse_brain/local_correlations.csv')
    adj_mr = pd.read_csv('/dellfsqd2/ST_OCEAN/USER/liyao1/07.spatialGRN/exp/13.revision/mouse_brain/local_correlations_bv_mr.csv')
    adj_gc = pd.read_csv('/dellfsqd2/ST_OCEAN/USER/liyao1/07.spatialGRN/exp/13.revision/mouse_brain/local_correlations_bv_gc.csv')
    fn = '/dellfsqd2/ST_OCEAN/USER/liyao1/07.spatialGRN/DATA/Mouse_brain_cell_bin.h5ad'
    rho_mask_dropouts = False
    adata = sc.read_h5ad(fn)
    common_tf_list = list(set(tf_list).intersection(set(adata.var_names)))
    # reshape matrix
    local_correlations['TF'] = local_correlations.columns
    local_correlations = local_correlations.melt(id_vars=['TF'])
    local_correlations.columns = ['TF', 'target', 'importance']
    local_correlations = local_correlations[local_correlations.TF.isin(common_tf_list)]
    # remove if TF = target
    adj = local_correlations[local_correlations.TF != local_correlations.target]
    matrix = adata.to_df()
    from pyscenic.utils import modules_from_adjacencies
    modules = list(modules_from_adjacencies(adj, matrix, rho_mask_dropouts=rho_mask_dropouts))
    modules_mr = list(modules_from_adjacencies(adj_mr, matrix, rho_mask_dropouts=rho_mask_dropouts))
    modules_gc = list(modules_from_adjacencies(adj_gc, matrix, rho_mask_dropouts=rho_mask_dropouts))
    dict_og = get_module_targets(modules_mr)
    dict_mr = get_module_targets(modules_mr)
    dict_gc = get_module_targets(modules_gc)
    jaccard_heatmap(dict_og, dict_mr, ylabel="hotspot", xlabel="moranr", fn='hotspot_moranr_jaccard_heatmap.png')
