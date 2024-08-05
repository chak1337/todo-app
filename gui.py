import functions as f
import FreeSimpleGUI as sg

label = sg.Text('Type in a to-do')

input_box = sg.InputText(tooltip='Type a todo', key='userinput_todo')
add_button = sg.Button('Add')
list_box = sg.Listbox(f.get_file(), key='todos',
                      enable_events=True, size=[45,10])
edit_button = sg.Button('Edit')

window = sg.Window('【My to-do App】',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button]],
                   font=('Arial', 20))

while True:
    event, value = window.read()
    match event:
        case 'Add':
            todos = f.get_file()
            todos.append(value['userinput_todo']+'\n')
            f.write_file(todos)

            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = value['todos'][0]
            new_todo = value['userinput_todo'] + '\n'

            todos = f.get_file()
            index_todo = todos.index(todo_to_edit)
            todos[index_todo] = new_todo
            f.write_file(todos)

            window['todos'].update(values=todos)
        case 'todos':
            window['userinput_todo'].update(value=value['todos'][0])
        case sg.WIN_CLOSED:
             break


window.close()

