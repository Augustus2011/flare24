

# after cloning
1. build image
    
        docker build -t nnunet_finetune .

2. run docker and mount volumn

        docker run -d -it --ipc=host --gpus all --memory="100g"  --memory-swap="110g" -v /mnt/ai_neuro/august_kun/miccai/flare24:/app/datasets nnunet_finetune

3. setup project by

        docker exec -it <container_id> /bin/bash

4. cd to nnunet then do
        
        pip install -e .

# move data to
pls check your input dim,values
1. for input mask .nii.gz in /workspace/datasets/nnunet_data/segmentation/segmentations 
2. for images volumns .nii.gz in 
/workspace/datasets/nnunet_data/segmentation/volumns

# preprocesing

1. do 

        export nnUNet_preprocessed="/workspace/datasets/nnunet_data/nnUNet_preprocessed"
        export nnUNet_results="/workspace/datasets/nnunet_data/nnUNet_results/"
        export nnUNet_raw="/workspace/datasets/nnunet_data/nnUNet_raw"

2. run prepare.py to save and split image,masks to folder (you can change your configs nameformat,dataset id) in prepare.py
    
        python prepare.py 


3. change config in /workspace/nnUNet/nnunetv2/dataset_conversion/generate_dataset_json.py  and run

        generate_dataset_json

4. run nnunet preprocess

        nnUNetv2_plan_and_preprocess -d 100 -pl nnUNetPlannerResEncM -c 3d_lowres --verify_dataset_integrity



# training

    nnUNetv2_train Dataset100_FLARE -p nnUNetResEncUNetMPlans 3d_lowres 1 -num_gpus 1

for continue    

    nnUNetv2_train Dataset100_FLARE -p nnUNetResEncUNetMPlans 3d_lowres 1 -num_gpus 1 --c

# predicting
place data in /workspace/inputs/ then run 

    nnUNetv2_predict_from_modelfolder -i inputs/ -o outputs/ -m /workspace/datasets/nnunet_data/nnUNet_results/Dataset100_FLARE/nnUNetTrainer__nnUNetResEncUNetMPlans__3d_lowres  -f 1 -chk checkpoint_best.pth -device cuda


