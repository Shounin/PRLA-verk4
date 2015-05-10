import os, shutil, re
 
def sort_downloads(src, dest, aliases):
    files = []
    #Create a list of all files in the source directory
    for dirName, subdirList, fileList in os.walk(src):
        for a in aliases:

            #copies all files in a directory if an alias is in the directory name
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
                os.makedirs(a)
            except:
                pass
 
        for x in sorted_list[key]:
            if key == 'Misc':
                try:
                    shutil.move(x, os.path.join(dest, aliases[0]))
                except:
                    pass
            else:
                try:
                    shutil.move(x, os.path.join(os.path.join(dest, aliases[0]), key))
                except:
                    pass
    #######
    cleanup(src)
 
    return
 
#Returns a dictionary of episodes sorted by seasons.  If no season can be determined, the file is sorted with 'Misc'
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
    return seasons
 
#Deletes unnecessary files and empty folders
def cleanup(src):
    ending = re.compile(r'\.txt|\.torrent|\.dat|\.rar|\.nfo|\.jpg|\.r\d\d|\.sfv$')
   
    for dirName, subdirList, fileList in os.walk(src, topdown=False):
        for name in fileList:
            if ending.findall(name):
                os.remove(os.path.join(dirName, name))
       
        for name in subdirList:
            if not os.listdir(os.path.join(dirName, name)):
                os.rmdir(os.path.join(dirName, name))
               
 
 
##########################################################################################
src = input("Enter source folder\n")
dest = input("Enter destination folder\n")
aliases = input("Enter name of show and aliases(optional), separated by ','\n").split(',')
 
sort_downloads(src, dest, [i.strip() for i in aliases])