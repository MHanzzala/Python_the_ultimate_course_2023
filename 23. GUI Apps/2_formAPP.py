import PySimpleGUI as sg

layout = [
    [sg.Text("This is my first Application")]

]

window = sg.Window("Application", layout,  size=(400, 400))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
