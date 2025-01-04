import os
from main import create_images, PatientData, ImageType
test_dir = os.path.dirname(os.path.realpath(__file__))

#pat = PatientData(birth_date_iso="2022-09-13", albumin_serum=1000, albumin_csf=10, igg_serum=200, igg_csf=1)

#create_images(data=pat, out_file="test", image_type=ImageType.PNG)

for file in os.listdir(test_dir):
    print("ccc", file)
    if file.endswith(".png"):
        print("file", file)