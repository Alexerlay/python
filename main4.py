from selenium.webdriver import Chrome
from pytube import Playlist
driver = Chrome("./chromedriver")
import time
import os
#打開網址
driver.get("https://www.youtube.com/view_all_playlists")
#find -> find_element
#find_all -> find_elements
driver.find_element_by_id("identifierId").send_keys("xxxxx@gmail.com")
driver.find_element_by_id("identifierNext").click()
time.sleep(2)
driver.find_element_by_class_name("whsOnd").send_keys("Password")
driver.find_element_by_id("passwordNext").click()
time.sleep(5)
#拿很多個
ps = driver.find_elements_by_class_name("vm-video-title-text")
for p in ps:
    #bs.text -> .text
    title = p.text
    #["href"] -> get_attribute
    url= p.get_attribute("href")
    print(title, url)

    pl = Playlist(url, suppress_exception=True)
    dirname = "yutube/"+ title +"/"
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    pl.download_all(dirname)
time.sleep(3)
driver.close()
