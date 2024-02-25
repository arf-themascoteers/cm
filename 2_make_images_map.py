import os
import shutil
import pandas as pd

SOURCE_IMAGE_FOLDER = r"E:\data\cm\original\CM_Diff_ML_dataset"
DEST_IMAGES = r"E:\data\cm\dest\images"
INFO_SPEADSHEET = r"E:\data\cm\dest\info.csv"
DEST_SPREADSHEET = r"E:\data\cm\dest\map.csv"


def get_efficiency(folder,child):
    info = pd.read_csv(INFO_SPEADSHEET)
    info = info[(info["folder"]==folder) & (info["child"]==child)]
    if len(info) == 0:
        return None
    return info.iloc[0]["efficiency"]


def import_image(path, ID, folder, child):
    child = child.split(".")[0]
    e = get_efficiency(folder, child)
    if e is None:
        #print(f"Not imported {path}")
        return None
    else:
        dest = os.path.join(DEST_IMAGES, f"{ID}.tif")
        shutil.copy(path, dest)
        return e


def process():
    ID = 0
    data = []
    for folder in os.listdir(SOURCE_IMAGE_FOLDER):
        folder_path = os.path.join(SOURCE_IMAGE_FOLDER, folder)
        for child in os.listdir(folder_path):
            child_path = os.path.join(folder_path, child)
            e = -1
            if os.path.isdir(child_path):
                for grand_child in os.listdir(child_path):
                    file = os.path.join(child_path, grand_child)
                    e = import_image(file, ID, folder, child)

            else:
                e = import_image(child_path, ID, folder, child)
            if e is None:
                continue
            data.append([ID, e])
            print(folder,child,ID)
            ID = ID + 1
    df = pd.DataFrame(data, columns=['id', 'efficiency'])
    df.to_csv(DEST_SPREADSHEET, index=False)


if __name__ == "__main__":
    # e = get_efficiency("CJ1_BR1_BR2_D4_image_31-01-2023", "BR1_2")
    # print(e)

    process()
