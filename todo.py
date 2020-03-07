#!/usr/bin/python3

import sys
import os

todoFile = "todos.txt"


def readTodos():

    # return empty array if the todos file does not yet exist
    if not os.path.isfile(todoFile):
        return []

    f = open(todoFile, "r")  # open the todos file for reading
    lines = f.readlines()  # get each line into an array
    f.close()  # close the file now that we've finished reading it

    # strip every line of leading/trailing whitespace (e.g. newline characters)
    todos = []
    for line in lines:
        todos.append(line.strip())

    return todos


def printTodos():
    todos = readTodos()
    for index in range(len(todos)):
        print(index + 1, "-", todos[index])


# print todos if there is no command
if len(sys.argv) < 2:
    printTodos()
    exit(0)

# execute command
command = sys.argv[1]
if command == "print":
    printTodos()
else:
    print("The command '" + command + "' is not suppported!")
    exit(1)
