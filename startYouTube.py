from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from termcolor import cprint

# youtubeSearchWord.txtから参照
file = open('youtubeSearchWords.txt', 'r')
words = file.read().split(',\n')


# YouTubeを開く
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")


# ワードごとにチェック！
for word in words:
    if word is '':
        break

    wordNum = len(word)

    element = driver.find_element_by_id('search')
    element.send_keys(word)
    driver.find_element_by_id('search-icon-legacy').click()

    cprint("Please press the 'Enteer_Key' as soon as the check is over", "yellow")
    input()
    element.send_keys(Keys.BACK_SPACE * wordNum)


# ダウンロードサイトを開く
driver.get("https://www.onlinevideoconverter.com/ja/video-converter")
cprint("Please press the 'Enteer_Key' when downloading is complete", "yellow")
input()


driver.close()
driver.quit()
