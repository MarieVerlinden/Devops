# Add to this file for the sample app lab
from flask import Flask
from flask import request
from flask import render_template

#instance of the flask class
sample = Flask(__name__)
@sample.route("/")
def main():
    return render_template("index.html")
    
#make sample run
if __name__ == "__main__":
        sample.run(host="0.0.0.0",port=8080)
