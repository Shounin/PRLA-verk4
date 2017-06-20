Assignment in the course 'The Python Programming Language' at Reykjavík University, spring semester 2015.  Written with Soffía Ingibjargar
 
Usage directions:
The script is meant to find all episodes of a particular television show inside a folder and move them to a separate folder, sorted by season.
The user begins by entering the path to a source folder (e.g. "downloads") and then a destination folder (e.g. "shows").  The user then enters the name of a show.
The first entry written in the list of possible names of the show will be the name given to the show's folder in the destination directory.  Then follow a number of possible aliases for the show, separated by a comma(',').
For the show "Top Gear", the entry could look something like this: "Top Gear, top.gear, top_gear".  The search terms are not case sensitive.
The script should then be able to find all episodes of the given show, and store them according to season.  If the script cannot determine a season for some files, those files will be moved to the root folder of the show, and the user could then sort them manually.
One last feature is that the script also runs cleanup, removing all files of types .txt, .torrent, .dat, .rar and more.  Please remember to unrar files after downloading, before running the script

Known bugs and limitations:
On rare occasions, the script will create an empty file with no file extension instead of a folder in the destination folder.  The user just has to delete the file manually and try again, and the script should work.
On even rarer occasions, the script will create such a file, and therefore not move the files, but remove them instead.
The script also does not work for episodes which do not either contain the name of the show in the file name or in the name of their parent directory (such as "That '70s Show" in the example data given).
