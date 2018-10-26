from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.popup import Popup

import sqlite3

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '400')

Config.write()

conn= sqlite3.connect('users.sqlite')
c = conn.cursor()


Builder.load_string("""
<ScreenOne>:
    BoxLayout:
        orientation:'vertical'
        width:400
        height: 400

        TextInput:
            id:edit_login
            size_hint_y:None 
            height:dp(100) 
            hint_text:"Введите логин"

        TextInput:
            id:edit_password
            size_hint_y:None 
            height:dp(100) 
            hint_text:"Введите пароль"
            password:True

        Button:
            id:enter_button
            size_hint_y: None
            height:dp(100)
            text: "Войти"
            on_press:
                root.manager.transition.direction = "down"
                root.manager.transition.duration = 1
                root.manager.current = "screen_three"
                app.enter(root.ids.edit_login.text, root.ids.edit_password.text)
                

        Button:
            id:registration_button
            size_hint_y: None
            height:dp(100)
            text: "Регистрация"
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 1
                root.manager.current = "screen_two"


<ScreenTwo>:

    BoxLayout:
        orientation:'vertical'
        width:400
        height: 400

        TextInput:
            id:edit_new_login
            size_hint_y:None 
            height:dp(133) 
            hint_text:"Придумайте логин"

        TextInput:
            id:edit_new_password
            size_hint_y:None 
            height:dp(133) 
            hint_text:"Придумайте пароль"
            password:True

        Button:
            size_hint_y: None
            height:dp(132)
            text: "Зарегестрироваться"
            on_press:
                root.manager.transition.direction = "right"
                root.manager.transition.duration = 1
                root.manager.current = "screen_one"
                app.add_new_user(root.ids.edit_new_login.text, root.ids.edit_new_password.text)
""")


class ScreenOne(Screen):
    pass


class ScreenTwo(Screen):
   pass

class ScreenThree(Screen):
    pass


class Authorization(App):

    def build(self):
        screen_manager = ScreenManager()

        screen_manager.add_widget(ScreenOne(name="screen_one"))
        screen_manager.add_widget(ScreenTwo(name="screen_two"))
        screen_manager.add_widget(ScreenThree(name="screen_three"))

        return screen_manager

    def add_new_user(self, login, paswrd):

        c.execute('''INSERT INTO users(login,pswrd) VALUES (?,?)''', (login, paswrd))
        conn.commit()

    def enter(self, log,psw):

        a = c.execute('''SELECT login,pswrd FROM users''')
        print(a)



sample_app = Authorization()
sample_app.run()
conn.close()