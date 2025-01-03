# Create-To-Do-List-----------

'''
##READ and WRITE functions
#NOTE: to not pass filename (eg: todos.txt) from within all blocks, we can set it as default like: fucn(arg="defalult_name")

def get_todos(filename="todos.txt"):
    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

#Note: if we use a default parameter, then non-default parameters should be placed before it!
#def write_todos(filepath="todos.txt", todos_arg):
def write_todos(todos_arg, filepath="todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
'''
#Note: above functions are moved to module : functions.py. So, just import them.

from functions import get_todos, write_todos
import time
print("Hi, today is: ",time.strftime("%b %d,%Y %H:%M:%S"))
print("----------------------------------*")
while True:
    userinput = input("Type add, show, edit or exit:")
    userinput = userinput.strip()

    if userinput.startswith("add"):
        #todo = input("Enter a todo: ") + "\n"
        todo = userinput[4:]

        #todos = get_todos(filename='todos.txt')
        todos = get_todos()
        todos.append(todo + '\n')
        #write_todos(filepath="todos.txt", todos_arg=todos)
                        ###OR####
        #write_todos(filepath="todos.txt", todos_arg=todos)
                        ###OR###
        write_todos(todos)


    elif userinput.startswith("show"):
        #todos = get_todos(filename='todos.txt')
        todos = get_todos()


        # print(todos) # we see that is includes \n . for user frendly view, can use list comprehension (list and loop in one line of code!)
        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.title()  # capitalizes each words first character
            # print(item) with "f" string!
            print(f"{index + 1}-{item}")  # add 1 just to start index nums from  1

    elif userinput.startswith("edit"):
        try:
            #number = int(input('# of todo to edit: '))
            number = int(userinput[5:])
            print(number)

            number = number - 1  # haha, indexing issue!
            # print(existing_todo = todos[number])

            # todos = get_todos(filename='todos.txt')
            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print('Your command is not Valid!')

            #Or just write 'continue' to back to while look again!
            ##userinput = input("Type add, show, edit or exit:")
            ##userinput = userinput.strip()
            continue

    elif userinput.startswith("complete"):
        number = int(input('# of todo to complete: '))

        # todos = get_todos(filename='todos.txt')
        todos = get_todos()

        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(number - 1)

        write_todos(todos)

        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)

    elif userinput.startswith('clear'):
        with open('../../../Mega-Course-Python/pypractices/save-todo.txt', 'r+') as file:
            file.truncate()

    elif userinput.startswith("exit"):
        break
    else:
        print('Invalid Option!')
print("Bye!")
