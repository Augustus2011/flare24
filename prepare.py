from utils.dataset import DataRenamer,DataSplitter


if __name__=="__main__":
    img="/Users/kunkerdthaisong/intern_cariva/flare24/datasets/nnunet_data/segmentation/volumes/"
    msk="/Users/kunkerdthaisong/intern_cariva/flare24/datasets/nnunet_data/segmentation/segmentations/"
    output="/Users/kunkerdthaisong/intern_cariva/flare24/datasets/nnunet_data/segmentation/split/"
    
    splitter = DataSplitter(images_dir=img,labels_dir=msk,output_dir=output,train_ratio=1.0,valid_ratio=0.0, delete_input=False)
    splitter.run()


    #output="/Users/kunkerdthaisong/intern_cariva/flare24/datasets/nnunet_data/segmentation/split"
    nnunet_data="/Users/kunkerdthaisong/intern_cariva/flare24/datasets/nnunet_data/nnUNet_raw"
    renamer=DataRenamer(path_to_input=output,path_to_output=nnunet_data,dataset_id=501,structure="FLARE")
    renamer.run()




# export nnUNet_raw="./datasets/nnunet_data/nnUNet_raw"
# export nnUNet_preprocessed="./datasets/nnunet_data/nnUNet_preprocessed"
# export nnUNet_results="./datasets/nnunet_data/nnUNet_results"


# export nnUNet_preprocessed="./datasets/nnunet_data/nnUNet_preprocessed"
# export RESULTS_FOLDER="./resutls"
# export nnUNet_raw_data_base="./datasets/nnunet_data/nnUNet_raw/"
