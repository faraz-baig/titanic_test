from flask import Flask, render_template,request
import pickle
import numpy as np

app= Flask(__name__)


svc_model = pickle.load(open('svc_trained_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/predict', methods=['POST'])
def predict():
   
   
   inputs = []
   inputs.append(request.form['sex'])
   inputs.append(request.form['fbs'])    
   inputs.append(request.form['exang'])
   inputs.append(request.form['slope'])
   
   sex = request.form['sex']
   fbs = request.form['fbs'] 
   exang = request.form['exang']
   slope = request.form['slope']
   

   
   
   final_inputs = [np.array(inputs)]
   prediction = svc_model.predict(final_inputs)
   
   if prediction[0] == 1:
        categorical_array = "DISEASED"
   if prediction[0] == 0:
        categorical_array = "NOT DISEASED"
    
   result= categorical_array
   if sex=="1":
       sex = "Male"
   if sex=="0":
       sex = "Female"
       
   if fbs=="0":
       fbs = "NO"
   if fbs=="1":
       fbs = "YES"
   
   if exang=="0":
       exang = "NO"
   if exang=="1":
       exang = "YES"  
       
   if slope=="0":
       slope = "Upsloping"
   if slope=="1":
       slope = "Flat"
   if slope=="2":
       slope = "Downsloping"
       
   return render_template('home.html', prediction_text1=result, sex1 = sex, fbs1=fbs, exang1=exang, slope1=slope)



if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
