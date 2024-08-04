import functions
import FreeSimpleGUI as sg

label = sg.Text('Type in a to-do')

input_box = sg.InputText(tooltip='Type the fucking todo you motherfucker!',key='todo')
add_button = sg.Button('Add')

window = sg.Window('【My to-do App】',
                   layout=[[label], [input_box, add_button]],
                   font=('Reddit', 20))
while True:
    event, value = window.read()
    print(event)
    print(value['todo'])
    match event:
        case 'Add':
            todos = functions.get_file()
            todos.append(value['todo']+'\n')
            functions.write_file(todos)
        case sg.WIN_CLOSED:
             break



window.close()

