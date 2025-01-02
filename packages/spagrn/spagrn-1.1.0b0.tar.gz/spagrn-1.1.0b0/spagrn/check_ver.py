#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: Created on 22 Dec 2024 22:16
# @Author: Yao LI
# @File: SpaGRN/check_ver.py
from importlib.metadata import version

import anndata
import hotspot
import pickle
import pandas as pd
from copy import deepcopy
from multiprocessing import cpu_count
from typing import Sequence, Type, Optional

from dask.diagnostics import ProgressBar
from dask.distributed import Client, LocalCluster

from ctxcore.genesig import Regulon, GeneSignature
from arboreto.algo import grnboost2
from ctxcore.rnkdb import FeatherRankingDatabase as RankingDatabase
from pyscenic.utils import modules_from_adjacencies
from pyscenic.aucell import aucell, derive_auc_threshold
from pyscenic.prune import prune2df, df2regulons

# modules in self project
from .scoexp import ScoexpMatrix
from .network import Network
from .autocor import *
from .corexp import *

import pandas as pd
from multiprocessing import cpu_count
from spagrn_debug.regulatory_network import InferNetwork as irn
import spagrn_debug.plot as prn
import scanpy as sc

import os
import sys
import time
import scanpy as sc
import numpy as np
import pandas as pd
import anndata as ad
import scipy
from scipy.sparse import csr_matrix, issparse
import multiprocessing
from tqdm import tqdm

import anndata
import pandas as pd
import numpy as np
import scanpy as sc
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Optional
from pyscenic.rss import regulon_specificity_scores
import matplotlib as mpl



numpy_version = version("numpy")
print("Numpy version:", numpy_version)

pandas_version = version("pandas")
print("Pandas version:", pandas_version)
