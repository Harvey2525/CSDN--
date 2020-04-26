import os

all_size=0

def dir_size(dir_name):
    global all_size #不然line 16不能取到？？？
    file_list = os.listdir(dir_name) #获取目录区内的文件列表
    print(file_list)
    for file in file_list:
        file_path = os.path.join(dir_name,file) #dir_name路径名和文件名拼起来 得到完整路径
        print(dir_name)
        if os.path.isfile(file_path): #如果是文件 就直接getsize
            size = os.path.getsize(file_path) #一个文件的大小
            print(size)
            all_size+=size   #全部加起来
        else:
            #如果是目录
            dir_size(file_path)  #递归调用 同第6行

dir_size(r'C:\Users\Zhiyong Zhou\Desktop\info\midas')
print(all_size)

