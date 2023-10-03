import os
import nibabel as nib


def loading_data_to_array(arg1, arg2):
    images = []
    masks = []
    for _ in range(len(os.listdir(arg1))):
      list_img = os.listdir(arg1)
      list_msk = os.listdir(arg2)
      try:
        img = nib.load(arg1+list_img[_])
        msk = nib.load(arg2+list_msk[_])
        data1 = img.get_fdata()
        data2 = msk.get_fdata()
        if data1.shape[2] ==  data2.shape[2]:
          for _ in range(data1.shape[2]):
            images.append(data1[:, :, _])
          for __ in range(data2.shape[2]):
            masks.append(data2[:, :, __])
        else:
          continue
      except:
        continue
    return images, masks