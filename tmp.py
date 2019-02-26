from bokeh.events import ButtonClick
from bokeh.models import Button

button = Button()

def callback(event):
    print('Python:Click')
print('in here')
button.on_event(ButtonClick, callback)
