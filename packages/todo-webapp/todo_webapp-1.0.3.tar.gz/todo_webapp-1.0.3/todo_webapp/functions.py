# Funcs to be sued in other modules
FILE_PATH = "todos.txt"


def get_todos(filename=FILE_PATH):
    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# Note: if we use a default parameter, then non-default parameters should be placed before it!
# def write_todos(filepath="todos.txt", todos_arg):
def write_todos(todos_arg, filepath=FILE_PATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# Some time we need some code (functions.py) to be "executed" when it is executed "directly" but not when executed via another code/file like "main.py"
# print(get_todos())
# SO: if we add below condition block, then it will only shows the print content if we direclty run the funtions.py and else nothing will happen!
# print("Text is out of if __name__ block!")

'''>>> print(__name__)
__main__
'''
print(__name__)

if __name__ == "__main__":
    print("HELLO FROM file functions.py ! ")
