# importing the required libraries
from flask import Flask

# Starting the flask application, giving it any name, usually __main__
app = Flask(__name__)

# app.route means once the server is up and running, this will always be listening on /, waiting for someone to goto ip_addr/
app.route('/')
def init(): # When someone visits /, this function says to run anything in the function
    return 'Hello world'

if __name__ == '__main__':
    app.run()
