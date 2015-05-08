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
    sorted_list = sort_by_season([x for sublist in files for x in sublist])
    try:
        b = os.path.abspath(os.path.join(dest, aliases[0]))
        print(b)
        os.mkdir(b)
    except:
        pass
    for key in sorted_list:
        try:
            a = os.path.abspath(os.path.join(os.path.join(dest, aliases[0]), key))
            print(a)
            os.mkdir(a)
        except:
            pass
        for x in sorted_list[key]:
            shutil.copy2(x, os.path.abspath(os.path.join(os.path.join(os.path.join(dest, aliases[0]), key), x.split('\\')[-1])))
    return


def sort_by_season(episode_list):
    seasonPattern = re.compile(r's\s?(\d?\d)\s?e\d?\d', re.I)
    seasons = {}
    for x in episode_list:
        if seasonPattern.findall(x):
            s = 'Season ' + ''.join(seasonPattern.findall(x))
            seasons[s] = seasons.get(s, []) + [x]
        else:
            s = 'Season ' + ''.join(seasonPattern.findall(x))
            seasons['Misc'] = seasons.get(s, []) + [x]
    print(seasons)
    return seasons


src = input("Enter source folder\n")
dest = input("Enter destination folder\n")
aliases = input("Enter name of show and aliases(optional), separated by ','\n").split(',')

sort_downloads(src, dest, [i.strip() for i in aliases])