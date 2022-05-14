import boto3
import joblib
import os

s3 = boto3.resource('s3', 'us-east-1')

s3.meta.client.download_file('modelo-credito-mia', 'modelos/pipeline1.joblib' , 'pipeline.joblib')

s3.meta.client.download_file('modelo-credito-mia', 'modelos/model01.joblib' , 'model.joblib')

transformer = joblib.load('pipeline.joblib')

model = joblib.load('model.joblib')

os.remove('pipeline.joblib')

os.remove('model.joblib')

print(model.predict(transformer.transform([['female', 80, 20000, 'free']])))

print(model.predict_proba(transformer.transform([['female', 80, 20000, 'free']])))

