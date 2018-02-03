#!/usr/bin/env python
#-*- coding:utf-8 -*-

#Hello Worldと表示するだけのプログラム

from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):
	def build(app):
		return Label(text='Hello World')
		
TestApp().run()
