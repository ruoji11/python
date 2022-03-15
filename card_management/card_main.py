import card_manage


while True:

    # 功能清单
    card_manage.show_menu()

    action_str = input("请输入您想选择的操作：")

    # 1,2,3操作
    if action_str in ["1","2","3"]:
        print("您选择的操作是[%s]" % action_str)
        # 功能1:显示全部
        if action_str == "1":
            card_manage.show_all()
        # 功能2:新增名片
        elif action_str == "2":
            card_manage.new_card()
        # 功能3：查询名片
        else:
            card_manage.search_card()

    # 0操作，退出系统
    elif action_str == "0":
        print("退出成功！")
        break

    # 输入内容错误
    else:
        print("输入错误，请您重新选择想要执行的操作")