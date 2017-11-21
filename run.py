import os
from flask import Flask, jsonify, request
from app import create_app
app = Flask(__name__)

# config_name = os.getenv('APP_SETTINGS') # 
config_name = "development"
app = create_app(config_name)

@app.route("/")
def main():
    return 'Welcome to Yummyrecipe Api !'


if __name__ == '__main__':
    app.run()



