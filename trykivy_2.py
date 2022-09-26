# приложение с одним виджетом.

from kivy.app import App
# все виджеты находятся в отдельных модулях внутри kivy.uix:
from kivy.uix.button import Button # кнопка

class MyApp(App):
   # если в объекте класса App есть метод build(),
   # то run() выполнит этот метод 
   # и выведет на экран то, что возвращает build
   def build(self):
      btn = Button(text='Это кнопка')
      return btn # возвращается всегда виджет!

app = MyApp()
app.run() # будет показан виджет класса Button

