import os, shutil, sys, re
from glob import glob
from pprint import pprint

def sort_downloads(src, dest, aliases):
    files = []
    for dirName, subdirList, fileList in os.walk(src):
        for a in aliases:
            if a.lower() in dirName.lower():
                files.append([os.path.join(dirName, x) for x in fileList])
                continue
            files.append([os.path.join(dirName, x) for x in fileList if a.lower() in x.lower()])
    sorted_list = sort_by_season([x for sublist in files for x in sublist])

    # Copying and deleting
    for key in sorted_list:
        if key is not 'Misc':
            try:
                a = os.path.abspath(os.path.join(os.path.join(dest, aliases[0]), key))
                #print(a)
                os.makedirs(a)
                #pprint(sorted_list[key])
            except:
                pass

        for x in sorted_list[key]:
            if key == 'Misc':
                try:
                    shutil.copy2(x, os.path.abspath(os.path.join(dest, aliases[0])))
                    os.remove(os.path.abspath(x))
                except FileNotFoundError:
                    pass
            #print(x)
            try:
                shutil.copy2(x, os.path.abspath(os.path.join(os.path.join(dest, aliases[0]), key)))
                os.remove(os.path.abspath(x))
            except FileNotFoundError:
                pass
            #pprint('tokst að eyða: ---> %s' % os.path.abspath(x))
    #######

    return


def sort_by_season(episode_list):
    seasonPattern1 = re.compile(r's\s?(\d?\d)\s?e\d?\d', re.I)
    seasonPattern2 = re.compile(r'(\d?\d)x\d?\d', re.I)
    seasons = {}
    for x in episode_list:
        if seasonPattern1.findall(x):
            s = 'Season ' + str(int(seasonPattern1.findall(x)[0]))
            seasons[s] = seasons.get(s, []) + [x]
        elif seasonPattern2.findall(x):
            s = 'Season ' + str(int(seasonPattern2.findall(x)[0]))
            seasons[s] = seasons.get(s, []) + [x]
        else:
            seasons['Misc'] = seasons.get('Misc', []) + [x]
    #print(seasons)
    return seasons


src = input("Enter source folder\n")
dest = input("Enter destination folder\n")
aliases = input("Enter name of show and aliases(optional), separated by ','\n").split(',')

sort_downloads(src, dest, [i.strip() for i in aliases])