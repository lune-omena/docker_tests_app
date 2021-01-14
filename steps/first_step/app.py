# First Step
from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():

    result = "Hello World!"
    
    return result

if __name__ == "__main__":
   server.run(host='0.0.0.0') 
