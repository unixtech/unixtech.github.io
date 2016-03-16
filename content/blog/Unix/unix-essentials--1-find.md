Title: Unix essentials-1 Find
Date: 2010-1-03 18:02
Category: Unix    
Tags: Unix, Essentials
Slug: practical-find
Authors: Unixer
Status: Published
Summary: Everyday usage of `find` utility


The `Find` utility in Linux is very useful in the sense that it quickly locates and searches through list of files and directories.
It can do so based on condition that you pass through arguments. 
`Find` can find files using different conditions like:  

 * Permissions
 * Users
 * Groups
 * File type
 * Date
 * Size and more.

## Basic Usage
- Find file in current directory
    
```bash
 # Find by filename in Current dir
 find . -name unixtech.txt

 #Output
 ./unixtech.txt
```

- Find file in current directory <span class="fa fa-arrow-right"></span> Case insensitive
    
```bash
 # Find by filename in Current dir
 find . -iname unixtech.txt

 #Output
 ./unixtech.txt
```

- Recursively searching file in all in whole system
```bash
# Recurse through whole file system
find / -name $FILENAME
```

## Find files based on permissions 

- Find files certain permissions
```bash 
# Find only files with full 777 permissions
find / -perm 0777 -print
# Find files with SGID bit set 
find / -perm 2644
# Or
find / -perm /g+s
```

- Find all files based on user permissions
```bash 
#Find all files with READ permission
find / -perm /u=r -print

# Find all files with executable bit set
find / -perm /a=x -print
```

> **Note:** Find can also execute command on found files based on given criterion.
> In addition to just printing list of files, You can modify, change permission and also delete files using `-exec` flag in find command.

So, If you want to change all the files that have permission set to `777` to something that only you can modify in your home directory, You may execute following variation of `find`

- Find all files with `777` permission and change it to `644` inside your home directory
```bash
#Find and exec 
find ~USERNAME -perm 777 -print -exec chmod 644 {} \;
```

|  |                                                                |
| :---:      | :---                                                                    |
| \{\}   | Shell expander which will put current file name from list in `-exec`|
| \;     | '\' is Shell escape and ';' is Unix chaining symbol                |


> **Note:** Here thing to remember is You have to put \{\} symbol where you want INPUT filename to be, and chain it with \; symbol.

- Same thing if you want to remove or list files
```bash
#List files that matches certain crieteria
find / -perm 777 -print -exec ls -la {} \;

#Removing files that matches certain crieteria
find / -perm 777 -print -exec rm -rf {} \;
```

## Finding files based on user/group ownership
```bash
#Find files owned by particular user
find / -user unixtech -print

#Find files owned by group
find / -group unixgroup -print

```


## Finding files based on modification/changed/accessed date time

- Find files modified 3 days back
```bash 

find / -mtime 3

```

- find all the files those are changed last hour
```bash
#Will return all the files changed in last 60 mins
find / -cmin -60
```

> **Note:** '-' sign in front of 60 includes all the files that changed within that timeframe, Ex. It will include files that are changed 3, 5, 10 mins back and so on.
> Notice different criterion for finding files such as `-mmin`, `cmin`, `amin`


|         |          |   
| ------------- |:-------------:|
|   Access time      | If you list/delete/open this file then `atime` will be modified          |   
|   Changed time      | Modifying data of the file changes `ctime` parameter of file |   
|   Modification time      | Same as Changed time but will also be changed upon changes in meta data of the file. |   


## Use `find` to search files based on size

This one is quite useful in case you want to find largest files in your home directory, files that are eating away space on hard drive. 

- Find all the  files between 10 MB - 100 MB

```bash
find /home -size +10M -size -100M
```

- Find all the files larger then 1GB and delete em

```bash
#Find larger files and list them first
find /home -size +1G -exec ls -la {} \;

# If you see desired files then remove them
find /home -size +1G -exec rm -rf {} \;

```

- Find all the movie files larger then 100MB and delete 
```bash
# Find and list files first
find /home -size +100M -print -iname "*mp4|wmv|mov";

# After listing them just press `UP` arrow, change the CMD and  delete 
find /home -size +100M -iname "*mp4|wmv|mov" -exec rm -rf {} \;
#Be careful while executing that command.
```

> **Note:** Find supports extended regular expressions too.   
>Regular expressions are swiss army knife for solving many kind of problem but they also come with added difficulty of maintaining and generating them. If none> of the above meets your requirement then as last resort only you should use Re>gExes in `find` utility.


