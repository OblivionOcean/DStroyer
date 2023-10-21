import os
import re
import time

"""
Usage:
1. Copy the script to the folder that you would like to scan.
2. Input "y" and the naughty MacOS files will perish.
"""

filenames = []
def fileFinder(filename, rootdir): # https://zhuanlan.zhihu.com/p/547499385
    for fileordir in os.scandir(rootdir):
        if fileordir.is_dir():
            fileFinder(filename, fileordir.path)
        else:
            if filename.find('*') >= 0:
                regularstring = filename
                if filename.rfind(r'.') > 0:
                    regularstring = regularstring.replace(r'.', r'\.')
                regularstring = regularstring.replace('*', r'[\w.]*')
                if re.match(regularstring, fileordir.name):
                    filenames.append(fileordir.path)
                    print(fileordir.path)
            else:
                if fileordir.name == filename:
                    filenames.append(fileordir.path)
                    print(fileordir.path)

if __name__ == '__main__':
    starttime = time.time()
    filenames.clear()
    fileFinder("._*", ".")
    fileFinder(".DS_Store", ".")
    endtime = time.time()
    print(f"Time Cost: {endtime-starttime:.3f}")
    ret = input(f"Are you sure to delete all MacOS .DS_Store/._* files? {len(filenames)}[y/n]")
    if ret == 'y':
        print("Starting deleting:")
        for delfile in filenames:
            try:
                os.remove(delfile)
                print(f"Deleted: {delfile}")
            except Exception as e:
                print(f"Failed: {e}")