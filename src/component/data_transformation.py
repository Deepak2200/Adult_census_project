import os
import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass 
from src.utils import save_object


@dataclass
class DataTransformationConfig:
   preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
   
   def __init__(self):
      self.transformation_config = DataTransformationConfig()

   def get_data_transformation_object(self):
      try:
         logging.info('Data Transformation initiated')

         #segregating cat and num columns
         categorical_cols=['workclass', 'education','occupation', 'race', 'sex',]
         numerical_cols=['age', 'education_num', 'capital_gain',"capital_loss", 'hours_per_week',]
         
         
         logging.info('Pipeline Initiated')
         #Numerical Pipeline
         num_pipeline = Pipeline(
            steps=[
               ('Imputer',SimpleImputer(strategy='median')),
               ('scaler',StandardScaler())
            ]
         )
         #categorical Pipeline
         cat_pipeline = Pipeline(
            steps=[
               ('imputer',SimpleImputer(strategy='most_frequent')),
               ('Onehotencode',OneHotEncoder(sparse_output=False)),
               ('scaler',StandardScaler())
            ]
         )

         preprocessor = ColumnTransformer([
               ('num_pipeline',num_pipeline,numerical_cols),
               ('cat_pipeline',cat_pipeline,categorical_cols)
            ]
         )

         logging.info('Pipeline completed')
         
         return preprocessor

      except Exception as e:
         logging('Exception occured at Data Transformation')
         raise CustomException(e,sys)
   
   def initiate_data_transformation(self,train_path,test_path):
      try:
         #Reading train and tests data
         train_df = pd.read_csv(train_path)
         test_df = pd.read_csv(test_path)
         logging.info('Read train and test data completed')

         logging.info(f"train data frame of data {train_df.info()}")
         logging.info(f"train data frame of data {test_df.info()}")
         

         #target income column
         income_map = {'<=50K':0, '>50K':1}
         train_df['salary'] = train_df['salary'].map(income_map)
         test_df['salary'] = test_df['salary'].map(income_map)
         logging.info('Mapping Target salary column')

         

         #Viewing train and test data of first five rows
         logging.info(f'Train dataframe head:\n {train_df.head().to_string()}')
         logging.info(f'Test dataframe head: \n {test_df.head().to_string()}')

         logging.info('Obtaining preprocessor object')
         preprocessor_obj = self.get_data_transformation_object()

         logging.info("target columns get initiated")

         target_column = "salary"
         drop_columns = ["salary","fnlwgt","marital-status","country","relationship"]

         
         logging.info("input train feature started")


         input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
         target_feature_train_df = train_df[target_column]

         input_feature_test_df = test_df.drop(columns=drop_columns,axis=1)
         target_feature_test_df = test_df[target_column]

         logging.info(f'Train dataframe head:\n {input_feature_train_df.head().to_string()}')
         logging.info(f'test dataframe head:\n {input_feature_test_df.head().to_string()}')
         

         logging.info("train test feature get into columns")
         logging.info("preprocessor started")
         
         #Transforming using preprocessor obj
         input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
         input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)
   

         logging.info('Applying preprocessing object on training and testing datasets')

         train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
         test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

         save_object(
            file_path = self.transformation_config.preprocessor_obj_file_path,
            obj = preprocessor_obj
         )
         logging.info('Preprocessor pickle file saved')

         return(
            train_arr,
            test_arr,
            self.transformation_config.preprocessor_obj_file_path
         )

      except Exception as e:
         logging.info('Exception occured at initiatede data transformation')
         raise CustomException(e,sys)
      


            

            
       
