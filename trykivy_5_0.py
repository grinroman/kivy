# программа с двумя экранами и одной ошибкой
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class FirstScr(Screen):
    def __init__(self, name):
        super().__init__()  # здесь надо передавать имя. Что будет, если не передать?
        layout = BoxLayout()
        btn = Button(text="Переключиться на другой экран")
        btn.on_press = self.next
        layout.add_widget(btn)
        self.add_widget(layout)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr(name='first'))
        sm.add_widget(Screen(name='second'))
        # можно выбрать текущий экран такой строкой:
        # sm.current = 'second' # пробуйте раскомментировать
        # а вот так работать не будет, нет экрана с таким именем:
        # sm.current = 'first' # пробуйте раскомментировать
        # потому что имя не передано конструктору класса Screen.

        # В остальном первый экран работает - он добавлен в ScreenManager первым,
        # поэтому без переключений по имени экрана нормально показывается в начале работы

        return sm


app = MyApp()
app.run()
