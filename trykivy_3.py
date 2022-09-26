from kivy.app import App
from kivy.uix.button import Button # кнопка
from kivy.uix.label import Label # надпись
from kivy.uix.boxlayout import BoxLayout # макет (это тоже виджет!)

class MyApp(App):
   def build(self):
      # при создании виджета можно задать значения его свойств.
      # Конструкторы виджетов принимают только именованные параметры!
      txt = Label(text='Это надпись') 
      btn = Button(text='Это кнопка')
      layout = BoxLayout()
      layout.add_widget(txt)
      layout.add_widget(btn)
      return layout # возвращается виджет, который 
                     # управляет расположением своих потомков - кнопки и надписи

MyApp().run()