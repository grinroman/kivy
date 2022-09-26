# кнопка и надпись подписываются на события
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


def tst():
    print('KUKU!')


def tst1(event):
    print(event)


class MyApp(App):
    def build(self):
        txt = Label(text='Это надпись')
        btn = Button(text='Это кнопка')
        btn.on_press = tst  # метод btn.on_press совпадает теперь с функцией tst
        # у надписи нет метода on_press, есть on_touch_down
        # (коснулись мышью с зажатой клавишей или пальцем на сенсорном экране):
        txt.on_touch_down = tst1  # метод txt.on_touch_down совпадает теперь с функцией tst1
        # так что эта функция будет вызываться автоматически при нажатии на надпись,
        # и ей будет передаваться дополнительная информация о событии
        layout = BoxLayout()
        layout.add_widget(txt)
        layout.add_widget(btn)
        return layout


MyApp().run()  # проверяйте, что будет печататься при кликах по кнопке и по надписи
