from flask import Flask
from flask import render_template, redirect, request
import tensorflow as tf
from tensorflow import keras
import h5py

model = tf.keras.models.load_model('sun.h5')

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST']) 
def home():  
    return render_template('home.html')

@app.route('/result', methods = ['GET', 'POST'])
def predict():
    if request.method == "POST":
       data = []
       lst = []
       Age = request.form.get("Age")
       Subscription_Length_Months = request.form.get("Subscription_Length_Months")
       Monthly_Bill = request.form.get("Monthly_Bill")
       Total_Usage_GB = request.form.get("Total_Usage_GB")
       data.append(int(Age))
       data.append(int(Subscription_Length_Months))
       data.append(int(Monthly_Bill))
       data.append(int(Total_Usage_GB))
       lst.append(data)
       print(lst)
       res = model.predict(lst)
    return render_template('result.html', result = res)

if __name__ == '__main__':  
    app.run(debug = True)