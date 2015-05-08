#
#
#
#  TODO: README
#
#
#
import os, shutil, sys, re
from glob import glob

def sort_downloads(src, dest, aliases):
    files = []
    for dirName, subdirList, fileList in os.walk(src):
        for a in aliases:
            if a.lower() in dirName.lower():
                files.append([os.path.join(dirName, x) for x in fileList])
                continue
            files.append([os.path.join(dirName, x) for x in fileList if a.lower() in x.lower()])
    print(set([x for sublist in files for x in sublist]))


def sort_by_season(episode_list):
    #TODO: implement
    return


src = input("Enter source folder\n")
dest = input("Enter destination folder\n")
aliases = input("Enter name of show and aliases(optional), separated by ','\n").split(',')

sort_downloads(src, dest, [i.strip() for i in aliases])