import pickle
from pathlib import Path

import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem

FPS_SIZE = 128

with open(Path(__file__).parent / "fps_dec10_gb_bag_frac0_95_bag_freq10",
          "rb") as infile:
    clf = pickle.load(infile)


def ecfp(smiles, size):
    mol = Chem.MolFromSmiles(smiles)
    fp = AllChem.GetMorganFingerprint(mol, 4, useCounts=True, useFeatures=True)
    arr = np.zeros((size,), np.int32)
    for idx, v in fp.GetNonzeroElements().items():
        nidx = idx % size
        arr[nidx] += int(v)
    return arr


def score_smiles(smiles):
    """
    Single SMILES score.

    Parameters
    ----------
    smiles : str
        One SMILES
    Returns
    -------
    float
        Score for input SMILES
    """
    fps = ecfp(smiles, FPS_SIZE)
    return clf.predict_proba([fps])[:, 1]


def score_all(smileses):
    """
    Bulk scoring for all input SMILES-es.

    Parameters
    ----------
    smileses : iterable of string
        Iterable of SMILES-es to be scored
    Returns
    -------
    ndarray of float
        Scores for input SMILES-es
    """
    X = []
    for smiles in smileses:
        X.append(ecfp(smiles, FPS_SIZE))
    return clf.predict_proba(np.array(X))[:, 1]
