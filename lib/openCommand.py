import webbrowser
import subprocess
from termcolor import cprint



# webSite Open
def openWebSite(urlsArray):
    for url_a in urlsArray:
        if url_a is '':
            break

        # url pathを取得
        url = url_a.split(',')[1]

        # webサイトopen
        webbrowser.open_new(url)


# App Open
def openApp(app):
    subprocess.run(["open -a " + app], shell=True)


# Mail Check
def mailCheck(app, url):

    openApp(app)
    webbrowser.open_new(url)


# typora open
def openTypora(path_a,linux_command_typora):

    # new file
    cprint("\nFile Name.md : \n", "yellow")
    path = path_a
    fileName = str(input())
    linux_command_newFile = "touch " + path + "/" + fileName
    subprocess.run([linux_command_newFile], shell=True)

    # open Typora
    subprocess.run([linux_command_typora], shell=True)
