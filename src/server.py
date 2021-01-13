from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello(**kwargs):

    result = ""
    result += f"kwargs:{kwargs}"

    """ if kwargs['input']:   
        result += kwargs['input'] + str("\n")

    if kwargs['output']:
        result += kwargs['output'] + str("\n")  """

    result += "Hello World!"
    return result

if __name__ == "__main__":
   server.run(host='0.0.0.0') 
