

import sys

def display_help():
    help_text = """
    Command Line Help Reminder:

    Basic Commands:
    - cd: Change directory
      Example: cd C:\\path\\to\\directory

    - dir: List directory contents
      Example: dir

    - mkdir: Create a new directory
      Example: mkdir new_directory

    - rmdir: Remove a directory
      Example: rmdir directory_to_remove

    - del: Delete files
      Example: del file_to_delete.txt

    File Management:
    - copy: Copy files
      Example: copy source_file.txt destination_file.txt

    - move: Move or rename files
      Example: move file_to_move.txt new_location.txt

    - type: Display file contents
      Example: type file_to_display.txt

    - ren: Rename files
      Example: ren old_name.txt new_name.txt

    System Information:
    - systeminfo: Display system configuration
      Example: systeminfo

    - tasklist: List currently running processes
      Example: tasklist

    - taskkill: Terminate processes
      Example: taskkill /PID 1234

    - ipconfig: Display network configuration
      Example: ipconfig

    File and Directory Permissions:
    - attrib: Change file attributes
      Example: attrib +r file_to_set_readonly.txt

    - icacls: Change file and directory permissions
      Example: icacls file_or_directory /grant User:(F)

    Intermediate Commands and Concepts:
    - set: Display or set environment variables
      Example: set MY_VAR=value

    - setx: Set environment variables permanently
      Example: setx MY_VAR value

    - %VARIABLE%: Access environment variables
      Example: echo %MY_VAR%

    - find, findstr: Search for text in files
      Example: findstr "search_text" file.txt

    - where: Locate files in directories listed in PATH
      Example: where python

    - xcopy: Copy files and directories with more options
      Example: xcopy source_directory destination_directory /E /H

    - robocopy: Robust file copy
      Example: robocopy source_directory destination_directory /MIR

    Advanced Topics:
    - PowerShell: Advanced scripting capabilities
      Example: powershell -Command "Get-Process"

    - WSL: Run Linux distributions on Windows
      Example: wsl ls -l

    - ping, tracert, netstat, nslookup: Networking commands
      Example: ping google.com
      Example: tracert google.com
      Example: netstat -an
      Example: nslookup google.com

    - perfmon: Performance monitoring tool
      Example: perfmon

    - wmic: Windows Management Instrumentation Command-line
      Example: wmic cpu get caption

    - chkdsk: Check and repair disk errors
      Example: chkdsk C: /F

    - cipher: Encrypt and decrypt files
      Example: cipher /E file.txt

    Customization:
    - Customize Command Prompt appearance and behavior
      Example: prompt $P$G

    - Set up aliases and custom commands using doskey
      Example: doskey cls=cls
    """

    print(help_text)

if __name__ == "__main__":
    display_help()