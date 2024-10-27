import os
from pathlib import Path
from datetime import datetime, timedelta
import notify2
import time
import shutil
import argparse

defaultDirectoryPaths: list = ['%s/.cache/' % Path.home(), '%s/Downloads/' % Path.home()]
file_exceptions = []
directory_exceptions = []
expired_time = 3

def datatime_sort(file: Path):
    file_info = file.stat()
    if datetime.now() > datetime.fromtimestamp(file_info.st_ctime) + timedelta(days=expired_time):
        print('%s expired' % file.name)
        return file
    print('%s is ok, is date, will expire on %s' % (file.name, datetime.fromtimestamp(file_info.st_ctime) + timedelta(days=3)))
    return 
def get_files_in_directories(directories: list) -> list:
    files = []
    for paths in directories:
        if paths in directory_exceptions:
            print('Path %s in exception' % paths)
            continue
        path = Path(paths)
        if path.name in directory_exceptions:
            print('Directory name %s in exception' % path.name)
            continue
        for file in path.glob('*'):
            if file in file_exceptions: 
                print('File %s in exception' % file)
                continue
            if file.name in file_exceptions:
                print('File name %s in exception' % file.name)
                continue
            print('Append %s' % file)
            files.append(datatime_sort(file))
    return files

def send_notification(title: str, body: str):
    notify2.init("DelTempFiles")
    notification = notify2.Notification(title, body) 
    notification.show()

if __name__ == "__main__":
    response_bool = True
    parser = argparse.ArgumentParser(description="Custom args")
    parser.add_argument('-ep', '--explorer-path',nargs='+',type=str, help='You can specify the folders to be cleared. Default %s' % defaultDirectoryPaths)
    parser.add_argument('-fe', '--file-exception', nargs='+', type=str, help='You can specify exceptions. Files that cannot be cleared. Default null')
    parser.add_argument('-de', '--directory-exception', nargs='+', type=str, help='You can specify exceptions. Directories that cannot be cleared. Default null')
    parser.add_argument('-ar', '--allow-response', type=bool, help="You can disable response. Default True")
    parser.add_argument('-e', '-expired', type=int, help="You can set file expiration times. Default 3(days)")
    args = parser.parse_args()
    if args.explorer_path:
        defaultDirectoryPaths.clear()
        for paths in args.explorer_path:
            defaultDirectoryPaths.append(paths)
    if args.file_exception:
        for exception in args.file_exception:
            file_exceptions.append(exception)
    if args.directory_exception:
        for exception in args.directory_exception:
            directory_exceptions.append(exception)
    if args.allow_response:
        response_bool = args.allow_response
    if args.expired:
        expired_time = args.expired
            
    if len(defaultDirectoryPaths) == 0: 
        raise ValueError("%s equal null, please create list dictionaries" % defaultDirectoryPaths)
    print("Done check files from 'paths'")
    last_check = datetime.now()

    while True:
        last_check = datetime.now()
        send_notification("Report", "At %s the file review began: %s" % (last_check, defaultDirectoryPaths))
        print(defaultDirectoryPaths)
        files = get_files_in_directories(defaultDirectoryPaths)
        print(files)
        expired_files:list = []
        for file in files:
            if file == None: continue
            expired_files.append(file)
            if response_bool: 
                response = input("You want delete this file? (Default: Y). Allowed replies: Y - Yes, N - no, YA - yes all: ")
                match(response):
                    case 'N' | 'n': continue
                    case 'Y' | 'y': 
                        if Path.is_dir(file):
                            shutil.rmtree(file)
                        else: os.remove(file)
                    case 'YA' | 'ya': 
                        response_bool = False
                    case _:
                        if Path.is_dir(file):
                            shutil.rmtree(file)
                        else: os.remove(file)
            else:
                if(Path.is_dir(file)):
                   shutil.rmtree(file)
                else:
                   os.remove(file)
            print('file checked: %s' % file)
        time.sleep(2)
        send_notification("Report", "Check successful, %s files cleared" % len(expired_files))
        time.sleep(10800)




