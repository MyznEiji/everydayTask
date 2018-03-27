import webbrowser

file = open('blogLinks.txt', 'r')
urls = file.read().split(',\n')
urls
for url in urls:
    if url is '':
        break
    webbrowser.open_new(url)
