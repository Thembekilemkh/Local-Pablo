from kivy.garden.mapview import MapView
from kivy.clock import Clock
from functools import partial
from marketmarker import MarketMarker
from kivymd.uix.list import OneLineListItem
from kivy.uix.boxlayout import BoxLayout
import csv

class Content(BoxLayout):
	def __init__(self, **kwargs):
		self.text = kwargs["text"]
		kwargs.pop("text")
		super(Content, self).__init__(**kwargs)

		self.orientation = "vertical"
		self.spacing = "12dp"
		self.size_hint_y = None
		self.height = "120dp"

		btn = OneLineListItem(text=self.text)
		self.add_widget(btn)

class FarmersMapView(MapView):
	market_names = []
	def __init__(self, **kwargs):
		def zoomie():
			print("Zoom me...")

		super(FarmersMapView, self).__init__(**kwargs)

		
		
		self.on_pan = self.start_getting_markets_in_fov
		self.zoom= 10
		self.lat= -26.208332731093424
		self.lon= 27.656745991698703
		
	
	def start_getting_markets_in_fov(self, **kwargs):
		# After one second get the markets in field of view
		
		BL_lat = kwargs["BL_lat"]
		BL_lon = kwargs["BL_lon"]
		TR_lat = kwargs["TR_lat"]
		TR_lon = kwargs["TR_lon"]

		box_coordinates = {}
		box_coordinates["BL_lat"] = BL_lat
		box_coordinates["BL_lon"] = BL_lon
		box_coordinates["TR_lat"] = TR_lat
		box_coordinates["TR_lon"] = TR_lon

		try:
			self.getting_markets_timer.cancel()
		except:
			pass

		self.getting_markets_timer = Clock.schedule_once(partial(self.get_markets_in_fov, box_coordinates), 1)

	def get_markets_in_fov(self, box, time, **kwargs):
		with open("plugs.csv", 'r') as file:
			reader = csv.reader(file)

			next(reader)

			for market in reader:
				name = market[0]

				if name in self.market_names:
					continue
				else:
					self.add_market(market)
		# Get all the markets in the field of view

		# After getting markets place marker on map

	def add_market(self, market):
		# Create the MarketMarker
		lon = float(market[2])
		lat = float(market[1])
		market_name = market[0]

		my_content = Content(text=market_name)
		marker = MarketMarker(lat=lat, lon=lon, content=my_content)
		marker.name = market_name

		# Add the Marker to the map
		self.add_widget(marker)

		# Keep track of marker name
		self.market_names.append(market_name)




		