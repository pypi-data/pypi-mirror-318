import functions
'''
pip install PySimpleGUI
sudo apt-get install python3.10-tk
'''
import PySimpleGUI as sg
import time

#Theme: search google: PySimpleGUI themes
#sg.theme("DarkPurple4")
#sg.theme("LightBlue2")
sg.theme("Black")

clock = sg.Text('', key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")

#Can add simple button or make it more visible!
#add_button = sg.Button("Add", size=5)
add_button = sg.Button(size=5, image_source="add.png", mouseover_colors="LightBlue2", tooltip="Add Todo", key="Add")

list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])  # 45 character, number of rows-high
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button('Exit')

#del_button = sg.Button("Delete")
#window = sg.Window('My To-Do App', layout=[[label], [input_box], [add_button], [del_button]]) # In different rows!, here based on list, 4 rows!
window = sg.Window('My To-Do App',           # In two rows, ...!
                   layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                   font=('Helvetica', 16))

while True:
    event, values = window.read(timeout=200) # check every 10 millisecond
    window["clock"].update(text_color="yellow", value=time.strftime('%b %d, %Y %H:%M:%S'))

    #Bellow will print infos we use withing the code
    #print(1, event)
    #print(2, values)
    #print(3, values['todos'])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)  #to show the todolist after Add in the window

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                #print("Please select an Item first!")
                sg.popup("Please select an Item first!", background_color="green", text_color="yellow", font=("Helvetica",20))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                #print("Please select an Item first!")
                sg.popup("Please select an Item first!", background_color="green", text_color="yellow", font=("Helvetica",20))

        case 'todos':    #to show the text we select to edit, in Input box!
            window['todo'].update(value=values['todos'][0])

        case 'Exit':
            break

        case sg.WIN_CLOSED:   # if we click on close icon, then will no more error happens!
            #exit()
            break



print("Test!")
window.close()

