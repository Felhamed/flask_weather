from flask import Flask, request, render_template
import requests

app = Flask(__name__)

BASE_URL = ""
API_KEY = ""
URL_SLUG = ""

app.route("/", methods="POST")
def home():
	pass