# Local dev
- `conda env create`

- `export PYTHONPATH="$PWD"`
To run Jupyter notebook with conda env kernel 
- conda install jupyter
- conda install nb_conda
- conda install ipykernel
- python -m ipykernel install --user --name mykernel

# GCP AI Platform Notebooks instance






## Run test
- `pytest -s text_recognizer/tests/test_character_predictor.py`
- `pytest -s text_recognizer`