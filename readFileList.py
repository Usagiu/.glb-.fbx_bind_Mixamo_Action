import os

list = []
# 指定文件夹路径
folder_path = "/Users/longwind/Downloads/归档"

# 初始化一个空数组来存储文件名
file_list = []

# 使用os.listdir遍历文件夹
for filename in os.listdir(folder_path):
    # 检查文件是否是普通文件（不是目录）
    if os.path.isfile(os.path.join(folder_path, filename)):
        file_list.append(filename)

# 打印文件名数组
print(file_list)