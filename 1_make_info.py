import pandas as pd
import math


SOURCE_IMAGE_FOLDER = r"E:\data\cm\original\CM_Diff_ML_dataset"
SOURCE_SPREADSHEET = r"E:\data\cm\original\CM_diff_ML_data_des.xlsx"
DEST_SPREADSHEET = r"E:\data\cm\dest\info.csv"

folders = []
image_or_subfolder = []


def is_new(folder_name):
    if isinstance(folder_name, float) and math.isnan(folder_name):
        return False
    else:
        return True


def process():
    df = pd.read_excel(SOURCE_SPREADSHEET, sheet_name=0)
    for index, row in df.iterrows():
        folder_name = row["Folder name"]
        if is_new(folder_name):
            folders.append({"name":folder_name, "children":[]})
        image_or_subfolder_name = row["Image/folder name"]
        efficiency = row["Efficiency in percentage"]
        folders[-1]["children"].append({"name": image_or_subfolder_name, "efficiency": efficiency})


if __name__ == "__main__":
    process()
    data = []
    for folder in folders:
        for child in folder["children"]:
            row = []
            row.append(folder["name"])
            row.append(child["name"])
            row.append(child["efficiency"])
            data.append(row)
    df = pd.DataFrame(data, columns=['folder', 'child', 'efficiency'])
    df.to_csv(DEST_SPREADSHEET, index=False)

