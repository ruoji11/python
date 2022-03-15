# 记录所有名片字典的列表
personal_list = []


def show_menu():
    """显示功能菜单"""
    print("*" * 50)

    print("欢迎使用【名片管理系统】V1.0\n")
    print("1.显示全部")
    print("2.新增名片")
    print("3.查询名片\n")

    print("0:退出系统")
    print("*" * 50)


def show_all():
    """显示所有名片"""
    # 增加判断列表是否为空，如果为空，提升用户增加名片，且不输出表头、名片字典等信息
    if len(personal_list) == 0:
        print("当前名片列表为空，请新增名片！")

        # return可以返回一个函数的执行结果，下方的代码不会被执行
        # 如果return后面没有任何内容，会返回到调用函数的位置，且不会返回任何结果
        return

    # 打印表头
    print("【名片列表】")
    for name in ["姓名","电话","qq","email"]:
        print(name,end="\t\t")
    print("")
    print("-" * 50)
    # 打印名片字典的值
    for card_dict in personal_list:
        print("%s\t\t%s\t\t%s\t\t%s" %(card_dict["name"],
                                       card_dict["phone"],
                                       card_dict["qq"],
                                       card_dict["email"]))

    print("-" * 50)


def new_card():
    """增加新名片"""
    # 1.提示用户输入信息
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入QQ：")
    email = input("请输入Email：")

    # 2.将输入的信息以字典形式保存
    card_dict = {"name": name,
                 "phone": phone,
                 "qq": qq,
                 "email": email}

    # 3.将每个信息字典添加到list中
    personal_list.append(card_dict)

    print(card_dict)

    # 4.提示用户添加成功
    print("添加%s的名片成功" %name)


def search_card():
    """查询名片"""
    # 1.提示用户输入想要查询的姓名
    find_name = input("请输入您想要查找的名片姓名:")
    # 2.遍历名片字典列表查找对应的信息并输出，如果没有找到需要提示用户
    for card_dict in personal_list:
        if card_dict["name"] == find_name:
            for name in ["姓名", "电话", "qq", "email"]:
                print(name, end="\t\t")
            print("")
            print("-" * 50)

            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))

            print("-" * 50)
            # 针对找到的名片信息进行修改或删除操作
            deal_card(card_dict)

            break

    else:

        print("抱歉！没有查找到%s的名片" % find_name)


def deal_card(find_dict):
    """
    :param find_dict: 找到的想要修改的名片字典
    """
    input_str = input("请输入您想执行的操作：1.修改 2.删除 0.返回上级菜单")
    if input_str == "1":
        modify_card(find_dict)
        print("修改名片成功！")

    elif input_str == "2":
        personal_list.remove(find_dict)
        print("删除名片成功！")


# 定义修改名片字典函数
def modify_card(find_dict):
    new_name = input("请输入修改后的名字(回车表示不修改):")
    if len(new_name) > 0:
        find_dict["name"] = new_name

    new_phone = input("请输入修改后的电话(回车表示不修改):")
    if len(new_phone) > 0:
        find_dict["phone"] = new_phone

    new_qq = input("请输入修改后的qq(回车表示不修改):")
    if len(new_qq) > 0:
        find_dict["qq"] = new_qq

    new_email = input("请输入修改后的email(回车表示不修改):")
    if len(new_email) > 0:
        find_dict["email"] = new_email

