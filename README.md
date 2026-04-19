**Todo App**

**README BY CLAUDE**





**A simple terminal-based task manager that stores tasks in plain-text save files.**



**---**



**## Main Menu**



**Launch the app and type the corresponding letter(s), then press Enter:**



**| Command | Action               |**

**|---------|----------------------|**

**| `A`     | Add task             |**

**| `R`     | Remove task          |**

**| `C`     | Mark task as complete|**

**| `P`     | Print tasks          |**

**| `N`     | New save file        |**

**| `S`     | Save to file         |**

**| `O`     | Open save file       |**

**| `CL`    | Clear all tasks      |**

**| `ST`    | Settings             |**

**| `Q`     | Quit                 |**



**Commands are case-insensitive.**



**---**



**## Task Management**



**### Add Task — `A`**

**Prompts you to type a task, then appends it to the \*\*Tasks\*\* list.**



**### Remove Task — `R`**

**Shows the current \*\*Tasks\*\* list, then prompts for the name of the task to remove. Removal is \*\*case-sensitive\*\* and raises an error if the task is not found.**



**### Mark Task as Complete — `C`**

**Shows the current \*\*Tasks\*\* list, then prompts for the task name. The task is moved from \*\*Tasks\*\* to the \*\*CompletedTasks\*\* list. Raises an error if the task is not found.**



**### Print Tasks — `P`**

**Prints both lists:**

**```**

**Current tasks:   \[...]**

**Completed tasks: \[...]**

**```**



**### Clear All Tasks — `CL`**

**Asks for confirmation (`y/n`). If confirmed, clears \*\*both\*\* the Tasks and CompletedTasks lists. This cannot be undone.**



**---**



**## File Management**



**### Default Save File**

**The default save file is \*\*`My\\\_todos.txt`\*\* (located in the same directory as the script).**



**- It is \*\*not created automatically\*\* — you must create it first using the \*\*New Save File\*\* command or manually.**

**- If the file exists, it is \*\*opened automatically at startup\*\*.**

**- To change the default, either update the `defaultSaveFile` variable directly in the code, or change it in \*\*Settings\*\* and save.**



**Save files store three lines:**

**```**

**\[Tasks list]**

**\[CompletedTasks list]**

**\[Settings list]**

**```**



**### New Save File — `N`**

**Prompts for a filename and creates an empty new file. If a file with that name already exists, an error is shown and no file is overwritten.**



**### Save to File — `S`**

**Prompts for a filename. Leave blank to save to the default save file. Writes the current Tasks, CompletedTasks, and Settings to the file.**



**### Open Save File — `O`**

**Prompts for a filename. Leave blank to open the default save file. Imports Tasks, CompletedTasks, and all settings from the file. Shows an error if the file is not found or is corrupted.**



**---**



**## Settings — `ST`**



**Displays current settings and lets you change them by number:**



**| # | Setting               | Default         |**

**|---|-----------------------|-----------------|**

**| 1 | Default sleep time    | `0.70` seconds  |**

**| 2 | Default save file     | `My\\\_todos.txt`  |**

**| 3 | Debug mode enabled    | `True`          |**

**| 4 | Save settings to file | —               |**



**- \*\*Sleep time\*\* controls the pause between menu prompts.**

**- \*\*Debug mode\*\*, when enabled, allows the hidden `debug` command (see below).**

**- Choosing option \*\*4\*\* saves all current settings (and tasks) to a file.**



**---**



**## Debug Mode**



**When debug mode is enabled, typing `debug` at the main menu loads five sample tasks (`Task 1` through `Task 5`) and marks `Task 2` and `Task 4` as complete — useful for quick testing.**



**---**



**## Notes**



**- \*\*VS Code users:\*\* Set the integrated terminal's working directory to the folder containing the script so that save files are created and found in the right place.**

**- When all tasks are moved to CompletedTasks (after an add, complete, remove, or open action), the app prints: `All tasks completed!`**

**- Save files use Python literal syntax and UTF-8 encoding. Do not edit them manually unless you know what you're doing, as malformed files will cause a load error.**

