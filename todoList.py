#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Final exercise, a to-do list and files
"""
def readFile():
    """
    file = open('todoList.txt','r')
    file.seek(0)
    for index, line in enumerate(file, start=1):
    print('{}) {}'.format(index, line), end='')
    file.close()
    """
    with open('todoList.txt','r') as file:      #Opening the file this way there
        for index, line in enumerate(file, start=1):    #is no need to close the file
            print(f'{index}) {line}', end='')

def append_into_file(task):
    with open('todoList.txt','a') as file:  #'a' is for append mode
        file.write(task)


if __name__ == "__main__":
    readFile()

