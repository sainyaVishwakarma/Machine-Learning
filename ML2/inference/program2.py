# install required packages
import numpy as np

#flask is a server used to developing rest apis
from flask import Flask,render_template

# create the flask application
app = Flask(__name__)

# add the routes
@app.route('/',methods=['GET'])
def root():
 return render_template('index.html')

# run the app
app.run(host="0.0.0.0", port = 5500,debug=True)