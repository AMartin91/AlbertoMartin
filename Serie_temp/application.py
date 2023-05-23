from flask import Flask
from flask_cors import CORS
import pandas as pd

df = pd.read_csv('tabla_pred_final.csv')

application = Flask(__name__)
CORS(application, origins='http://localhost:5173')

@application.route('/')
def man():
    return df.to_json()

if __name__ == '__main__':
    application.run()


