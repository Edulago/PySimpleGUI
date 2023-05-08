import PySimpleGUI as sg

sg.theme('Default') # Add a little color to your windows

layout = [
        [sg.Text('Username')], 
        [sg.InputText(key='Username')],
        [sg.Text('Password')], 
        [sg.InputText(key='Password', password_char='*')],
        [sg.OK(), sg.Cancel()]
        ]

# Create de Window

window = sg.Window('Test', layout=layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        # If user closes window or clicks Cancel, exit the loop
        break
    if event == 'OK':
        username = values['Username']
        password = values['Password']
        if username == 'Admin' and password == 'admin123':
            
            layout2 = [
                [sg.Text("Welcome")],
                [sg.OK()]
            ]

            window2 = sg.Window('Welcome', layout=layout2)
            event2, values2 = window2.read()
            window2.close()

        else: 
            
            error_layout = [    
                [sg.Text('Error')],
                [sg.OK()]
            ]

            error_window = sg.Window('Error', layout=error_layout)
            error_event, error_values = error_window.read()
            error_window.close()

window.close()