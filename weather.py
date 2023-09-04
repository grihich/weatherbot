from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps



def get_temperature_at_place(place):
	api_key = '4aa1a8ce74cd71a59cca5daf1deaab9e'
	owm = OWM(api_key)
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(place + ",RU")
	w = observation.weather
	temperature_in_choosed_place = round(w.temperature('celsius')['temp'])
	return temperature_in_choosed_place



