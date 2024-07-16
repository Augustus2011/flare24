from utils.dataset import DataRenamer,DataSplitter


if __name__=="__main__":
    img="/Users/kunkerdthaisong/intern_cariva/flare24/datasets/nnunet_data/segmentation/volumes/"
    msk="/Users/kunkerdthaisong/intern_cariva/flare24/datasets/nnunet_data/segmentation/segmentations/"
    output="/Users/kunkerdthaisong/intern_cariva/flare24/datasets/nnunet_data/segmentation/split/"
    
    splitter = DataSplitter(img, msk, output, 0.8, 0.2, delete_input=False)
    splitter.run()


    output="/Users/kunkerdthaisong/intern_cariva/flare24/datasets/nnunet_data/segmentation/split"
    nnunet_data="/Users/kunkerdthaisong/intern_cariva/flare24/datasets/nnunet_data/nnUNet_raw"
    renamer=DataRenamer(path_to_input=output,path_to_output=nnunet_data,dataset_id=500,structure="FLARE")
    renamer.run()




# export nnUNet_raw="./datasets/nnunet_data/nnUNet_raw"
# export nnUNet_preprocessed="./datasets/nnunet_data/nnUNet_preprocessed"
# export nnUNet_results="./datasets/nnunet_data/nnUNet_results"
