#!/usr/bin/python3

import sys
import os

thisScriptDirectory = os.path.dirname(os.path.realpath(__file__))
todoFile = os.path.join(thisScriptDirectory, "todos.txt")  # todos are saved beside the script
tick = "/"  # this character at the start of each todo means that todo is completed

# this function returns True if the todo is completed, otherwise returns False
def isTodoCompleted(todo):
    return len(todo) == 0 or todo[0] == tick


# this function returns the strikethrough version of some text
def strikethrough(completedTodo):
    completedTodo = completedTodo[1:]  # remove the tick character from the beginning
    textWithStrikethrough = ""
    for character in completedTodo:
        textWithStrikethrough += character
        textWithStrikethrough += "\u0336"  # this character makes the previous character print with strikethrough effect
    return textWithStrikethrough


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


def writeTodos(todos):
    # open the file for writing, creating it if it doesn't exist
    f = open(todoFile, "w+")
    # write each todo in a new line
    for todo in todos:
        f.write(todo + "\n")
    f.close()


def printTodos():
    todos = readTodos()
    for index in range(len(todos)):
        todo = todos[index]

        # if the todo is complete then we modify the text so it prints with strikethrough effect
        if isTodoCompleted(todo):
            todo = strikethrough(todo)

        print(index + 1, "-", todo)


def addTodo():
    # check that some text was given to us after the 'add' command
    if len(sys.argv) < 3:
        print("Some text is needed!")
        exit(1)

    # get the todo as a string so we can write it to a new line in the todos file
    args = sys.argv[2:]
    todo = " ".join(args)

    f = open(todoFile, "a+")  # open file for appending, creating it if it doesn't exist
    f.write(todo + "\n")  # write todo to file, last line should always be empty
    f.close()  # close the file now that we've finished writing it


def completeTodo():
    # check that some text was given to us after the 'complete' or 'do' command
    if len(sys.argv) < 3:
        print("Tell us which todo number to complete!")
        exit(1)

    # check that the todo number provided is an integer
    indexToComplete = sys.argv[2]
    if not indexToComplete.isdigit():
        print("Todo number must be an integer!")
        exit(1)

    # convert the string todo number to an integer index
    indexToComplete = int(indexToComplete) - 1

    # get the todos
    todos = readTodos()

    # check that the chosen todo exists
    if indexToComplete >= len(todos) or indexToComplete < 0:
        print("Todo number", indexToComplete + 1, "does not exist!")
        exit(1)

    # check that the chosen todo is not already completed
    if isTodoCompleted(todos[indexToComplete]):
        print("Todo number", indexToComplete + 1, "is already completed!")
        exit(1)

    # complete the chosen todo by placing a tick character at the start
    todos[indexToComplete] = tick + todos[indexToComplete]

    # write the todos to the file, overwriting the old ones
    writeTodos(todos)


def uncompleteTodo():
    # check that some text was given to us after the 'uncomplete' or 'undo' command
    if len(sys.argv) < 3:
        print("Tell us which todo number to uncomplete!")
        exit(1)

    # check that the todo number provided is an integer
    indexToUncomplete = sys.argv[2]
    if not indexToUncomplete.isdigit():
        print("Todo number must be an integer!")
        exit(1)

    # convert the string todo number to an integer index
    indexToUncomplete = int(indexToUncomplete) - 1

    # get the todos
    todos = readTodos()

    # check that the chosen todo exists
    if indexToUncomplete >= len(todos) or indexToUncomplete < 0:
        print("Todo number", indexToUncomplete + 1, "does not exist!")
        exit(1)

    # check that the chosen todo is not already incomplete
    if not isTodoCompleted(todos[indexToUncomplete]):
        print("Todo number", indexToUncomplete + 1, "is already incomplete!")
        exit(1)

    # uncomplete the chosen todo by removing the tick character from the start
    todos[indexToUncomplete] = todos[indexToUncomplete][1:]

    # write the todos to the file, overwriting the old ones
    writeTodos(todos)


def deleteTodo():
    # check that some text was given to us after the 'delete' command
    if len(sys.argv) < 3:
        print("Tell us which todo number to delete!")
        exit(1)

    # check that the todo number provided is an integer
    indexToDelete = sys.argv[2]
    if not indexToDelete.isdigit():
        print("Todo number must be an integer!")
        exit(1)

    # convert the string todo number to an integer index
    indexToDelete = int(indexToDelete) - 1

    # get the todos
    todos = readTodos()

    # check that the chosen todo exists
    if indexToDelete >= len(todos) or indexToDelete < 0:
        print("Todo number", indexToDelete + 1, "does not exist!")
        exit(1)

    # delete the chosen todo by removing it from the todos array
    del todos[indexToDelete]

    # write the todos to the file, overwriting the old ones
    writeTodos(todos)


# print todos if there is no command
if len(sys.argv) < 2:
    printTodos()
    exit(0)

# execute command
command = sys.argv[1]
if command == "print":
    printTodos()
elif command == "add":
    addTodo()
elif command == "complete" or command == "do":
    completeTodo()
elif command == "uncomplete" or command == "undo":
    uncompleteTodo()
elif command == "delete":
    deleteTodo()
else:
    print("The command '" + command + "' is not suppported!")
    exit(1)
