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
