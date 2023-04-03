#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service

#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pathlib import Path
import time
import subprocess
import re
import undetected_chromedriver as webdriver


#global variables
driver = None

#logic
#start a loop
    #func like
    #func new message
    #func reply

#func like
    #get image
    #query chatgpt
    #analyze response
    #like or dislike
    #check if max likes reached and clear error

#func new message
    #check if any new people appeared 
    #copy previous conversation
    #query chatgpt 
    #send message

#func reply
    #check if any people replied 
    #copy previous conversation
    #query chatgpt 
    #send message
    
def openai(question):
    global driver
    

    #try:
    #    time.sleep(2)   
    #    login_button = driver.find_element(By.XPATH, '//div[text()="Log in"]')
    #    login_button.click() 
    #    time.sleep(5)   
    #    google_button = driver.find_element(By.XPATH, '/html/body/div/main/section/div/div/div/div[3]/form[2]/button')
    #    google_button.click()
    #except:
    #    pass


    driver.switch_to.window(driver.window_handles[1])
    try:
        # wait for the page to load
        #time.sleep(4)   
        chatbox = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/main/div[2]/form/div/div[2]/textarea')
        chatbox.send_keys(question)
        time.sleep(2)   
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/main/div[2]/form/div/div[2]/button')
        button.click()
        time.sleep(5)
        reply = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/main/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/p')
        #output = reply.get_attribute('style')
        new_chat_btn = driver.find_element(By.XPATH, '//a[text()="New chat"]')
        new_chat_btn.click()
        time.sleep(0.5)

        driver.switch_to.window(driver.window_handles[0])
        return reply.text
    except:
        driver.switch_to.window(driver.window_handles[0])
        return ''

def init():
    global driver
    subprocess.run("taskkill /f /im chrome.exe")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.use_chromium = True  
    chrome_options.add_argument('--disable-popup-blocking')  


    chrome_options.user_data_dir=str(Path.home())+"\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"

    driver = webdriver.Chrome(options = chrome_options, use_subprocess=True)

def load():
    global driver
    # navigate to the Tinder website
    driver.get("https://tinder.com")

    #while True: 
    #get rid of unnecessary prompts
    #try:
    #    #driver.switch_to.window(driver.window_handles[1])
    #    facebook_button = driver.find_element(By.XPATH, '//span[text()="Maybe Later"]')
    #    facebook_button.click()
    #    #break 
    #except:
    #    pass

    #load ChatGPT
    # Open a new window
    driver.execute_script("window.open('');")
    # Switch to the new window
    driver.switch_to.window(driver.window_handles[1])
    # navigate to the Tinder website
    driver.get("https://chat.openai.com/chat")

    
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[2])
    driver.get('https://am2.co/wp-content/uploads/CloseWindow.png')

    while (len(driver.window_handles) > 2):
        time.sleep(2)
        if(len(driver.window_handles) == 0):
            quit()
    driver.switch_to.window(driver.window_handles[0])

def like():
    global driver
    #get the image of the first photo
    driver.switch_to.window(driver.window_handles[0])
    url_next_match = None
    time.sleep(1)
    while True:
        try:    
            image = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/span[1]/div')
            gl_url = image.get_attribute('style')
            print(gl_url)
            url_pattern = re.compile('url\("(.+?)"\)')
            matches = url_pattern.findall(gl_url)
            if matches:
                url_next_match = matches[0]
                #answer = openai('is this person young? ' + url_next_match)

                # like the first match on the screen 
                
                #like_button = driver.find_element(By.XPATH, '//button[class()="background-like"]')
                #like_button = driver.find_element_by_css_selector("button[class*='Bgi($g-ds-background-like):a']")
                #like_button = driver.find_element(By.XPATH, '//*/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button')
                #/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button
                for i in range(1,6):
                    try:
                        element = '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[' + str(i) +']/div/div[4]/button'
                        like_button = driver.find_element(By.XPATH, element)
                        like_button.click()
                    except:
                        pass
                break
        except:
            pass    


def reply():
    global driver
    try:  
        print("reply logic")
    except:
        pass
    print("Replied to the message.")

def new_message():
    global driver
    # TODO: Implement the new_message function logic here
    print("New message received.")

def close():
    global driver
    # close the driver
    driver.quit()

def main():

    init()
    load()
    like()
    like()
    like()
    like()
    like()
    like()
    like()
    like()
    like()
    reply()
    new_message()


if __name__ == "__main__":
    main()