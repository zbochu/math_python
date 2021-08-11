import numpy as np
import asyncio
import datetime
import PySimpleGUI as sg

async def loop1(loop):
    while True:
        print('In loop {}'.format(loop.time()))
        await asyncio.sleep(1)

async def display_date(loop, window):
    while True:
        tx = 'Counting {}'.format(datetime.datetime.now())
        print(tx)
        window["-TOUT-"].update(tx)   
        await asyncio.sleep(1)    

async def main(loop, window):
    event, values = window.read()
    print('readng ...', )
    # End program if user closes window or
    # presses the OK button
    if event == "EXIT" or event == sg.WIN_CLOSED:
        exit
    elif event == "OK":
        pass

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # end_time = loop.time() + 5.0

    layout = [ 
            [sg.Text("Counting ...")],
            [sg.Text(size=(40, 1), key="-TOUT-")], 
            [sg.Button("EXIT"), sg.Button("OK")]
        ]

    # Create the window
    window = sg.Window("Demo", layout)

    asyncio.ensure_future(main(loop, window))
    
    asyncio.ensure_future(loop1(loop))
    asyncio.ensure_future(display_date(loop, window))
    
    try:
        loop.run_forever()

    except KeyboardInterrupt:
        print('... stopping from keyboard')
    finally:
        window.close()
        loop.close()
        print('Stopping')
    