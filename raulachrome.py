from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.by import By
from selenium import webdriver
import sys,getpass,requests
from time import sleep



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

#print(url)
repo=input('Enter a repo name: ')
url=url+'/'+repo

res=requests.get(url)

if res.status_code!=200:
    print("No such repo exists in your account")
    sys.exit()
 
#print(res.status_code)   
url=url+'/settings'





#sleep(2)
#driver.back()
driver.get(url)

#WebDriverWait(browser,10000).until(EC.visibility_of_element_located((By.TAG_NAME,'body')))

deleteElem=driver.find_element_by_css_selector("button[data-facebox='#delete_repo_confirm']")
deleteElem.click()
"""
signin_window_handle=None

while not signin_window_handle:
	for handle in driver.window_handles:
		print(handle)
		if handle!=main_window_handle:
			signin_window_handle=handle
			break

print("Hola")

driver.switch_to.window(signin_window_handle)

"""


textElem=driver.find_element_by_css_selector('form[action="/MayankPratap/'+repo+'/settings/delete"] input[type="text"]')
#print(textElem.tag_name)
#print(textElem.get_attribute('type'))
#print(textElem.get_attribute('class'))
#print(textElem.get_attribute('aria-label'))
#print(textElem.location)    
"""if textElem.is_displayed():
    print("Element is displayed.")
else:
    print("Element is not displayed")
"""
# This is the hack!!!! to get repo name inside popup 
# I have executed javaScript.

driver.execute_script("arguments[0].setAttribute('value','"+repo+"')",textElem)

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
    confirmElem=driver.find_element_by_css_selector('form[action="/MayankPratap/'+repo+'/settings/delete"] button[type="submit"]')
    confirmElem.submit()
except:
    print("Some cool error")

print("Deleted % successfully" % repo)
sleep(2)

driver.close()

#driver.switch_to.window(main_window_handle)


#driver.quit()
#print("Clicked and submited")


