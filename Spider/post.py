# conding:utf-8
"""

如何txt文件中的内容内容一行行删除，并且每次删除后，返回删除的内容
1.先把文件中的内容读取出来，放到一个列表中
2.将列表中的最后一个数据进行删除
3.然后将列表中的数据通过循环写入到文件中
"""
import os


def read_data(file):
    """读取文件中的内容"""
    with open(file, encoding='utf-8') as f:
        data = f.readlines()
        return data


def delete_file(file):
    """每次调用函数时，会删除文件的最后一行内容，并且将删除的内容返回"""
    file_data = read_data(file)
    # 删除列表中的最后一行，并且循环新列表中的内容，将新的内容写入文件中
    delete_data = file_data.pop()
    # # 判断原文件是否存在，如果存在，就删除,写文件时，会自动创建文件
    if os.path.exists(file):
        os.remove(file)
        for data in file_data:
            """将删除最后一行的列表数据写入文件中"""
            data = data.strip("\n")
            with open(file, mode="a", encoding="utf-8") as f:
                f.write(data)
                f.write("\n")
    return delete_data


def outid():
    file = r"./Spider/30.txt"
    data = delete_file(file).strip().split('-')
    return data[0], data[len(data) - 1]


if __name__ == '__main__':
    file = r"./Spider/30.txt"
    data = delete_file(file).strip().split('-')
    print(data[0],type(data[0]), data[len(data) - 1])
    print(data)
