from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
import webbrowser

class MiningApp(App):
    def build(self):
        self.store = JsonStore('user_data.json')
        if not self.store.exists('stats'):
            self.store.put('stats', balance=0.0)
        self.current_balance = self.store.get('stats')['balance']
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.label = Label(text=f'Balance: {self.current_balance:.4f}', font_size='30sp')
        self.btn = Button(text='Boost Mining (Watch Ad)', size_hint=(1, 0.3))
        self.btn.bind(on_release=self.open_ad)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.btn)
        return self.layout

    def open_ad(self, instance):
        webbrowser.open('https://www.profitablecpmratenetwork.com/cck0a153?key=f71a13fe6a65a3e989fc79af71126f32')
        Clock.schedule_once(self.update_points, 15)

    def update_points(self, dt):
        self.current_balance += 0.0005
        self.store.put('stats', balance=self.current_balance)
        self.label.text = f'Balance: {self.current_balance:.4f}'

if __name__ == '__main__':
    MiningApp().run()
