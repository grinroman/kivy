# программа с двумя экранами
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
# Экран (объект класса Screen) - это виджет типа "макет" (Screen - наследник класса RelativeLayout).
# ScreenManager - это особый виджет, который делает видимым один из прописанных в нём экранов.


class FirstScr(Screen):
    def __init__(self, name='first'):
        # имя экрана должно передаваться конструктору класса Screen
        super().__init__(name=name)
        btn = Button(text="Переключиться на другой экран")
        btn.on_press = self.next
        # экран - это виджет, на котором могут создаваться все другие (потомки)
        self.add_widget(btn)

    def next(self):
        # объект класса Screen имеет свойство manager
        self.manager.transition.direction = 'right'
        # - это ссылка на родителя
        self.manager.current = 'second'


class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        btn = Button(text="Вернись, вернись!")
        btn.on_press = self.next
        self.add_widget(btn)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'first'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SecondScr())

        sm.add_widget(FirstScr())
        # будет показан FirstScr, потому что он добавлен первым. Это можно поменять вот так:
        # sm.current = 'second'
        return sm


app = MyApp()
app.run()
