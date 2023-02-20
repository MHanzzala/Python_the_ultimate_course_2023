import PySimpleGUI as sg
import io


currentSize = 11
currentFont = "Courier"


def about():
    sg.popup('about','About this program, version 1.0 Beta, My Text Editor Copyright 2023')


def save(data):
    with io.open("data.txt", "w", encoding="utf8") as f:
        f.write(data)


menu = [['File', ['Open', 'Save', 'Save as', 'Close']],
        ['Edit', ['Font', ["Arial", "Courier", "Time New Roman"], ['Size', ["8", "11", "18", "22"]]]],
        ['About', ['Version']]
        ]

layout = [
    [sg.Menu(menu)],
    [sg.Multiline(size=(600, 400), font=("Courier", 11), key='_text_')]
]


window = sg.Window("My Text Editor", layout, resizable=True,
                   size=(600, 400), icon="favicon.ico")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close':
        print("Text Editor closed successfully")
        break

    if event == 'Courier':
        currentFont = 'Courier'
        font = ("Courier", currentSize)
        window["_text_"].update(font=font)

    if event == 'Arial':
        currentFont = 'Courier'
        font = ("Arial", currentSize)
        window["_text_"].update(font=font)
    
    if event == 'Time New Roman':
        currentFont = 'Courier'
        font = ("Time New Roman", currentSize)
        window["_text_"].update(font=font)

    if event == '8':
        currentSize = '8'
        font = (currentFont, '8')
        window["_text_"].update(font=font)

    if event == '11':
        currentSize = '11'
        font = (currentFont, '11')
        window["_text_"].update(font=font)

    if event == '18':
        currentSize = '18'
        font = (currentFont, '18')
        window["_text_"].update(font=font)

    if event == '22':
        currentSize = '22'
        font = (currentFont, '22')
        window["_text_"].update(font=font)

    if event == 'Version':
        about()

    if event == 'Save':
        save(values['_text_'])
        print("text file created successfully")

window.close()
