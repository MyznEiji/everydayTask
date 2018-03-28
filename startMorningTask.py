from termcolor import cprint

from lib import openCommand



"""
Morning Flow
"""


# 配列化
file = open('/Users/miyazonoeiji/projects/python/everdayTask/myList/morningLists.txt', 'r')
urlsArray = file.read().split(',\n')
urlsArray

# open Web
openCommand.openWebSite(urlsArray, "Check Web Site")


# mailCheck
openCommand.openWebSite(["mail,https://mail.google.com/mail/u/0/#inbox"], "Check Gmail")
openCommand.openApp("mail", "CheckMail")


# discordCheck
openCommand.openApp("discord", "Check Discord")


# slackCheck
openCommand.openApp("slack", "Check Slack")
