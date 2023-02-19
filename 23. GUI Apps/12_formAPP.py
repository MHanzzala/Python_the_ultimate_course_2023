import PySimpleGUI as sg

dropDown = ["Pakistan", "Russia", "Malaysia",
            "Uzbakistan", "Sri Lanka", "Endia"]

menu = [
    ["File", ["Open", "Save", "Save As"]],
    ["Edit", ["Font", "Size"]],
    ["Help", ["About"]]
]

col1 = [
    [sg.Text("This is my Seventh Application")],
    [sg.Text("name")],
    [sg.InputText(key="_input1_")],
    [sg.Text("surname")],
    [sg.InputText(key="_input2_")],
]

col2 = [[sg.Combo(dropDown, readonly=True, key="_drop1_", default_value=dropDown[0])],
        [sg.Listbox(dropDown, size=(20, 5))],
        [sg.Button('Done', key="_done_"), sg.Button('Send', key="_send_")],
        ]

layout = [[sg.Menu(menu)],
          [sg.Column(col1), sg.VSeparator(), sg.Column(col2)],
          [sg.Text("Write the comment below")],
          [sg.Multiline(size=(100, 20), key="_editor_")],
          ]

window = sg.Window("Application", layout, resizable=True,
                   size=(800, 600), icon="favicon.ico")

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
