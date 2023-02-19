import PySimpleGUI as sg

dropDown = ["Pakistan", "Russia", "Malaysia",
            "Uzbakistan", "Sri Lanka", "Endia"]

menu = [
    ["File", ["Open", "Save", "Save As"]],
    ["Edit", ["Font", "Size"]],
    ["Help", ["About"]]
]

layout = [
    [sg.Menu(menu)],
    [sg.Text("This is my fifth Application")],
    [sg.Text("First Input: "), sg.InputText(key="_input1_")],
    [sg.Text("Second Input: "), sg.InputText(key="_input2_")],
    [sg.Text("Please Select the country: "), sg.Combo(dropDown, readonly=True, key="_drop1_",
                                                      default_value=dropDown[0])],
    [sg.Listbox(dropDown, size=(20, 5))],
    [sg.Multiline(size=(100,20), key="_editor_" )],
    [sg.Button('Done', key="_done_"), sg.Button('Send', key="_send_")]

]

window = sg.Window("Application", layout, resizable=True ,size=(
    800, 600), icon="favicon1.ico")

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