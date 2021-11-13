from kivymd.uix.dialog import MDInputDialog
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from urllib import parse
from kivy.network.urlrequest import UrlRequest

class SearchPopupMenu(MDInputDialog):
	title = "Search By Address"
	text_button_ok = "Search"


	def __init__(self):
		super().__init__()
		self.size_hint = [0.9, 0.3]
		self.events_callback = self.callback()

	def callback(self, *args):
		address = "Potchefstroom"

		for child in self.children:

			for grand_child in child.children:
				if isinstance(grand_child, BoxLayout):
					for kiddie in grand_child.children:
						if isinstance(kiddie, MDTextField):
							print("Address: ", kiddie.text)
				else:
					pass


	def geocode_get_lat_lon(self, address):
		APIkey = ""
		address = parse.quote(address)
		url = f"https://geocoder.ls.hereapi.com/6.2/geocode.json?searchtext={address}&apiKey={APIkey}"
		UrlRequest(url, on_succes=self.success, on_failure=self.failure, on_error=self.error)

	def success(self, urlrequest, result):
		print("Success")
		print(result)

	def failure(self, urlrequest, result):
		print("failure")
		print(result)

	def error(self, urlrequest, result):
		print("error")
		print(result)