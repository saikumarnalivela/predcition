from flask import Flask, jsonify, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    features = [int(x) for x in request.form.values()]
    ## Converting it into array
    final_features = [np.array(features)]
    prediction  = model.predict(final_features)
    return 'salary of the person with age: {} and his salry might be {}'.format(features,prediction)



if __name__ == "__main__":
    app.run(debug= True)