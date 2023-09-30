# LIBRARIES
import pandas as pd
from dataclasses import dataclass
import os
from sklearn.model_selection import train_test_split # Dividing into X_train, X_test, y_train,y_test
import zipfile

@dataclass
class DataIngestionConfig:
    base_data_path: str = '../../../artifacts/'
    X_train_data_path: str = os.path.join(base_data_path, 'X_train.csv')
    X_test_data_path: str = os.path.join(base_data_path, 'X_test.csv')
    y_test_data_path: str = os.path.join(base_data_path, 'y_test.csv')
    y_train_data_path: str = os.path.join(base_data_path, 'y_train.csv')


class Data:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    # Extract the file from ZIP
    def Dataextraction(self):
        # Extract the zip file
        with zipfile.ZipFile('C:/Users/doguy/Desktop/Planets/data.zip', 'r') as zip_ref:
            zip_ref.extractall('C:/Users/doguy/Desktop/Planets/artifacts/')

        # Read the row dataset
        data = pd.read_csv("C:/Users/doguy/Desktop/Planets/artifacts/data.csv")

        #Save the dataset as csv file into "artifacts" folder
        os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
        data.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
            
        os.makedirs(self.ingestion_config.base_data_path, exist_ok=True)
        
        # Read the data
        df = pd.read_csv(os.path.join(self.ingestion_config.base_data_path, 'designed_data.csv'))

        # Independent columns and dependent column
        X = df.drop("Planet Name", axis = 1)
        y = df["Planet Name"]

        # Splitting
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

        # Save them as csv file
        X_train.to_csv(self.ingestion_config.X_train_data_path,index=False,header=True)
        X_test.to_csv(self.ingestion_config.X_test_data_path,index=False,header=True)

        y_train.to_csv(self.ingestion_config.y_train_data_path,index=False,header=True)
        y_test.to_csv(self.ingestion_config.y_test_data_path,index=False,header=True)

        return(
            self.ingestion_config.X_train_data_path,
            self.ingestion_config.y_test_data_path,
            self.ingestion_config.y_train_data_path,
            self.ingestion_config.X_test_data_path
        )