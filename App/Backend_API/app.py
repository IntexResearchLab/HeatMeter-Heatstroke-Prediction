import pickle

import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
#create flask app

wbgt_app = Flask(__name__)

#Loading the pickle model

model = pickle.load(open("model.pkl", "rb"))

#working on api

@wbgt_app.route("/predict", methods = ["POST"])

def predict():
    json_ = request.json
    print(request.json)
    query_df = pd.DataFrame(json_, index=[0])
    prediction = model.predict(query_df)
    return jsonify({"Prediction" : list(prediction)})


if __name__ == "__main__":
    print("aise")

    wbgt_app.run(debug=True, host='0.0.0.0', port=5000)

#ws://127.0.0.1:53700/uY61f9oU5sk=/ws
