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



if __name__ == "__main__":
    todolist = ToDoList('todoList.txt')
    print('Before adding a task')
    todolist.list_task()
    todolist.add_task('Buy a gamer chair')
    print('After adding a task')
    todolist.list_task()

