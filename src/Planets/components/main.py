from data_ingestion import Data,DataIngestion
from data_transformation import transformation


if __name__ == "__main__":

    Data_extraction = Data()
    # Data_extraction.ingestion_config()
    # Data_extraction.Dataextraction()
    print("Happened")
    Data_Ingestion = DataIngestion()
    Data_Ingestion.initiate_data_ingestion()

    Data_Transformation = transformation()
    Data_Transformation.row_data_transformation()