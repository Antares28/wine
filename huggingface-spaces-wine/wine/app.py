# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 17:34:34 2023

@author: Antares
"""

import gradio as gr
from PIL import Image
import requests
import hopsworks
import joblib
import pandas as pd
import numpy as np

project = hopsworks.login()
fs = project.get_feature_store()

mr = project.get_model_registry()
model = mr.get_model("wine_model", version=1)
model_dir = model.download()
model = joblib.load(model_dir + "/wine_model.pkl")
print("Model downloaded")

def wine(ttype,fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,ph,sulphates,alcohol):
    print("Calling function")
    if(ttype=="White/0"):
        ttype = int(0)
    else:
        ttype = int(1)
    #df = [ttype],[fixed_acidity],[volatile_acidity],[citric_acid],[residual_sugar],[chlorides],[free_sulfur_dioxide],[total_sulfur_dioxide],[density],[ph],[sulphates],[alcohol]])
    df = pd.DataFrame([[ttype,fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,ph,sulphates,alcohol]], 
                      columns=["type","fixed_acidity","volatile_acidity","citric_acid","residual_sugar","chlorides","free_sulfur_dioxide","total_sulfur_dioxide","density","ph","sulphates","alcohol"])
    print("Predicting")
    print(df)
    # 'res' is a list of predictions returned as the label.
    res = model.predict(df) 
    # We add '[0]' to the result of the transformed 'res', because 'res' is a list, and we only want 
    # the first element.
#     print("Res: {0}").format(res)
    print('res:',res)
    #flower_url = "https://raw.githubusercontent.com/featurestoreorg/serverless-ml-course/main/src/01-module/assets/" + res[0] + ".png"
    #img = Image.open(requests.get(flower_url, stream=True).raw)            
    return res
        
demo = gr.Interface(
    fn=wine,
    title="Wine Quality Predictive Analytics",
    description="Experiment with 12 wine attributes to predict what quality it is.",
    allow_flagging="never",
    inputs=[
        gr.inputs.Radio(["White/0", "Red/1"], label="type"),
        gr.inputs.Number(default=1.0, label="fixed_acidity"),
        gr.inputs.Number(default=1.0, label="volatile_acidity"),
        gr.inputs.Number(default=1.0, label="citric_acid"),
        gr.inputs.Number(default=1.0, label="residual_sugar"),
        gr.inputs.Number(default=1.0, label="chlorides"),
        gr.inputs.Number(default=1.0, label="free_sulfur_dioxide"),
        gr.inputs.Number(default=1.0, label="total_sulfur_dioxide"),
        gr.inputs.Number(default=1.0, label="density"),
        gr.inputs.Number(default=1.0, label="ph"),
        gr.inputs.Number(default=1.0, label="sulphates"),
        gr.inputs.Number(default=1.0, label="alcohol"),
        ],
    
    outputs=gr.Number(label="quality"))

demo.launch(debug=True)

