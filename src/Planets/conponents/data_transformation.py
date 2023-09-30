# Clean the train.csv --> Dropping (The columns that has more than 1000 null value and unecessary columns)
# Clean the train.csv --> Dropping (The columns that has more than 1000 null value and unecessary columns)
# Median Imputation (to numerical columns)
# Categorical Frequency Imputation (to categorical columns)
# y = 'Planet Name'
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import os
from dataclasses import dataclass
import pandas as pd
from common import rename_columns
from additional import fill_missing_with_median,fill_missing_with_frequency,result_df_preprocessing


@dataclass
class DataIngestionConfig:
    base_data_path: str = '../../../artifacts/'

class transformation:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def row_data_transformation(self):
        y = 'Planet Name'
        data = pd.read_csv(os.path.join(self.ingestion_config.base_data_path, "data.csv"))
        planets = pd.read_csv(os.path.join(self.ingestion_config.base_data_path, "planets.csv"))
        # src/Planets/Conponents
        rename_columns(data,planets["Long_Name"])

        result_df = fill_missing_with_median(data) #Median Imputation
        result_df = fill_missing_with_frequency(result_df) # Categorical Frequency Imputation
        result_df = result_df_preprocessing(result_df) # Other necessary preprocessing
        result_df.isnull().sum()
        result_df.to_csv(os.path.join(self.ingestion_config.base_data_path, "designed_data.csv", index=False))


