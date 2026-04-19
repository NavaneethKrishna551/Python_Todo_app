# Todo app made by Navaneeth Krishna
# wononav12@gmail.com
# Minimal AI used!
# Save files are made in the same directory as this file when running locally
# When using VS code change the terminal to this files directory



from time import sleep
import ast


Tasks: list = []
CompletedTasks: list = []
inputTask: str = ""
mode: str = "a"
defaultSaveFile: str = "My_todos.txt"
defaultSleepTime: float = 0.70
debugModeEnabled: bool = True
settings: list = [defaultSaveFile, defaultSleepTime, debugModeEnabled]


def addTask(Task: str) -> None:
    Tasks.append(Task)


def newSaveFile(fileName: str) -> None:
    try:
        with open(fileName, "x", encoding="utf-8") as file:
            print(f"File '{fileName}' created successfully.")
    except FileExistsError:
        print("Error! File already exists. Save to that file or rename.")


def saveToSaveFile(saveFileName: str) -> None:
    settings[0] = defaultSaveFile
    settings[1] = defaultSleepTime
    settings[2] = debugModeEnabled
    with open(saveFileName, "w+", encoding="utf-8") as saveFile:
        saveFile.write(f"{Tasks}\n")
        saveFile.write(f"{CompletedTasks}\n")
        saveFile.write(f"{settings}\n")
    print(f"Saved to '{saveFileName}'.")


def openSaveFile(saveFileName: str, TasksVar: list, CompletedTasksVar: list, settingsVar: list) -> None:
    global defaultSaveFile, defaultSleepTime, debugModeEnabled
    try:
        with open(saveFileName, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if len(lines) >= 1:
                TasksVar.clear()
                TasksVar.extend(ast.literal_eval(lines[0].strip()))
            if len(lines) >= 2:
                CompletedTasksVar.clear()
                CompletedTasksVar.extend(ast.literal_eval(lines[1].strip()))
            if len(lines) >= 3:
                settingsVar.clear()
                settingsVar.extend(ast.literal_eval(lines[2].strip()))  
                
                defaultSaveFile    = settingsVar[0]
                defaultSleepTime   = settingsVar[1]
                debugModeEnabled   = settingsVar[2]
        print(f"Opened '{saveFileName}' successfully.")
    except FileNotFoundError:
        print(f"Error: '{saveFileName}' not found. Make new save file or change default!")
    except (ValueError, SyntaxError):
        print("Error: Save file is corrupted or in an unexpected format.")


def completeTask(taskToBeCompleted: str) -> None:
    CompletedTasks.append(taskToBeCompleted)
    Tasks.remove(taskToBeCompleted)


def removeTask(taskToRemove: str) -> None:
    Tasks.remove(taskToRemove)



openSaveFile(defaultSaveFile, Tasks, CompletedTasks, settings)


while mode.lower() != "q":
    sleep(defaultSleepTime)
    mode = input(
        "\nWhat do you want to do?\n"
        "  Add task:               A\n"
        "  Remove task:            R\n"
        "  Mark task as complete:  C\n"
        "  Print current tasks:    P\n"
        "  New save file:          N\n"
        "  Save to file:           S\n"
        "  Open save file:         O\n"
        "  Clear all tasks:        CL\n"
        "  Settings:               ST\n"
        "  Exit:                   Q\n"
        "-> "
    )

    if mode.lower() == "a":
        inputTask = input("Write what task is to be added: ")
        addTask(inputTask)

    elif mode.lower() == "debug" and debugModeEnabled:
        addTask("Task 1")
        addTask("Task 2")
        addTask("Task 3")
        addTask("Task 4")
        addTask("Task 5")
        completeTask("Task 2")
        completeTask("Task 4")
        print("Debug tasks loaded.")

    elif mode.lower() == "p":
        print(f"Current tasks:   {Tasks}")
        print(f"Completed tasks: {CompletedTasks}")

    elif mode.lower() == "r":
        try:
            print(f"Current tasks: {Tasks}")
            taskToRemove = input("Which task do you want to remove (case sensitive):\n> ")
            removeTask(taskToRemove)
            print(f"Remaining tasks: {Tasks}")
        except ValueError:
            print("Task not found in the list.")

    elif mode.lower() == "c":
        try:
            print(f"Current tasks: {Tasks}")
            taskToBeCompleted = input("What task do you want to mark as complete?\n> ")
            completeTask(taskToBeCompleted)
            print(f"Completed tasks so far: {CompletedTasks}")
        except ValueError:
            print("Task not found.")

    elif mode.lower() == "n":
        filename = input("What do you want to name the new file? -> ")
        newSaveFile(fileName=filename)

    elif mode.lower() == "s":
        inputSaveFileName = input("Save file name (leave blank for default): -> ")
        saveToSaveFile(inputSaveFileName if inputSaveFileName else defaultSaveFile)

    elif mode.lower() == "o":
        inputSaveFileName = input("Save file to open (leave blank for default): -> ")
        openSaveFile(
            inputSaveFileName if inputSaveFileName else defaultSaveFile,
            Tasks, CompletedTasks, settings
        )

    elif mode.lower() == "cl":
        confirm = input("Clear ALL tasks? This cannot be undone. (y/n): ")
        if confirm.lower() == "y":
            CompletedTasks.clear()
            Tasks.clear()
            print("All tasks cleared.")

    elif mode.lower() == "st":
        print(
            f"\n  1) Default sleep time    = {defaultSleepTime}"
            f"\n  2) Default save file     = {defaultSaveFile}"
            f"\n  3) Debug mode enabled    = {debugModeEnabled}"
            f"\n  4) Save settings to file"
        )
        try:
            setting = int(input("Type the number of the setting to change -> "))
        except ValueError:
            print("Invalid input, please enter a number.")
            continue

        if setting == 1:
            try:
                defaultSleepTime = float(input(f"New sleep time (currently {defaultSleepTime}): -> "))
            except ValueError:
                print("Invalid input, please enter a number.")

        elif setting == 2:
            defaultSaveFile = input(f"New default save file name (currently {defaultSaveFile}): -> ").strip()

        elif setting == 3:
            raw = input(f"Enable debug mode? (currently {debugModeEnabled}) (true/false): -> ")
            debugModeEnabled = raw.strip().lower() == "true"
            print(f"Debug mode set to {debugModeEnabled}.")


        elif setting == 4:
            settingFileName = input("Save settings to file (leave blank for default): -> ")
            saveToSaveFile(settingFileName if settingFileName else defaultSaveFile)


        else:
            print("Invalid setting number.")


    elif mode.lower() != "q":
        print("Unknown command. Please try again.")


    if mode.lower() in ("a", "c", "r", "debug", "o") and len(Tasks) == 0 and len(CompletedTasks) > 0:
        print("All tasks completed!\n")