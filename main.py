import functions
import time

now = time.strftime('It is %b %d, %Y %H: %M :%S')
print(now)

while True:
    user_action = input("choose:[add],[show],[edit],[complete],[exit]:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]+'\n'

        todos = functions.get_file()

        todos.append(todo)

        functions.write_file(todos)
    elif user_action.startswith('show'):
        todos = functions.get_file()

        for index, item in enumerate(todos):
            row = f'{index+1}->{item}'
            print(row, end='')
    elif user_action.startswith('edit'):
        try:
            num_to_edit = int(user_action[5:])
            print(num_to_edit)
            num_to_edit -= 1

            todos = functions.get_file()

            new_todo = input("in what todo you want to change to?:")
            todos[num_to_edit] = new_todo + '\n'

            functions.write_file(todos)
        except ValueError:
            print('Your command is not valid,type number you want to edit')
            continue
    elif user_action.startswith('complete'):
        try:
            num_to_complete = int(user_action[9:])
            index = num_to_complete - 1

            todos = functions.get_file('todos.txt')

            todo_has_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_file(todos)

            messege = f'This item: [{todo_has_remove}] is now removed'
            print(messege)
        except IndexError :
            print('We do not have so much items in todo list! try again')
            continue
        except ValueError :
            print('Wrong value!')
            continue
    elif user_action.startswith('exit'):
        todos = functions.get_file()
        print("that is the thing you still need to do today:--> ", todos)
        break
    else:
        print('Command is not valid!')
print("See you next time:)")
