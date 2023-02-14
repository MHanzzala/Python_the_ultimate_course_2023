import PySimpleGUI as sg

layout =  [ 
    [sg.Text("This is my first App" )  ],
    [sg.InputText(key="_input1_")],
     [sg.InputText(key="_input2_")],
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
