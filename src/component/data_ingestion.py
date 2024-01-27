import os
import sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.component.data_transformation import DataTransformation
from src.utils import space_remover


# initialize the Data Ingestion Configaration

@dataclass
class DataIngestionconfig:
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts","raw.csv")


# create a class for data ingestion
class DataIngetion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion method Start")
        try:
            df=pd.read_csv(os.path.join("dataset","cleaned_adult.csv"))
            logging.info("Dataset read as pandas DataFrame")
            #Removing white space from categorical columns mainly of -> '<=50K'and'>50k'
            df = space_remover(df)
            

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("Tain_test_split")

            train_set,test_set=train_test_split(df,test_size=0.30)

            train_set=train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set=test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("data ingetion is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        except Exception as e:
            logging.info("Exception occured at data ingestion stage")
            raise CustomException(e,sys)
    



        
