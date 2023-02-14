import PySimpleGUI as sg

dropDown = ["USA", "Germany", "France","USA", "Germany", "France"]

menu =[["File",["Open", "Save", "Save As"] ],
       ["Edit", ["Font","Size"]], ["Help", ["About"]] ]

layout =  [ 
    [sg.Menu(menu)],
    [sg.Text("This is my first App" )  ],
    [sg.InputText(key="_input1_")],
    [sg.InputText(key="_input2_")],
    [sg.Combo(dropDown, readonly=True ,key="_drop1_", default_value=dropDown[0])],
    [sg.Listbox(dropDown , size=(20,5))],
    [sg.Button('Done' ,key="_done_" ), sg.Button('Send', key="_send_") ]
    
    ]

window = sg.Window("App", layout,  size=(600,400))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED : 
        break
    if event == "_send_":
        print(values["_input1_"])

window.close()
