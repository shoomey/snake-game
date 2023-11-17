from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
    
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)

    def go_to_settings(self):
        sm.current = 'settings'

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)

    def go_to_menu(self):
        sm.current= 'menu'

class GameScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('my.kv')

sm = WindowManager()
    
sm.add_widget(MenuScreen(name = 'menu'))
sm.add_widget(GameScreen(name = 'game'))
sm.add_widget(SettingsScreen(name = 'settings'))
    
    
        
class MyApp(App):
    def build(self):
        return sm

kv = Builder.load_file('my.kv')
    
if __name__ == '__main__':
    MyApp().run()