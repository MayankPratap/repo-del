# repo-del
An easy repository deleter for github.

I wanted to delete many of my repositories on github which I had created or forked but I was not working on them.  

But Github delete option is too time consuming, boring. Specially if you have many repositories to delete. Isnt it ?? 

So I decided to write a python script which will take all my unwanted repository names through command line and delete them with ease.

The script provides you an autocomplete of your repos. So that you dont have to type whole repository name. In a single run of this script, you can delete many repositories. 


### Works with Python 3. Tested on Ubuntu.

### Steps to run this script

1) Clone this repo.

2) To install dependencies :
   
   ```bash
   sh installer.sh
   ```

3) Now, You are ready to go,
  
   ```bash
   python3 raulachrome.py
   ```
### What after that ?

> Once the script runs it asks for your github username and password. If username passoword is wrong, it will ask you to enter again.  If correct, it lists your current repositories and asks you to enter a repository name. You can enter many repository names one by one. You can access autocomplete by tab here so that you dont have to type whole repository name.

> After you have added names , you can enter "(no)" . Now the script will process each repository name you entered and will delete it.
