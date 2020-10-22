# Lab 1 
- Single character prediction: Train model to solve simple version of line text recognition 
- Use base model MLP/CNN 
- Write test for the model 
- Download EMNIST data(character prediction dataset)
- Run simple base model 
- Folder structure:
    - text_recognizer/networks/mlp.py
    - text_recognizer/networks/lenet.py
    - text_recognizer/models/base.py
    - text_recognizer/models/character_model.py

    - training/util.py

- Run
    - Train MLP/ CNN
        - training/run_experiment.py --save \
  '{"dataset": "EmnistDataset", "model": "CharacterModel", "network": "mlp",  "train_args": {"batch_size": 256}}'
    - Try larger MLP, with smaller batch size
        - training/run_experiment.py \
  '{"dataset": "EmnistDataset", "model": "CharacterModel", "network": "mlp", "network_args": {"num_layers": 8}, "train_args": {"batch_size": 128}}'

- Test
    - `pytest -s text_recognizer/tests/test_character_predictor.py`

# Lab 2

- Simple convolutional network to recognize EMNIST characters.
- Construct a synthetic dataset of EMNIST lines.
- Move from reading single characters to reading lines.

# Lab 3
- Model, network, and loss
- Train an LSTM on EMNIST

# Lab 4
- Introduce IAM handwriting dataset
- Introduction to Weights & Biases
- Running multiple experiments in parallel
- Automate trials with hyper-parameter sweeps
- Try some ideas & review results on W&B


# Lab 5
- Training data augmentation
- Ensemble 2 models 


# Lab 6: Data labeling & versioning
- Data labeling
- Export data and update metadata file
- Training on the new dataset


# Lab 7: Test & CI/ CD
- Test
- Py lint
- CircleCI set up


# Lab 8: Deployment

- Run LinePredictor as a web app, and send it some requests
- Dockerize
- Deploy app to production 