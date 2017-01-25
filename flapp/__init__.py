from flask import Flask, request, render_template
import requests

app = Flask(__name__)
from flapp import weather
