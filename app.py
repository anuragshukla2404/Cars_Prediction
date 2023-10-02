from flask import Flask,render_template, request
import pickle
import numpy as np


app = Flask(__name__)
model = pickle.load(open('cars_price.pkl','rb'))

@app.route('/')
def home():
         return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features) 
    output = round(prediction[0],2)
    return render_template('home.html', prediction_text='The used car price is: {}'.format(output))                                
      
      
if __name__ == "__main__":
     app.run(host='0.0.0.0', port=8080)             

