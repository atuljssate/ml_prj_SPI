from flask import Flask, request, jsonify, render_template
import os
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler 
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

application = Flask(__name__)
app = application

## Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if  request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':        
        try:
            # Extract data from the request
            # data = request.json
            # reading_score = float(data['reading_score'])
            # writing_score = float(data['writing_score'])
            CustomData_obj = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score'))
            )
            data_df = CustomData_obj.get_data_as_data_frame()
            print("Dataframe Head : ",data_df.head())
            predict_pipeline = PredictPipeline()
            preds = predict_pipeline.predict(features=data_df)  
            return render_template('home.html', results=f' Exam Score: {preds[0]}')        

        except Exception as e:
            return jsonify({'error': str(e)}), 400

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)