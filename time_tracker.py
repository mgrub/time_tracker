import PySimpleGUI as sg
import pandas
import os
import datetime

# load labels from file
config_file = os.path.join("labels.csv")
df = pandas.read_csv(config_file)

button_kwargs = {"border_width": 0.1, 
                 "size": (20,1),
                 "button_color": ("black","white")}

# put labels into layout
layout = [[sg.Button(row['label_text'], **button_kwargs)] for i, row in df.iterrows()]
layout.append([sg.Button('Done', **button_kwargs)])

# create window
window = sg.Window('Time tracker', layout, background_color='white')

# Event Loop to process "events" and get the "values" of the inputs
while True:

    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break

    report_string = str(datetime.datetime.utcnow()) + ',' + event
    print(report_string)

window.close() 
