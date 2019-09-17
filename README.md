the goal of this file to explain what does what.

asd/

    c2p   : goes through the current directory looking for `.cbr` files
            and making them into `.pdf`
            ps: `.cbr` is the extention for comic books files

    cfrate: uses codeforces.com API to get info on a specific contestant in a
            round once it's over and notify the user that the info is ready.
            the notification behaviour can be easily implemented by the user
            However; I did implement one -the default -that plays an mp4/mp3 file.

    ctrlf :searches from the current directory to all the subs looking for files
           and directories that matches a given regex-expression
           and list the results.
           have the option to look for pattern and ignore another.

    expo  :(only on window)when launched from the cmd, opens the current directory
           into explorer.
           saves me a lot of frustration on daily basis ;D

    inst  :
            asd inst -i is a short cut for the command `python stup.py install`
            asd inst -u is a short cut to upload to pypy (still in progress)\

    joke  :the main idea is to use some API to give me some cheesy one-liners
           plans to be devloped by adding more APIs and further automate the
           process to the point where I don't even type any command.

    opterm:(only on windows) `asd opterm path` open the cmd w/ in the path directory
           just like "expo" this is usless by itself but really useful in other projects
    
    org     : cause now i'm too lazy to move my files around.
              so this searches a directory(and all it's subs) looking for files
              which their names contain one or all (depends on arg) from a given
              list and move them to dest folder
              type `asd org -h` for  more info.

    randpass:since my collage requires me to change the password for my collage-email
             every month -I don't give a damn about that email- here goes:
                crates a random password every month and save it in a log file.
                `asd randpass -r` create a new password and save it
                `asd randpass -o` open the log with all saved passwords.
                
    sds     : (short for: Sort Directories by Size) I always want to sort my folders
               by size - windows doesn't allow it-, so now i can type:
               `asd sds` in a directory and folders will be sorted by size in non-increasing
               order showing the size of each one.
               `asd sds -r` reverse the display order.
               thinking to turn this into a gui-app with more uttilty. do you think it will be cool?
               Are you even reading this? Have you found my easter egg(s)?

