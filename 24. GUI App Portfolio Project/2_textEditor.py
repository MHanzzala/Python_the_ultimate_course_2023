
import PySimpleGUI as sg

currentSize = 11
currentFont = "Arial"

menu = [['File', ['Open', 'Save', 'Save as', 'Close']],
        ['Edit', ['Font', ["Arial", "Courier", "Time New Roman"],
                  ['Size', ["8", "11", "18", "22"]]]],
        ['About', ['Version']]
        ]

layout = [
    [sg.Menu(menu)],
    [sg.Multiline(size=(600, 400), font=("Arial", 11), key='_text_')]
]


window = sg.Window("My Text Editor", layout, resizable=True,
                   size=(600, 400), icon="favicon.ico")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Courier':
        font = ("Courier", currentSize)
        window["_text_"].update(font=font)

    if event == 'Arial':
        font = ("Arial", currentSize)
        window["_text_"].update(font=font)

    if event == 'Time New Roman':
        font = ("Time New Roman", currentSize)
        window["_text_"].update(font=font)


window.close()
