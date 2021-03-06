"""
Useful_Functions
"""

def filelist(path, ext):
    """creating a list of files with a specific extension"""
    # path is the folder path and ext is the file extension e.g. 'py'.
    from os import listdir
    file = [f for f in listdir(path) if f.endswith(ext)]
    file.sort()
    return file

def folderlist(path):
    """creating a list of folders in a directory"""
    # path is the path of a directory.
    from os import walk
    for (_,folder,_) in walk(path):
        break
    folder.sort()
    return folder
