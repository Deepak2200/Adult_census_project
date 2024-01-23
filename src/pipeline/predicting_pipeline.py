import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object


class PredictionPipeline:
   def __init__(self):
      pass

   def predict(self,features):
      try:
         preprocessor_path = os.path.join('artifacts','preprocessor.pkl')
         model_path = os.path.join('artifacts','model.pkl')

         preprocessor = load_object(preprocessor_path)
         model = load_object(model_path)

         data_scaled = preprocessor.transform(features)

         pred = model.predict(data_scaled)

         return pred
      except Exception as e:
         logging.info('Exception occured at prediction pipeline')
         raise CustomException(e,sys)
      
      

class CustomData:
   
   def __init__(self,
                age:float,
                education_num:float,
                capital_gain:float,
                hours_per_week:float,
                capital_loss:float,
                workclass:float,
                education:str,
                occupation:str,
                relationship:str,
                race:str,
                sex:str):
   
      self.age = age  
      self.workclass = workclass    
      self.education = education 
      self.education_num = education-num         
      self.occupation= occupation               
      self.race =race  
      self.sex = sex
      self.capital_gain = capital-gain   
      self.capital_loss = capital-loss 
      self.hours_per_week = hours-per-week

   
   
   

   
   def get_data_as_dataframe(self):
      try:
         custom_data_input_dict = {
            'age':[self.age],
            'education_num':[self.education_num],
            'capital_gain':[self.capital_gain],
            'capital_loss':[self.capital_loss],
            'hours_per_week':[self.hours_per_week],
            'workclass':[self.workclass],
            'education':[self.education],
            'occupation':[self.occupation],
            'race':[self.race],
            'sex':[self.sex]

         }

         df = pd.DataFrame(custom_data_input_dict)
         logging.info('Data Frame Gathered')
         return df

      except Exception as e:
         logging.info('Exception occured in prediction pipeline')
         raise CustomException(e,sys)