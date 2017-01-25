from flapp import app

BASE_URL = "http://api.openweathermap.org/data/2.5/"
API_KEY = "d4628f26f65cc37ce99e6ae0bf2a2155"
URL_SLUG = "weather"

app.route("/", methods=["POST"])
def home():
	return render_template('weather.html')
	return "hi there ladies"
