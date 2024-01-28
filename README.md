# END TO END MACHINE LEARNING PROJECT

### This proejct is based on the adult census dataset

## Steps 
### Create  environment 
'''
conda create -p venv python==3.8

'''
### Activate environment
'''
conda activate venv/ ---#  "/" is using for involve venv

'''

### install the requirements
'''
pip install -r requirements.txt

'''

### make a setup .py

### Now initialized git and also make a ".gitignore" file
"""
git init

git add .

git commit "first commit"

git branch -M main

git {enter your git link}

git puch -u origin main


"""

### Need to do Data cleaning process

### analysize the data based on statistics ,graphs ets.

## we need to do some machine learing basic step 

### data ingestion :- 
In data ingestion we need to do data into train test split and some basic EDA

### data TRansformation :-
we need  to do all the eda process automatically and create a pipeline and transform that data.
we also convert data into the vector form and create metrics

### model train:-
In model training we need to do the model training based on that data set

## training pipeline:-
training pipeline summarize the previous file into the project

### predcition pipeline :-
prediction pipeline is use for the prediction of the data
 
### model results:-

{'LogisticRegression': 0.8263675476336816, 'Decision Tree': 0.7994263470600287, 'Random Forest': 0.8198115140340094, 'Support vector Machine': 0.8299528785085023, 'KNN': 0.8019872976849006}

============================================================================================
Best Model Found , Model Name : Support vector Machine , Accuracy Score : 0.8299528785085023

====================================================================================

### tamplate :-
we needs to create form.html , index.html,  result.html


## AWS Deployment 

create ".ebextension" folder  and make "python.config" file for the AWS deployment 

written:
option_settings:
  "aws:elasticbeanstalk:container:python":
    WSGIPath : application:application

when want to do other deployment than we delete the aws folder



