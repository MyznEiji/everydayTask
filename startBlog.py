from lib import openCommand

file = open('/Users/miyazonoeiji/projects/python/everdayTask/myList/blogLinks.txt', 'r')
urls = file.read().split(',\n')

# Open Blogs
openCommand.openWebSite(urls)
