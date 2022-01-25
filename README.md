# MF-Score

## Installation
1. Create new conda environment (or use already created):
    ```bash
    conda create --name new_env python>=3.6
    conda activate new_env
    ```
2. Install `rdkit` if not already installed:
    ```bash
    conda install -c conda-forge rdkit
    ```
3. Install MF-Score, where `project_root` is the root directory of the project
     ```bash
     cd $project_root
     python3 setup.py develop
     ```
For `venv` based virtual environment, this should also work if you somehow
install `rdkit` (it is possible).

## Exemplary usage
```python
>>> from mfscore.ocsvm import score_smiles, score_all
>>> aspirin = "O=C(C)Oc1ccccc1C(=O)O"
>>> cholesterol = "C[C@H](CCCC(C)C)[C@H]1CC[C@@H]2[C@@]1(CC[C@H]3[C@H]2CC=C4[C@@]3(CC[C@@H](C4)O)C)C"
>>> score_smiles(aspirin)
10.232122084989555
>>> score_all([aspirin, cholesterol])
array([  10.23212208, -412.95839636])
```
