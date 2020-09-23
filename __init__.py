import sys
from mycroft import MycroftSkill, intent_file_handler
from Adafruit_IO import MQTTClient

ADAFRUIT_IO_KEY = 'aio_zaSA378nNDu9vnMPcq5IpcfBWyNn'
ADAFRUIT_IO_USERNAME = 'Kenzo16'

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.connect()
client.loop_background()


class Lamb2offControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
    @intent_file_handler('lamb2off.control.intent')
    def handle_jarvis_introducing(self, message):
        self.speak_dialog('lamb2off.control')
        client.publish('Lamb2', 0)


def create_skill():
    return FanControl()

