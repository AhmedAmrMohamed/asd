## What Does What.

### asd/

#####	c2p 
through the current directory looking for `.cbr` files
making them into `.pdf`
PS: `.cbr` is the extension for comic books files

#### cfrate
Uses ```codeforces.com ``` API to get info on a specific contestant in a
round once it's over and notify the user that the info is ready.
The notification behavior can be easily implemented by the user
However; I did implement one -the default -that plays an mp4/mp3 file.

#### ctrlf 
searches from the current directory to all the subs looking for files
and directories that matches a given regex-expression
and list the results.
have the option to look for pattern and ignore another.

#### expo
From the cmd/terminal, opens the current directory into explorer.
saves me a lot of frustration on daily basis ;D

#### joke
The main idea is to use some API to give me some cheesy one-liners
plans to be developed by adding more APIs and further automate the
process to the point where I don't even type any command.

#### opterm
only on windows) `bash asd opterm path` open the cmd w/ in the path directory
just like "expo" this is useless by itself but really useful in other projects

#### org
cause now I'm too lazy to move my files around.
So this searches a directory(and all it's subs) looking for files
which their names contain one or all (depends on ``arg``) from a given
list and move them to ```dest``` folder
run ```bash asd org -h``` for  more info.

randpass :  

since my collage requires me to change the password for my collage-email
every month -I don't give a damn about that email- here goes:
crates a random password every month and save it in a log file.
```bash asd randpass -r``` create a new password and save it
```bash asd randpass -o``` open the log with all saved passwords.

#### sds
(short for: Sort Directories by Size) I always want to sort my folders
by size - windows doesn't allow it-, so now i can type:
``bash asd sds`` in a directory and folders will be sorted by size in non-increasing
order showing the size of each one.
```bash asd sds -r``` reverse the display order.
thinking to turn this into a gui-app with more utility. do you think it will be cool?
Are you even reading this? Have you found my easter egg(s)?

#### CTF

(short for clean them files) directed to organize libraries(mainly songs, movies,...etc) where the same file 
exists under multiple very similar yet different names.
for options run ```bash asd cdtf -h``` 
for more info check the [original ctf repo][https://github.com/theunderd0g/Clean-them-files]

