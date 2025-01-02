import pandas as pd
import numpy as np
import scanpy as sc
from esda.moran import Moran
import sys
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
mpl.rcParams['svg.fonttype'] = 'none'


def make_adata(df, coor):
    adata = sc.AnnData(df)
    adata.obsm['spatial'] = coor.copy()
    return adata


def compute_weights(distances, neighborhood_factor=3):
    from math import ceil
    radius_ii = ceil(distances.shape[1] / neighborhood_factor)
    sigma = distances[:, [radius_ii - 1]]
    sigma[sigma == 0] = 1
    weights = np.exp(-1 * distances ** 2 / sigma ** 2)
    wnorm = weights.sum(axis=1, keepdims=True)
    wnorm[wnorm == 0] = 1.0
    weights = weights / wnorm
    return weights


def neighbors_and_weights(data,
                          latent_obsm_key="spatial",
                          n_neighbors=30,
                          neighborhood_factor=3):
    """
    :param data:
    :param latent_obsm_key:
    :param n_neighbors:
    :param neighborhood_factor:
    :param approx_neighbors:
    :return:
    """
    from sklearn.neighbors import NearestNeighbors
    coords = data.obsm[latent_obsm_key]
    # get Nearest n Neighbors
    nbrs = NearestNeighbors(n_neighbors=n_neighbors, algorithm="ball_tree").fit(coords)
    dist, ind = nbrs.kneighbors()  # neighbor name and index
    # dist and ind have the same shape: cell num * neighbor num
    # get spatial weights between two points
    weights = compute_weights(dist, neighborhood_factor=neighborhood_factor)
    ind_df = pd.DataFrame(ind, index=data.obs_names)
    neighbors = ind_df
    weights = pd.DataFrame(weights, index=neighbors.index, columns=neighbors.columns)
    return ind, neighbors, weights


def get_w(ind, weights_n):
    """Create a Weight object for esda program"""
    nind = pd.DataFrame(data=ind)
    nei = nind.transpose().to_dict('list')
    w_dict = weights_n.reset_index(drop=True).transpose().to_dict('list')
    from pysal.lib import weights
    w = weights.W(nei, weights=w_dict)
    return w


def cal_moran(df, data, reg_name):
    data = data[df.index]
    coor = data.obsm['spatial']
    adata = make_adata(df, coor)
    ind, neighbors, weights_n = neighbors_and_weights(adata, latent_obsm_key='spatial', n_neighbors=10)
    Weights = get_w(ind, weights_n)
    x = df[reg_name].to_numpy()
    i = Moran(x, Weights)
    return i


def moran_boxplot(moran_dict, idx, fn='moran_boxplot'):
    df = pd.DataFrame(moran_dict)
    df.index = idx
    print(df)
    df.to_csv(f'{fn}.csv', sep='\t')
    ax = sns.boxplot(data=df)
    plt.title("Moran's I Score")
    plt.ylabel('score')
    ax.set_xticklabels(['SpaGRN', 'pySCENIC'])
    plt.tight_layout()
    plt.savefig(f'{fn}.pdf', format='pdf')
    plt.close()


if __name__ == '__main__':
    # data = sc.read_h5ad('tumor19.h5ad')
    data = sc.read_h5ad(sys.argv[1])
    auc_grn = pd.read_csv('spg_global_moran/spg_auc.csv', index_col=0)
    auc_scenic = pd.read_csv('pyscenic/boost_auc.csv', index_col=0)
    isr_grn = data.obsm['isr']
    # regs = ['NFE2L2(+)','IRF6(+)']
    grn_regs = list(auc_grn.columns)
    scenic_regs = list(auc_scenic.columns)
    com_regs = list(set(grn_regs).intersection(scenic_regs))

    print(f'Found {len(com_regs)} regulons')

    # # 1. SpaGRN vs pySCENIC: spatial pattern measurement
    # results = {}
    # presults = {}
    # results['SpaGRN'] = []
    # results['pySCENIC'] = []
    # presults['SpaGRN'] = []
    # presults['pySCENIC'] = []
    # for reg in com_regs:
    #     i = cal_moran(auc_grn, data, reg)
    #     results['SpaGRN'].append(i.I)
    #     presults['SpaGRN'].append(i.p_norm)
    #     i2 = cal_moran(auc_scenic, data, reg)
    #     results['pySCENIC'].append(i2.I)
    #     presults['pySCENIC'].append(i2.p_norm)
    #
    # # plot boxplot
    # moran_boxplot(results, com_regs, fn='moran_sp')
    # moran_boxplot(presults, com_regs, fn='pvalue_sp')

    # 2. Z-score vs ISR
    results2 = {}
    results2['ISR'] = []
    # results2['AUC_zscore'] = results['SpaGRN']
    results2['AUC_zscore'] = []
    presults2 = {}
    presults2['ISR'] = []
    # presults2['AUC_zscore'] = presults['SpaGRN']
    presults2['AUC_zscore'] = []
    for reg in grn_regs:
        i = cal_moran(isr_grn, data, reg)
        results2['ISR'].append(i.I)
        presults2['ISR'].append(i.p_norm)
        i2 = cal_moran(auc_grn, data, reg)
        results2['AUC_zscore'].append(i2.I)
        presults2['AUC_zscore'].append(i2.p_norm)

    moran_boxplot(results2, grn_regs, fn='moran_ia')
    moran_boxplot(presults2, grn_regs, fn='pvalue_ia')
