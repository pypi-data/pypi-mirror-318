[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![PyPI version](https://badge.fury.io/py/controller-companion.svg)](https://pypi.org/project/controller-companion/)

# Controller Companion

Easily map controller shortcuts to an action.
The following actions are supported:
- Kill a task by its name.
- Execute a keyboard shortcut.
- Execute an arbitrary console command.

## Features
- GUI and CLI options available
- Supports a wide variety of controllers (those supported by [pygame](https://www.pygame.org))
- Runs on Windows, Linux and Mac
- Auto start on system boot (windows only for now)
- GUI app can be compiled as a standalone executable (using [PyInstaller](https://pyinstaller.org))

## Screenshots
### Main Window
![demo](https://raw.githubusercontent.com/Johannes11833/controller-companion/master/demo/app.png)
### Create a new shortcut 
![demo](https://raw.githubusercontent.com/Johannes11833/controller-companion/master/demo/add_new_shortcut.png)


## How to Install
- Using pip:
    ```console
    pip install controller-companion
    ```
- For the GUI version, executables are additionally available [here](https://github.com/Johannes11833/controller-companion/releases) for Windows, Mac and Linux. In addition for windows, an installer is available.

## How to run
- CLI and GUI versions available
- CLI:
    - Multiple mappings can be created.
    - One or multiple input controller key combination that triggers an action can be defined using --input. The keys of one individual input combination are separated by commas, while each distinct input combination is separated by a space. 
    - One or multiple actions can be defined using either `--task-kill`, `--console` or `--shortcut`. These actions will be mapped to the previously defined controller `--input` key combinations in the order `--task-kill`, `--console` and finally `--shortcut`
    - Example with 2 mappings: 
        ```console
        controller_companion --input A,B Back,Left --console explorer.exe --shortcut alt+f4
        ```
        will result in the following mapping:
        ```console
        Controller<A,B> --> Action<name: Run command "explorer.exe", target: explorer.exe, type: CONSOLE_COMMAND>
        Controller<Back,Left> --> Action<name: Shortcut "alt+f4", target: alt+f4, type: KEYBOARD_SHORTCUT>
        ```

    - Run `controller_companion --help` to see all available arguments

## Build Executable
With [poetry](https://python-poetry.org/) installed, run the following command to build the executable using [PyInstaller](https://pyinstaller.org):
```console 
poetry run build_controller_companion_executable
```

## Credits
- Gamepad button icons: https://80.lv/articles/free-button-icons-for-unreal-engine-and-unity