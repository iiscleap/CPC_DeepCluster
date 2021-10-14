# CPC_DeepCluster
This is the implementation of "SELF SUPERVISED REPRESENTATION LEARNING WITH DEEP CLUSTERING FOR ACOUSTIC UNIT DISCOVERY FROM RAW SPEECH" submitted to ICASSP 2022
<<<<<<< HEAD

## setup instructions

1) Clone the repo:
`https://github.com/iiscleap/CPC_DeepCluster.git`

2) Install libraries which would be required for torch-audio https://github.com/pytorch/audio :
 * Linux: `sudo apt-get install sox libsox-dev libsox-fmt-all`

3) `conda env create -f environment.yml && conda activate cpc37`

4) Run setup.py
`python setup.py develop`

## Using the Repository

To start the training :

```bash 
python cpc/train_mod.py --pathDB $PATH_AUDIO_FILES --pathCheckpoint $PATH_CHECKPOINT_DIR --LabelsPath $Path_Pseudo_Labels --file_extension $EXTENSION --normMode batchNormn--rnnMode linear --nLevelsGRU 2 --max_size_loaded 1000000000 --save_step 1 --alpha_val $Cluster_Loss_Weighting
```

Where:
- $PATH_AUDIO_FILES is the directory containing the audio files. The files should be arranged as below:
```
PATH_AUDIO_FILES
│
└───speaker1
│   └───...
│         │   seq_11.{$EXTENSION}
│         │   seq_12.{$EXTENSION}
│         │   ...
│
└───speaker2
    └───...
          │   seq_21.{$EXTENSION}
          │   seq_22.{$EXTENSION}
```
- $PATH_CHECKPOINT_DIR in the directory where the checkpoints will be saved
- $EXTENSION is the extension of each audio file
- $Path_Pseudo_Labels is the directory that contains the psuedo labels of all the audio files in $PATH_AUDIO_FILES
- $Cluster_Loss_Weighting provides the weighting factor for the cluster loss. 

## Restarting the session

To restart a session from the last save checkpoint  run
```bash
python cpc/train_mod.py --pathCheckpoint $PATH_CHECKPOINT_DIR
```
## Generating the pseudo labels for training

Create quantized.txt using the repository [here](https://github.com/bootphon/zerospeech2021_baseline)
```bash
python create_pseudolabels.py --input_file $Path_Containing_quantized.txt --out_path $Output_Dir
```
- $Output_Dir is the directory where .pt files containing pseudo labels

## Extracting features, training K Means and Language Models

Extract the features for K means clustering and train K Means clustering, Language models  using the repository [here](https://github.com/bootphon/zerospeech2021_baseline)


=======
>>>>>>> f6709e28057c8fc7c4c970f24deae6e65130264d
