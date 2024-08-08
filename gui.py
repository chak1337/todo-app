import functions
import functions as f
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

sg.theme('Black')
clock = sg.Text('', key='clock')
label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Type a todo', key='userinput_todo')
add_button = sg.Button('Add',size=10)
list_box = sg.Listbox(f.get_file(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

pre_layout = [[label],
              [input_box, add_button],
              [list_box, edit_button, complete_button],
              [exit_button]]

window = sg.Window('【My to-do App】',
                   layout=pre_layout,
                   font=('Arial', 20))

while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = f.get_file()
            todos.append(values['userinput_todo']+'\n')
            f.write_file(todos)
            window['todos'].update(values=todos)
            window['userinput_todo'].update(value='')
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['userinput_todo'] + '\n'

            todos = f.get_file()
            index_todo = todos.index(todo_to_edit)
            todos[index_todo] = new_todo
            f.write_file(todos)
            window['userinput_todo'].update(value='')
            window['todos'].update(values=todos)
        case 'Complete':
            todo_to_complete = values['todos'][0]
            todos = f.get_file()
            todos.remove(todo_to_complete)
            f.write_file(todos)
            window['todos'].update(values=todos)
            window['userinput_todo'].update(value='')
        case 'Exit':
            break
        case 'todos':
            window['userinput_todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
             break


window.close()

