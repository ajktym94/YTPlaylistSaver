import requests, time
from selenium import webdriver

M_URL = "https://www.youtube.com/playlist?list=PLqLu_Fx0uieHjlT21DeCjlL_YMnFVKOsC"
T_URL = "https://www.youtube.com/playlist?list=PLqLu_Fx0uieGh66chFLg-_exltlbjC-c7"
E_URL = "https://www.youtube.com/playlist?list=PLqLu_Fx0uieGh66chFLg-_exltlbjC-c7"
H_URL = ""

browser = webdriver.Firefox()
browser.get(M_URL)
# time.sleep(5)
# browser.switch_to_frame('passive_signin')
# vids = browser.find_element_by_class_name('yt-simple-endpoint style-scope ytd-playlist-video-renderer')
# vids = browser.find_element_by_css_selector('.yt-simple-endpoint style-scope ytd-playlist-video-renderer')

'''iframe = browser.find_element_by_xpath("//iframe[@name='passive_signin']")
browser.switch_to.frame(iframe)
vids = browser.find_element_by_class_name('yt-simple-endpoint style-scope ytd-playlist-video-renderer')'''

vids = browser.find_elements_by_id('video-title')

print(vids[1].get_attribute('href'))

'''res = requests.get(M_URL)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
vids = soup.select('.style-scope ytd-app')
# print(soup.prettify())
# print( vids[0].getText() )

f = open('html.txt','w', encoding='UTF-8')
f.write(soup.prettify())
f.close()'''