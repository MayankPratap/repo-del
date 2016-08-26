# repo-del
An easy repository deleter for github.

I wanted to delete many of my repositories on github which I had created or forked but I was not working on them.  

But Github delete option is too time consuming, boring. Specially if you have many repositories to delete. Isnt it ?? 

So I decided to write a python script which will take all my unwanted repository names through command line and delete them with ease.

### Works with Python 3. Tested on Ubuntu.

### Steps to run this script

1) First install Google Chrome.

  ```bash
  sudo apt-get install libxss1 libappindicator1 libindicator7
  
  wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  
  sudo dpkg -i google-chrome*.deb
  
  sudo apt-get install -f
  ```
2) Now, let’s install xvfb so we can run Chrome headlessly:

  ```bash
  sudo apt-get install xvfb

  ```
3) Install ChromeDriver:
  
  ```bash
  sudo apt-get install unzip

  wget -N http://chromedriver.storage.googleapis.com/2.20/chromedriver_linux64.zip
  unzip chromedriver_linux64.zip
  chmod +x chromedriver

  sudo mv -f chromedriver /usr/local/share/chromedriver
  sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
  sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
  ```
4) Install some Python dependencies for Selenium:

  ```bash
  sudo apt-get install python3-pip
  pip3 install pyvirtualdisplay selenium
  ```
  
### Now, You are ready to go, clone this repo and run :
   
   ```bash
   python3 raulachrome.py
   ```
