from torch.utils.data import Dataset
import torch
from PIL import Image
import torchvision.transforms as transforms
import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler


class CMDataset(Dataset):
    def __init__(self):
        self.images_path = r"E:\data\cm\dest\images"
        self.csv = r"E:\data\cm\dest\map.csv"
        self.df = pd.read_csv(self.csv)
        self.data = self.df.values.tolist()
        for i in range(len(self.data)):
            self.data[i] = str(int(self.data[i]))

        scaler = MinMaxScaler()
        column_to_scale = [row[1] for row in self.data]
        scaled_column = scaler.fit_transform([[value] for value in column_to_scale])

        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.485, 0.485], std=[0.229, 0.229, 0.229])
        ])

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        sample = self.data[idx]
        the_id = sample["id"]
        efficiency = sample["efficiency"]
        file_path = os.path.join(self.images_path,f"{the_id}.tif")
        image = Image.open(file_path)
        image = self.transform(image)
        target = torch.tensor(efficiency, dtype=torch.float32)
        return image, target


if __name__ == "__main__":
    dataset = CMDataset()
    from torch.utils.data import DataLoader
    dataloader = DataLoader(dataset, batch_size=3, shuffle=True)

    for image, target in dataloader:
        print(image.shape)
        print(target)