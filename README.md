# Delete-Temp-Files
This program clears the specified folders in the arguments when files are overdue for a certain amount of time. Only Linux


## Execute
Download the repository
```
git clone https://github.com/slepming/Delete-Temp-Files
```
Run the program 
```
python __init__.py ARGUMENTS(Optionaly)
```


## Arguments
```
options:
  -h, --help            show this help message and exit
  -ep EXPLORER_PATH [EXPLORER_PATH ...], --explorer-path EXPLORER_PATH [EXPLORER_PATH ...]
                        You can specify the folders to be cleared. Default ['$HOME/.cache/', '$HOME/Downloads/']
  -fe FILE_EXCEPTION [FILE_EXCEPTION ...], --file-exception FILE_EXCEPTION [FILE_EXCEPTION ...]
                        You can specify exceptions. Files that cannot be cleared. Default null
  -de DIRECTORY_EXCEPTION [DIRECTORY_EXCEPTION ...], --directory-exception DIRECTORY_EXCEPTION [DIRECTORY_EXCEPTION ...]
                        You can specify exceptions. Directories that cannot be cleared. Default null
  -ar ALLOW_RESPONSE, --allow-response ALLOW_RESPONSE
                        You can disable response. Default True
  -et EXPIRED_TIME, --expired-time EXPIRED_TIME
                        You can set file expiration times. Default 3(days)
  -te TIME_EXECUTION, --time-execution TIME_EXECUTION
                        How many times will the audit be conducted. Default 10800 sec
```
