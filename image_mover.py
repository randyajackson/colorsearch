import pandas as pd
import os

data = pd.read_csv("all_data_info_in_train.csv")
for x in range(501,1000):
    print(data['new_filename'][x])
    src = 'F:/art_data/train set (must be used)/train/' + data['new_filename'][x]
    dest = 'F:/art_data/train set (must be used)/train/images_for_upload/' + data['new_filename'][x]

    os.rename(src, dest)


