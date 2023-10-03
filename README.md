# Prostate_Cancer_Detection

The Project is to Detect Breast Cancer using MRI's(mpMRI's bpMRI's) Dataset

This a U-net model with resnet-34 as its backbone which is trained over 3492 samples 

with MRI's containing both of MRI's with their segmented Masks.

The model also uses ImageDataGenerator from keras.preprocessing to agument data.

The final model has achieved an IOU score of 0.6490418542704078


# Below shows a sample of Testing image on which model is doing the segmentation and deriving mask for it.

![image](https://user-images.githubusercontent.com/81517526/233560858-691c65fb-d6d5-4a96-9369-5d91699fd4ab.png)
