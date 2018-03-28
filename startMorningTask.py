from termcolor import cprint

from lib import openCommand



"""
Morning Flow
"""


# 配列化
file = open('/Users/miyazonoeiji/projects/python/everdayTask/myList/morningLists.txt', 'r')
urlsArray = file.read().split(',\n')

# open Web
cprint("Check Web Site", "yellow")
openCommand.openWebSite(urlsArray)
input(cprint("Next : Enter key", "yellow"))

# mailCheck
cprint("Check Mail", "yellow")
openCommand.mailCheck("mail", "https://mail.google.com/mail/u/0/#inbox")
input(cprint("Next : Enter key", "yellow"))

# discordCheck
cprint("Check Discord", "yellow")
openCommand.openApp("discord")
input(cprint("Next : Enter key", "yellow"))

# slackCheck
cprint("Check Slack", "yellow")
openCommand.openApp("slack")
input(cprint("Fine : Enter key", "red"))
