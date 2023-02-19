import PySimpleGUI as sg

dropDown = ["Pakistan", "SaudiaArab", "Qatar"]
layout = [
    [sg.Text("This is my Third Application")],
    [sg.InputText(key="_input1_")],
    [sg.InputText(key="_input2_")],
    [sg.Combo(dropDown, readonly=True, key="_drop1_",
              default_value=dropDown[0])],

    [sg.Button('Done', key="_done_"), sg.Button('Send', key="_send_")]

]

window = sg.Window("Application", layout,  size=(400, 400))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "_done_":
        print("The window closed successfully")
        break
    if event == "_send_":
        print("Your First Input Was: ", values["_input1_"])
        print("Your Second Input Was: ", values["_input2_"])
        print("Your selected Country is: ", values["_drop1_"])

window.close()
