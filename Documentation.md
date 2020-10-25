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
- Moving from reading single character to reading lines 

- Simple convolutional network to recognize EMNIST characters.
- Construct a synthetic dataset of EMNIST lines.
- Move from reading single characters to reading lines.

- Train single epoch (for experiment) 
    - training/run_experiment.py '{"dataset": "EmnistDataset", "model": "CharacterModel", "network": "lenet", "train_args": {"epochs": 1}}'

- Subsampling data 
    - `subsample_fraction=0.1`
    - Run : training/run_experiment.py '{"dataset": "EmnistDataset", "dataset_args": {"subsample_fraction": 0.25}, "model": "CharacterModel", "network": "lenet"}'

- Making synthetic dataset of Emnist lines 
    - Sample sentences from Brown corpus
    - For each character, sample random EMNIST character and place on a line (with some random overlap)
    `notebooks/02-look-at-emnist-lines.ipynb`

- Reading multiple character at once 
    - Train CNN 
    - Use LeNet network -> applied to each character in sequence 
        - use `TimeDistributed` layer
        - express same network using all conv layers 
    - `notebooks/02b-cnn-for-simple-emnist-lines.ipynb`



    - Run: python training/run_experiment.py --save '{"train_args": {"epochs": 5}, "dataset": "EmnistLinesDataset", "dataset_args": {"max_length": 8, "max_overlap": 0}, "model": "LineModel", "network": "line_cnn_all_conv"}'




# Lab 3: Use sequence model for line text recognition
- Model, network, and loss
- Train an LSTM on EMNIST
    - `networks/line_lstm_ctc.py`
    - `models/line_model_ctc.py`

- Train LSTM with CTC loss 
    - Run : python training/run_experiment.py --save '{"train_args": {"epochs": 16}, "dataset": "EmnistLinesDataset", "model": "LineModelCtc", "network": "line_lstm_ctc"}'


# !!!! TODO in Lab3
- Code Encoder - Decoder architecture with attention 


# Lab 4: Train on real handwriting dataset and experiment W&B
- Introduce IAM handwriting dataset(lines dataset)
    - `notebooks/03-look-at-iam-lines.ipynb`
- Introduction to Weights & Biases
- Running multiple experiments in parallel
- Automate trials with hyper-parameter sweeps
- Try some ideas & review results on W&B


- Train LSTM w CTC model Line predictor on IAM 
    - 40 epochs get accuracy = 60%

    - Run : python training/run_experiment.py --save '{"dataset": "IamLinesDataset", "model": "LineModelCtc", "network": "line_lstm_ctc"}'


`training/prepare_experiments.py`
`training/gpu_manager.py`

- Run : `training/prepare_experiments.py training/experiments/sample.json`


```
python training/run_experiment.py --gpu=-1 '{"dataset": "EmnistDataset", "model": "CharacterModel", "network": "mlp", "network_args": {"num_layers": 2}, "train_args": {"batch_size": 256}, "experiment_group": "Sample Experiments 2"}'
python training/run_experiment.py --gpu=-1 '{"dataset": "EmnistDataset", "model": "CharacterModel", "network": "mlp", "network_args": {"num_layers": 4}, "train_args": {"batch_size": 256}, "experiment_group": "Sample Experiments 2"}'
python training/run_experiment.py --gpu=-1 '{"dataset": "EmnistDataset", "model": "CharacterModel", "network": "lenet", "train_args": {"batch_size": 256}, "experiment_group": "Sample Experiments 2"}'
```

- Run all in parallel 
    - `tasks/prepare_sample_experiments.sh | parallel -j2`



- Use Weight and Bias experiment tracking tool 
    - Run : `wandb init`
    
Goto : https://app.wandb.ai/<USERNAME>/fsdl-text-recognizer-project

How to implement W&B in training code?

Look at `training/run_experiment.py` and `training/util.py`


- Run 1st W&B experiment 
    - `tasks/train_character_predictor.sh`
    
wandb: Tracking run with wandb version 0.8.15
wandb: Run data is saved locally in wandb/run-20191116_020355-1n7aaz5g
wandb: Syncing run flowing-waterfall-1

- Run multiple experiment 
- Automatically run multiple experiments
- Config sweeps 




# Lab 5: Line Predictor : Detect line regions in an image of a whole param of text 
- Train model that input image containing lines of text, output pixelwise labeling of that image , 
each pixel belonging to either background, odd line of handwriting, even line of handwriting.
- Output of model -> find line regions -> image processing operation
- Dataset : IAM (lines + original sample forms, with annotate each line and word region)

- Run to load IAM dataset : `python text_recognizer/datasets/iam_dataset.py`
-> `~/fsdl-text-recognizer-project/data/raw/iam/iamdb/forms` (raw data file)


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
- Deploy ML model to production 


- Run 
    - python api/app.py

