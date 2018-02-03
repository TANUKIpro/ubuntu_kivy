#!/usr/bin/env python
#-*- coding:utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty 

class TextWidget(Widget):
    text = StringProperty()    # プロパティの追加

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = ''

    def buttonClicked(self):        # ボタンをクリック時
        self.text = 'Hello World'


class Test1App(App):
    def __init__(self, **kwargs):
        super(Test1App, self).__init__(**kwargs)
        self.title = 'greeting'

    def build(self):
        return TextWidget()

if __name__ == '__main__':
    Test1App().run()
