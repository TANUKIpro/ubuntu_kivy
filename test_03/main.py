#!/usr/bin/env python
#-*- coding:utf-8 -*-

import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class TextWidget(Widget):
	pass

class Test2App(App):
	def __init__(self, **kwargs):
		super(Test2App, self).__init__(**kwargs)
		self.title = 'greeting'  #windowsの名前変更
		
if __name__ == '__main__':
	Test2App().run()
