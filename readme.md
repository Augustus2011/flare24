

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
    export nnUNet_results="./resutls"
    export nnUNet_raw="./datasets/nnunet_data/nnUNet_raw"

    export nnUNet_preprocessed="/workspace/datasets/nnunet_data/nnUNet_preprocessed"
    export nnUNet_results="/workspace/datasets/nnunet_data/nnUNet_results/"
    export nnUNet_raw="/workspace/datasets/nnunet_data/nnUNet_raw"

-2. run prepare.py to save and split image,masks to folder

# preprocess and cropping
-1. run edit path in and run 
python prepare.py
generate_dataset_json
nnUNetv2_plan_and_preprocess -d 100 --verify_dataset_integrity

    nnUNetv2_plan_and_preprocess -d 100 -pl nnUNetPlannerResEncM -c 3d_lowres --verify_dataset_integrity

nnUNetv2_plan_and_preprocess -d 101 -pl nnUNetPlannerResEncM -c 3d_fullres --verify_dataset_integrity


to run preprocess pls update ram
docker update --memory="100g"  --memory-swap="110g" c61f67d3a403

# run training
nnUNetv2_train Dataset100_FLARE -p nnUNetResEncUNetLPlans 3d_fullres 5 -num_gpus 2

nnUNetv2_train Dataset100_FLARE 3d_lowres 5 -num_gpus 2
add more batch_size
3d_lowres can be ['2d', '3d_lowres', '3d_fullres', '3d_cascade_fullres']

nnUNetv2_train Dataset100_FLARE -p nnUNetResEncUNetMPlans 3d_lowres 1 -num_gpus 2

nnUNetv2_train Dataset102_FLARE -p nnUNetResEncUNetMPlans 3d_lowres 1 -num_gpus 1 --c

nnUNetv2_predict_from_modelfolder -i inputs/ -o outputs/ -m /workspace/datasets/nnunet_data/nnUNet_results/Dataset100_FLARE/nnUNetTrainer__nnUNetResEncUNetMPlans__3d_lowres  -f 1 -chk checkpoint_best.pth -device cuda


nnUNetv2_train Dataset103_FLARE 3d_lowres 1 -num_gpus 2
