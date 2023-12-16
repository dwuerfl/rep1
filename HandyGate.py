from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.togglebutton import ToggleButton
import paho.mqtt.client as mqtt

class HandyGate(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.message_callback_add("status", self.on_message_status)
        self.mqtt_client.message_callback_add("abstand", self.on_message_distance)
        self.mqtt_client.connect("192.168.173.63", 1883, 60)
        self.mqtt_client.subscribe("status")
        self.mqtt_client.subscribe("abstand") 
        self.mqtt_client.loop_start()  
        self.automatic_state = False
        self.send_automatic = False  

    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        action_bar = BoxLayout(size_hint_y=None, height=40)
        option_button = Button(text="Optionen")
        option_button.bind(on_press=self.show_options)
        action_bar.add_widget(option_button)
        
        self.status_label = Label(text="Status: ")
        self.data_label = Label(text="Abstand: ")
        self.publish_button1 = Button(text="Öffnen/Schließen", on_press=self.publish_message1)
        
        layout.add_widget(action_bar)
        layout.add_widget(self.status_label)
        layout.add_widget(self.data_label)
        layout.add_widget(self.publish_button1)
        
        return layout
    
    def on_message_status(self, client, userdata, msg):
        if msg.topic == "status":
            received_message = msg.payload.decode()
            print("Empfangene Nachricht:", received_message)
            self.update_status_label(received_message)

    def update_status_label(self, message):
        self.status_label.text = f"Status: {message}"

    def on_message_distance(self, client, userdata, msg):
        if msg.topic == "abstand":
            received_distance = msg.payload.decode()
            print("Empfangene Nachricht:", received_distance)
            self.update_distance_label(received_distance)
    
    def update_distance_label(self, message):
        self.data_label.text = f"Abstand: {message}cm"

    def show_options(self, instance):
        popup_layout = BoxLayout(orientation='vertical')
        automatic_label = Label(text="Automatik:")
        
        toggle_layout = BoxLayout(orientation='horizontal')
        toggle_on = ToggleButton(text="Ein", group='automatic', state='down' if self.automatic_state else 'normal')
        toggle_off = ToggleButton(text="Aus", group='automatic', state='normal' if self.automatic_state else 'down')
        toggle_layout.add_widget(toggle_on)
        toggle_layout.add_widget(toggle_off)
        
        popup_layout.add_widget(automatic_label)
        popup_layout.add_widget(toggle_layout)
        
        popup = Popup(title='Optionen', content=popup_layout, size_hint=(None, None), size=(300, 200))
        popup.open()
        
        toggle_on.bind(on_press=self.start_auto_close)
        toggle_off.bind(on_press=self.stop_auto_close)

    def start_auto_close(self, instance):
        if not self.automatic_state:
            self.mqtt_client.publish("test1", "111")
            self.automatic_state = True
            self.send_automatic = True
    
    def stop_auto_close(self, instance):
        if self.automatic_state:
            self.mqtt_client.publish("test1", "0")
            self.automatic_state = False
            self.send_automatic = False


    def publish_message1(self, instance):
        self.mqtt_client.publish("test1", "10")

   

if __name__ == '__main__':
    HandyGate().run()
