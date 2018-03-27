import webbrowser
import subprocess
from termcolor import cprint

# 配列化
file = open('myList/markdownLinks.txt', 'r')
urlsArray = file.read().split(',\n')
urlsArray[0].split(',')

for url_a in urlsArray:

    if url_a is '':
        break

    # url pathを取得
    url, path = url_a.split(',')[1], url_a.split(',')[2]

    # webサイトopen
    webbrowser.open_new(url)

    while True:
        cprint("Would you like to create a new file? (y/n)", "yellow")
        input_a = str(input())

        if input_a == "y":
            # ファイルを作成
            cprint("\nFile Name.md : \n", "yellow")
            fileName = str(input())
            linux_command_newFile = "touch " + path + "/" + fileName
            subprocess.run([linux_command_newFile], shell=True)

            # typoraを起動
            linux_command_typora = "open -a typora" + path
            subprocess.run([linux_command_typora], shell=True)
            break
        elif input_a == "n":
            cprint("\nnext!\n", "yellow")
            break
        else:
            cprint("\nInvalid Value\n", "red")
