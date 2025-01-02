#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: Created on 28 Aug 2024 19:15
# @Author: Yao LI
# @File: SpaGRN/plot_rep_exp_reg.py.py
import pandas as pd
import numpy as np
import scanpy as sc
from esda.moran import Moran
import sys
sys.path.append('/dellfsqd2/ST_OCEAN/USER/liyao1/07.spatialGRN/')
import spagrn_debug.plot as prn

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
mpl.rcParams['svg.fonttype'] = 'none'


def cal_isr_exp(data, regulon, receptor, weight=1):
    regulon = f'{regulon}(+)' if '(+)' not in regulon else regulon
    exp_mtx = data.to_df()
    receptor_exp_mtx = exp_mtx[receptor]
    # receptor_exp_mtx = receptor_exp_mtx * weight
    normalized_receptor_exp_mtx = (receptor_exp_mtx - np.min(receptor_exp_mtx)) / (np.max(receptor_exp_mtx) - np.min(receptor_exp_mtx))
    normalized_receptor_exp_mtx = normalized_receptor_exp_mtx * weight
    regulon_auc_mtx = data.obsm['auc_mtx'][regulon]
    # combine regulon AUC value and receptor expression value
    df = pd.concat([normalized_receptor_exp_mtx, regulon_auc_mtx], axis=1)
    # sum receptor expression value
    isr = df[regulon] + df[receptor]
    return isr


if __name__ == '__main__':
    output_dir = 'receptor_isr'
    adata = sc.read_h5ad('/dellfsqd2/ST_OCEAN/USER/liyao1/07.spatialGRN/exp/14.new_data/13.slideseq3/output/spg_global_moran/isr.h5ad')
    coor = adata.obsm['spatial']
    # reg_rep_combo = [
    #     ('Emx1', 'Nlgn1'),
    #     ('Gbx1', 'Nrp2'),
    #     ('Gbx1', 'Ptpro'),
    #     ('Hivep2', 'Epha3'),
    #     ('Hivep2', 'Ephb1'),
    #     ('Hivep2', 'Ptprk'),
    #     ('Hivep2', 'Nrp1'),
    #     ('Hivep2', 'Islr2'),
    #     ('Lhx8', 'Nrp2'),
    #     ('Lhx8', 'Cntnap2'),
    #     ('Neurod1', 'Epha3'),
    #     ('Neurod1', 'Nrp2'),
    #     ('Rarb', 'Islr2'),
    #     ('Zeb1', 'Cdh4')
    # ]
    reg_rep_combo = [
        ('Hivep2', 'Nrp1'),
        ('Neurod1', 'Nrp2'),
        ('Zeb1', 'Cdh4')
    ]

    weights = [1]#, 0.5, 0.3]
    for regulon, receptor in reg_rep_combo:
        for w in weights:
            mtx = cal_isr_exp(adata, regulon, receptor, weight=w)
            prn.plot_isr(mtx, coor, regulon, receptor, s=1, fn=f'{output_dir}/{regulon.strip("(+)")}_{receptor}_weight{w}.pdf')
