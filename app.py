
from flask import Flask, render_template,request
import pickle
import numpy as np
#from sklearn.ensemble.forest import RandomForestClassifier

app= Flask(__name__)


svc_model = pickle.load(open('svc_trained_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/predict', methods=['POST'])
def predict():
   
   
   inputs = []
   inputs.append(request.form['pclass'])
   inputs.append(request.form['gender'])    
   inputs.append(request.form['siblings'])
   inputs.append(request.form['embarked'])
   
   class1 = request.form['pclass']
   gender = request.form['gender'] 
   siblings = request.form['siblings']
   embarked = request.form['embarked']
   

   
   
   final_inputs = [np.array(inputs)]
   prediction = svc_model.predict(final_inputs)
    #unseen_feature_vectors = request.form.values()
   
   if prediction[0] == 1:
        categorical_array = "Survived"
   if prediction[0] == 0:
        categorical_array = "Not Survived"
    
   result= categorical_array
   if class1=="1":
       class1 = "First Class"
   if class1=="2":
       class1 = "Second Class"
   if class1=="3":
       class1 = "Third Class"
       
   if gender=="0":
       gender = "Female"
   if gender=="1":
       gender = "Male"
     
   if siblings=="1":
       siblings = "One"
   if siblings=="2":
       siblings = "Two"
   if siblings=="3":
       siblings = "Three"
       
   if embarked=="0":
       embarked = "Cherbourg"
   if embarked=="1":
       embarked = "Queenstown"
   if embarked=="2":
       embarked = "Southampton"
       
   return render_template('Home.html', prediction_text1=result, class11 = class1, gender1=gender, siblings1=siblings, embarked1=embarked)



if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)