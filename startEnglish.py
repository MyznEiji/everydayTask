from termcolor import cprint

from lib import openCommand


# 配列化
file = open('/Users/miyazonoeiji/projects/python/everdayTask/myList/englishTask.txt', 'r')
urlsArray = file.read().split(',\n')

# open Web
cprint("Check Web Site", "yellow")
openCommand.openWebSite(urlsArray)
input(cprint("Next : Enter key", "yellow"))

# Kindle ReadingOpne
cprint("Check Kindle", "yellow")
openCommand.openApp("kindle")

# typora open
path = "/Users/miyazonoeiji/projects/markDown/englishMd/readingEnglish"
linux_command_typora = "open -a typora " + path

openCommand.openTypora(path, linux_command_typora)

cprint("Move the new file!!!", "red")
