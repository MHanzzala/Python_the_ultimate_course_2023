import PySimpleGUI as sg
import io
import os


scriptPath = os.path.dirname(__file__)
currentSize = 11
currentFont = "Arial"
firstTimeApp = 1
filename = scriptPath


def about():
    sg.popup('About',
             'About this program, version 1.0 Beta, My Text Editor Copyright 2023',
             'Created by: M Hanzala')


def save(data):
    if filename != '':
        with io.open(filename, "w", encoding="utf8") as f:
            f.write(data)


def save_as(data):
    global filename
    filename = sg.tk.filedialog.asksaveasfilename(
        defaultextension='.txt',
        filetypes=(("ALL TXT Files,", "*.txt"), ("All Files", "*.*")),
        initialdir=scriptPath,
        title="Save As")
    if filename != '':
        with io.open(filename, "w", encoding="utf8") as f:
            f.write(data)


def open_file():
    fileopen = sg.popup_get_file('file to open', no_window=True)
    if fileopen != '':
        with open(fileopen, "rt", encoding="utf-8") as f:
            text = f.read()
        window['_text_'].update(value=text)
        window.TKroot.title(fileopen)


menu = [['File', ['Open', 'Save', 'Save as', 'Close']],
        ['Edit', ['Font', ["Arial", "Courier"], ['Size', ["8", "11", "18", "22"]]]],
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
    if event == sg.WIN_CLOSED or event == 'Close':
        print("Editor closed successfully")
        break

    if event == 'Courier':
        currentFont = 'Courier'
        font = ("Courier", currentSize)
        window["_text_"].update(font=font)

    if event == 'Arial':
        currentFont = 'Courier'
        font = ("Arial", currentSize)
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
        if firstTimeApp == 0:
            save(values['_text_'])
            print("File updated successfully")
        else:
            save_as(values['_text_'])
            firstTimeApp = 0
            print("File created successfully")

    if event == 'Save as':
        save_as(values['_text_'])
        print("File created successfully")

    if event == 'Open':
        open_file()


window.close()
