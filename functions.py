def read_file(filepath = 'todo.txt'):
    with open(filepath,'r') as file:
        todos = file.readlines()
    return todos

def write_file(todos, filepath='todo.txt'):
    with open(filepath,'w') as file:
        file.writelines(todos)