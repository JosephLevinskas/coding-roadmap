#DVCS - distributed version control system
A server has a copy of all the files and change history
Then each file checkout on a local computer also gets the full history this way all the data isn't in one place
This is what git is

#GIT
Git takes snapshots of changed and references files that didn't change instead of fully copying each time
this makes it like a mini file system
You have the entire history of the project on your device so it is very quick
Everything in GIT is check summed 
Uses hashing to look up files 
Committed means the data is safely stored on your device
Modified means you have changed a file but not committed it yet
Staged means you have marked a current changed file to be committed on the next commit 
The git directory is where git stores the metadata and object database for the project
This is what is copied when you clone a repository 
The working directory is a single checkout of one version of the project
can use git config to change setting of git
git config --global user.name "" - sets name
git config --global user.email "" - sets email
git config --list - to show all settings
