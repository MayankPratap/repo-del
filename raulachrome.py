from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.by import By
from selenium import webdriver
import sys,getpass,requests
from time import sleep
import readline





display=Display(visible=0,size=(800,600))
display.start()

driver=webdriver.Chrome()
url='https://github.com/login'
driver.get(url)
print(driver.title)

#sleep(5)



#print(elems[0].tag_name)
#print(elems[1].tag_name)



while 1:

    username=input('Enter github username: ')
    #email=input('Enter email id: ')
    pswd=getpass.getpass("Enter your password: ")
    emailElem=driver.find_element_by_name('login')
    emailElem.clear()
    emailElem.send_keys(username)

    passElem=driver.find_element_by_name('password')
    passElem.clear()

    passElem.send_keys(pswd)
    submitElem=driver.find_element_by_name('commit')
    submitElem.click()
    #print(driver.current_url)

    if driver.current_url=='https://github.com/':
    	break


url='https://github.com/'+username

tempUrl='https://github.com/'+username+'?tab=repositories';

driver.get(tempUrl)

repoNames=driver.find_elements_by_css_selector('a[itemprop="name codeRepository"]')

length=len(repoNames)

names=[]

for i in range(0,length):
    names.append(str(repoNames[i].text))

for i in range(0,length):
    print(names[i])

# This is the code for autocomplete based on my repositories    

def complete(text,state):
    for name in names:
        if name.startswith(text):
            if not state:
                return name
            else:
                state-=1


readline.parse_and_bind("tab: complete")
readline.set_completer(complete)

repos=[]

while 1:
    repo=input('Repo name to be deleted or (no):')
    if repo=="(no)":
        break
    repos.append(repo)

#print(url)
for i in range(0,len(repos)):

    loopurl=url+'/'+repos[i]
    #print(str(i)+" "+loopurl)
    res=requests.get(loopurl)
    if res.status_code!=200:
        print("No repo named %s exists in your account" % repos[i])
        continue
#print(res.status_code)   
    loopurl=loopurl+'/settings'
    driver.get(loopurl)

    #print("Hola")

#WebDriverWait(browser,10000).until(EC.visibility_of_element_located((By.TAG_NAME,'body')))

    deleteElem=driver.find_element_by_css_selector("button[data-facebox='#delete_repo_confirm']")
    deleteElem.click()



    textElem=driver.find_element_by_css_selector('form[action="/MayankPratap/'+repos[i]+'/settings/delete"] input[type="text"]')

    # This is the hack!!!! to get repo name inside popup  
    # I have executed javaScript.

    driver.execute_script("arguments[0].setAttribute('value','"+repos[i]+"')",textElem)

    """

    if textElem.is_displayed():
        print("Element is displayed")
    else:
        print("Element is not displayed")
    
    if textElem.is_enabled():
        print("Element is enabled")

    #sleep(1)
    """

    try:
        confirmElem=driver.find_element_by_css_selector('form[action="/MayankPratap/'+repos[i]+'/settings/delete"] button[type="submit"]')
        confirmElem.submit()
    except:
        print("!!!!!!!!!!error!!!!!!!!")

    print("Deleted \"%s\" successfully" % repos[i])
    
    


    #driver.switch_to.window(main_window_handle)
    #driver.quit()
    #print("Clicked and submited")


print("All undesired repos deleted succesfully")
sleep(1)
driver.close()