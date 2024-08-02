FILEPATH = 'todos.txt'
def get_file(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_file(todo_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todo_arg)


