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
    [sg.Text("This is my Sixth Application")],
    [sg.Text("Name: "), sg.InputText(key="_input1_"),sg.Text("Surname: "), sg.InputText(key="_input2_")],
    [sg.HSeparator()],
    [sg.Text("Please Select the country: "), sg.Combo(dropDown, readonly=True, key="_drop1_",
                                                      default_value=dropDown[0])],
    [sg.Listbox(dropDown, size=(20, 5))],
    [sg.Text("Write the comment below")],
    [sg.Multiline(size=(100,20), key="_editor_" )],
    [sg.HSeparator()],
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
        print("Your message is: ", values["_editor_"])

window.close()