# AccelToolKit
In this repo you can find a few usefull tools to use when working with accelerometer data processing or other projects.

##concat.py
Concatenates files in a directory containing a certain string in their name omitting their respective (but an initial) header line section of variable length into a single file. <br/>
`python concat.py ID F [-hd [int]] OD` is the usage, where `ID` is the directory, that should be searched for files containing `F`. This does not work recursively and only file directly in `ID` are seen. 
`F` is a continuous string, that is part of the name or extension of the file, allowing filtering for specific files. All other files found, will be ingored. `-hd` takes an integer that defines the number of headerlines each file that should be concatenated has, so that -hd 1 would assume, that the firs file should be copied completely and every consecutive file should be copied from the second line. If -hd is not specified one headerline will be assumed. Only non-negative amounts of lines will have an effect.

## getFileList.py
