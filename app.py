from flask import Flask,render_template, request
import pickle
import numpy as np
import bz2file as bz2

def decompressed_pickle(file):
    data = bz2.BZ2File(file,'rb')
    data = pickle.load(data)
    return data



app = Flask(__name__)
model = decompressed_pickle('file.pbz2')

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
     app.run(debug=True)             

