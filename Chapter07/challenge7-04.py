answers = ["6", "4", "9", "1"]
while True:
    text = input("数字を入力するか、qで終了:")

    if text == "q":
        break

    elif text in answers:
        print("正解")

    elif text.isdigit():
        print("不正解")

    else:
        print("数字を入力するか、qで終了します")
