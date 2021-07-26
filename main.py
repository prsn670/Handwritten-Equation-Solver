from prep_data.download_and_extract import download_and_extract_data
from prep_data.extract_features import img_thing
from constants.constants import EXTRACTED_IMAGES, RESOURCE_DIR
import os
import pandas as pd


if __name__ == "__main__":
    train_data = []
    if not os.path.isdir(EXTRACTED_IMAGES):
        download_and_extract_data()
    else:
        print('file already exists')

    for folder in os.listdir(EXTRACTED_IMAGES):
        train_data.append(img_thing(folder))

    df = pd.DataFrame(train_data, index=None)
    df.to_csv(os.path.join(RESOURCE_DIR, 'train_final.csv'), index=False)
    print("done")
