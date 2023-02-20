import PySimpleGUI as sg


menu = [
    ['File', ["Open", 'Read', 'Save', 'SaveAs', 'Close']],
    ['Edit', ['Font', ['Arial', 'Corier'], ['Size', ['8', '11', '18', '22']]]],
    ['About', ['Version']]
]

layout = [
    [sg.Menu(menu)],
    [sg.Multiline(size=(600, 400), key='_text_')],
]


window = sg.Window("My Text Editor", layout,  resizable=True,
                   size=(600, 400), icon="favicon.ico")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
