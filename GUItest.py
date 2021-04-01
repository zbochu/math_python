import PySimpleGUI as sg

import time

layout = [ 
    [sg.Text("Hello from PySimpleGUI")],
    [sg.Text(size=(40, 1), key="-TOUT-")], 
    [sg.Button("EXIT"), sg.Button("OK")]
]

# Create the window
window = sg.Window("Demo", layout)

i = 0
isOK = False

# Create an event loop
while True:
    event, values = window.read()
    print('readng ...', )
    # End program if user closes window or
    # presses the OK button
    if event == "EXIT" or event == sg.WIN_CLOSED:
        break
    elif event == "OK":
        for i in range(100):
            window["-TOUT-"].update(i)
            time.sleep(.02)

window.close()