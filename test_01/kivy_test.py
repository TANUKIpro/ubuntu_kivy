#!/usr/bin/env python
#-*- coding:utf-8 -*-

import kivy

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
  
	def build(App):
		return Label(text='Hello kivy!')
		
if __name__=='__main__':
	MyApp().run()
