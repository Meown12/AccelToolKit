# AccelToolKit
In this repo you can find a few usefull tools to use when working with accelerometer data processing or other projects.

## concat.py
Concatenates files in a directory containing a certain string in their name omitting their respective (but an initial) header line section of variable length into a single file. <br/>
`python concat.py ID F [-hd [int]] OD` is the usage, where `ID` is the directory, that should be searched for files containing `F`. This does not work recursively and only file directly in `ID` are seen. 
`F` is a continuous string, that is part of the name or extension of the file, allowing filtering for specific files. All other files found, will be ingored. `-hd` takes an integer that defines the number of headerlines each file that should be concatenated has, so that -hd 1 would assume, that the firs file should be copied completely and every consecutive file should be copied from the second line. If -hd is not specified one headerline will be assumed. Only non-negative amounts of lines will have an effect.
concat can not be called in any other way than through the command line, it can not be imported into other scripts.

## getFileList.py
Returns a list of files in a directory ID and stores all files found in another file OD. As its main purpose was to create a list of all the biobank accelerometer data it only considers .gz and .csv files.
For this it works in the following way: `python getFileList.py ID OD`, where ID is the directory the files should be found in and OD is the file (absolute or relative path + name +extension) of the output list. The list is equipped with standard `\n` line endings and contains one file (absolute path) per line.

## sortIntoDir.py
With this script Files from a directory A are copied into several directories which are named to a template and have an increasing index at the end. Each of the directories contains at most n files. This script is useful if other scripts dont accept file lists to work with but need a directory of data. To split such data for array jobs for example this script could be used.
`python sortIntoDir.py ID OD n` where ID is the directory the files that need to be split sit in; OD is the path plus a template name e.g. `/path/to/new/directory/dirName` which will create as many directories as needed for the given amount of files, that are named like: `/path/to/new/directory/dirName_0` where 0 will increase for other directories. The number `n` specifies how many files there should be in each directory. All but the last are expected to have this number.
This script can too only be accessed on the command line, although importing it wont harm the importing script.

## splitFileList.py
Allows creating a set of file lists of a directory, that each contain only a certain number of filenames / line lines. It is based on getFileList.py so refer to there if needed. `python splitFileList.py ID OD n` where ID is the path of the directory to list files from. OD is the naming template  which should be a full path like /your/path/to/file/fileName.ext . This will create file lists in files named /your/path/to/file/fileName_0.ext with 0 incrementing once a list is full (automatically starting a new file. n controls the number of files in a list.

