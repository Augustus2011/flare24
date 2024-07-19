

# get started after cloning
-1 . cd /nnUNet
-2. pip install -e .

# download data and place in 
-1. /datasets/nnunet_data/segmentation
-2. /datasets/nnunet_data/segmentation/segmentations for placing the mask .nii.gz
-3. /datasets/nnunet_data/segmentation/volumns for placing the images .nii.gz

# run prepare.py
-1. before running do
    export nnUNet_preprocessed="./datasets/nnunet_data/nnUNet_preprocessed"
    export RESULTS_FOLDER="./resutls"
    export nnUNet_raw_data_base="./datasets/nnunet_data/nnUNet_raw"

-2. run prepare.py to save and split image,masks to folder


# preprocess and cropping
-1. run edit path in and run generate_task_json

-2. run nnUNet_plan_and_preprocess -t 501 -pl3d ExperimentPlanner3DFabiansResUNet_v21_Organs -pl2d None

