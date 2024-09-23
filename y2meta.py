import time
from selenium import webdriver

driver = webdriver.Safari()
website = "https://flvto.com.co/en11/"
driver.get(website)
song_list = ["https://www.youtube.com/watch?v=ZcZvVCaoeWU&pp=ygUPa2l5YSBraXlhIGF1ZGlv",
             "https://www.youtube.com/watch?v=9hTMZkzIv4w&pp=ygUTbmFyYXlhbiBuYXJjaSBhdWRpbw%3D%3D"]
for i in song_list:
    search_box = driver.find_element("xpath", "//*[@id='input']")
    search_box.send_keys(i)

    driver.find_element("xpath", "//*[@id='submit']").click()  # search button

    time.sleep(1.5)

    driver.switch_to.window(driver.window_handles[-1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    while True:
        try:
            download = driver.find_element("xpath", "//*[@id='mylink']")
            download.click()
            break
        except:
            continue

    time.sleep(1)
    driver.switch_to.window(driver.window_handles[-1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(15) # instead of waiting i can check if the file s downloaded
    home = driver.find_element("xpath", "//*[@id='buttons']/a[3]") # back home for the next song
    home.click()
driver.close()
