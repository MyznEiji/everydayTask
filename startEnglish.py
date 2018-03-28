from termcolor import cprint

from lib import openCommand


# 配列化
file = open('/Users/miyazonoeiji/projects/python/everdayTask/myList/englishTask.txt', 'r')
urlsArray = file.read().split(',\n')


# open Web
openCommand.openWebSite(urlsArray,"Check Web Site")

# Kindle ReadingOpne
openCommand.openApp("kindle", "Check Kindle")

# typora open
path = "/Users/miyazonoeiji/projects/markDown/englishMd/readingEnglish"
new_file_path = openCommand.openTypora(path, "Open Typora")


cprint("Move the" + new_file_path , "red")
