import webbrowser
import subprocess
from termcolor import cprint


border1 = "\n#############################################\n"
border2 = "\n---------------------------------------------\n"


def print_info(func):
    """
    decorater
    """

    def wrapper(lists, str):
        # print
        cprint("\n\n" + border1 + str + border1, "yellow")

        # メソッド実行
        result = func(lists)

        # 入力待ち
        input(cprint("\nNext : Enter key" + border2, "yellow"))


        return  result
    return wrapper



# webSite Open
@print_info
def openWebSite(urlsArray):
    for url_a in urlsArray:
        if url_a is '':
            break

        # url pathを取得
        url = url_a.split(',')[1]

        # webサイトopen
        webbrowser.open_new(url)


# App Open
@print_info
def openApp(app):
    subprocess.run(["open -a " + app], shell=True)



# typora open
@print_info
def openTypora(path_a):

    # new file
    cprint("\nFile Name.md : \n", "blue")
    path = path_a
    fileName = str(input())
    linux_command_newFile = "touch " + path + "/" + fileName
    subprocess.run([linux_command_newFile], shell=True)

    # open Typora
    linux_command_typora = "open -a typora " + path_a
    subprocess.run([linux_command_typora], shell=True)

    return str(path + "/" + fileName)
