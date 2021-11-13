from kivy.garden.mapview import MapMarkerPopup
from kivymd.uix.dialog import MDDialog
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.button import MDFlatButton
from functools import partial
from kivy.properties import ObjectProperty

class MarketMarker(MapMarkerPopup):
	def __init__(self, **kwargs):
		self.content = ObjectProperty()
		self.name = ""
		kwargs.pop("content")
		super(MarketMarker, self).__init__(**kwargs)

	def on_release(self):
		# Open up the location popup menu
		def close(pop, val):
			pop.dismiss()

		close_pop = MDFlatButton(text="CLOSE")
		popup = MDDialog(title=self.name, text='')
		popup.content_cls=self.content
		popup.buttons=[close_pop,]
		close_pop.bind(on_release=partial(close, popup))

		popup.open()