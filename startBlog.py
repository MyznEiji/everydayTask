import webbrowser

from lib import openCommand

file = open('myList/blogLinks.txt', 'r')
urls = file.read().split(',\n')

# Open Blogs
openCommand.openWebSite(urls)
