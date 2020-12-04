
from geotext import GeoText

# Using Geotext (needs capital letters for city names effective in catching city names)
def test_geotext(sentence):
	places=GeoText(sentence)
	print(places.cities) 
	print(len(places.cities))
	return (len(places.cities))