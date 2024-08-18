
# get png by

in etc.ipynb we use sitk to read .nii.gz  and resize it to 512


# run preprocess contour diff

1. run preprocess domain_2 which is ct domain and masks

        python preprocess.py --data_directory data --domain_img_folder domain_2/images --domain_contour_folder domain_2/contours --domain_meta_path meta

2. run preprocess domain_2 which is mr domain and masks (we have no mr mask so just use ct mask)
      
        python preprocess.py --data_directory data --domain_img_folder domain_3/images --domain_contour_folder domain_3/contours --domain_meta_path meta_3


# train contour diff

1. train ct 2 mr 

        CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python3 train.py --input_domain CT --output_domain MR --data_directory /workspace/data --input_domain_img_folder domain_2/images --input_domain_contour_folder domain_2/contours --output_domain_img_folder domain_3/images --output_domain_contour_folder domain_3/contours --input_domain_meta_path /workspace/data/domain_2/meta --output_domain_meta_path  /workspace/data/domain_3/meta_3 --output_dir /workspace/checkout/ct_2_mr/ --contour_guided --img_size 512 --train_batch_size 16 --save_model_epochs 10

2. if you want to train mr 2 ct model 

        CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python3 train.py --input_domain MR --output_domain CT --data_directory /workspace/data --input_domain_img_folder domain_3/images --input_domain_contour_folder domain_3/contours --output_domain_img_folder domain_2/images --output_domain_contour_folder domain_2/contours --input_domain_meta_path /workspace/data/domain_3/meta_3 --output_domain_meta_path  /workspace/data/domain_2/meta_2 --output_dir /workspace/checkout/mr_2_ct/ --contour_guided --img_size 512 --train_batch_size 16 --save_model_epochs 10

3. example of continue training

        CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python3 train.py --input_domain MR --output_domain CT --data_directory /workspace/data --input_domain_img_folder domain_3/images --input_domain_contour_folder domain_3/contours --output_domain_img_folder domain_2/images --output_domain_contour_folder domain_2/contours --input_domain_meta_path /workspace/data/domain_3/meta_3 --output_domain_meta_path  /workspace/data/domain_2/meta --output_dir /workspace/checkout/mr_2_ct/ --contour_guided --img_size 512 --train_batch_size 16 --save_model_epochs 5 --check_point /workspace/checkout/mr_2_ct/model_epoch_35/unet/


# translation

translate ct 2 mr
    
    python translation.py   --input_domain CT   --output_domain MRI   --data_directory /workspace/data/   --input_domain_contour_folder /workspace/data/domain_2/contours  --input_domain_meta_path /workspace/data/domain_2/meta   --num_copy 1   --by_volume   --selected_epoch 40   --translating_folder_name /workspace/outputs/ --device "cuda"   --num_partition 1   --partition 0 --workers 16 --eval_batch_size 128


translate mr 2 ct

    python translation.py   --input_domain MRI   --output_domain CT   --data_directory /workspace/data/   --input_domain_contour_folder /workspace/data/domain_3/contours  --input_domain_meta_path /workspace/data/domain_3/meta_3   --num_copy 1   --by_volume   --selected_epoch 50   --translating_folder_name /workspace/outputs/   --device "cuda"   --num_partition 1   --partition 0 --workers 16 --eval_batch_size 128

# postprocess

pack png and transpose image to .nii.gz with same space, same affine from the original .

in pack_png2nii.ipynb 






