from kivymd.app import MDApp
from  farmersmapview import FarmersMapView
from searchpopupmenu import SearchPopupMenu

class MainApp(MDApp):
	search_menu = None

	def on_start(self):
		self.search_menu = SearchPopupMenu()


MainApp().run()