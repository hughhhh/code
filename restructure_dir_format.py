"""
Moving all files in a directory to a specific format
Below i'm taking all files in this directory and moving them into filename/current/filename.csv
https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
for file in dir:
  new_dir = file.name/current/
  mkdir new_dir
  cp file.name new_dir
"""
import os
for filename in os.listdir():
    try:
        print(filename)
        namespace = filename.split('.')[0]
        path = f'{namespace}/current'
        os.makedirs(path)
        os.rename(f'{filename}', f'{path}/{filename}')
    except FileExistsError:
        continue
