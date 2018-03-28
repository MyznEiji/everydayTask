from lib import openCommand

file = open('/Users/miyazonoeiji/projects/python/everdayTask/myList/webSiteLists.txt', 'r')
urls = file.read().split(',\n')

openCommand.openWebSite(urls)
