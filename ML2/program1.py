# import required packages
import numpy as np
import pickle

# load the model using pickle

with open("./model.pkl","rb") as file:
 model = pickle.load(file)


#get the SAT_score input from user
sat_score = float(input("enter your SAT score: "))

#inference the model
gpa = model.predict([[sat_score]])
print(f"your gpa will be : {gpa[0]:.2f}")