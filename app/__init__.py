#This file initializes in the application and brings together all of the various components.
import os
from flask import Flask
template_dir = os.path.abspath('../frontend/src')
app = Flask(__name__, template_folder=template_dir)

app.config['SECRET_KEY'] = 'ihopethisissecret'
# Import the application routes
from app import views