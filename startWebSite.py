from lib import openCommand

file = open('myList/webSiteLists.txt', 'r')
urls = file.read().split(',\n')

openCommand.openWebSite(urls)
