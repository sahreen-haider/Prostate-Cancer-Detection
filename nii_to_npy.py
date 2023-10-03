import os
import nibabel as nib
import numpy as np
import streamlit as st

path = '/Users/sahreenhaider/Desktop/PROSTATEx_masks/Files/prostate/mask_prostate/'



def conversion(path):
    for _ in os.listdir(path):
        try:
            img = nib.load(path+'/'+_)
            data = img.get_fdata()
            for __ in range(data.shape[2]):
                np.save('/Users/sahreenhaider/Desktop/PROSTATEx_masks/Files/prostate/Images_mask/'+str(_.strip('.nii.gz') + str(__)+'.npy'), data[:, :, __])
        except Exception as e:
            continue


conversion(path)