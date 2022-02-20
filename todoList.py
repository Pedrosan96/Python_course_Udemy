#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Final exercise, a to-do list and files
"""
class ToDoList:
    def __init__(self, file_name):
        self.file_name=file_name
        self.tasks=self.load_file_into_list()

    def load_file_into_list(self):
        tasks=[]
        with open(self.file_name,'r') as file:
            for task in file:
                tasks.append(task.strip())  #strip is for separete the final caracter
        return tasks

    def list_task(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f'{index}) {task}')

    
    def write_into_file(self):
        with open(self.file_name,'w') as file:
            for task in self.tasks:
                file.write('{}\n'.format(task))

    def add_task(self, task):
        self.tasks.append(task)
        self.write_into_file

    def done_task(self, task_index):
        try:
            del(self.tasks[task_index-1])
            self.write_into_file
        except IndexError:
            print(f'There is no open task with index {task_index}')

def todo_help():
    print()
    print('To-Do List')
    print('* Create new task: [todo TASK]')
    print('* Mark a task as done: [done INDEX]')
    print('* List a task: [list]')
    print('* Quit the program: [quit]')
    print()

def run():
    todolist = ToDoList('todoList.txt')
    todo_help()
    while True:
        cmd_detail=input('Enter cmd: ')
        cmd=cmd_detail.split(' ', 1)[0]
        if cmd == 'list':
            todolist.list_task()
        elif cmd == 'todo':
            task_description=cmd_detail.split(' ',1)[1]
            todolist.add_task(task_description)
        elif cmd=='done':
            task_index=int(cmd_detail.split(' ',1)[1])
            todolist.done_task(task_index)
        elif cmd=='help':
            todo_help()
        elif cmd=='quit':
            break
        else: 
            print('Command not found!')
            todo_help()

if __name__ == "__main__":
    run()

