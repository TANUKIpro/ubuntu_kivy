#!/usr/bin/env python
#-*- coding:utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class RootWidget(BoxLayout):

	# Kvファイルで定義されている button_include Widget を Pythonファイル内で定義
	button_include = ObjectProperty()
	
	def print_obj(self, obj):
		print(obj)
		
	def chack_button_include(self):
		print(self.button_include)
		
class TestApp(App):
	def build(self):
		return RootWidget()
		
if __name__ == '__main__':
	TestApp().run()
