import webbrowser

file = open('myList/webSiteLists.txt', 'r')
urls = file.read().split(',\n')

for url in urls:
    if url is '':
        break
    webbrowser.open_new(url)
