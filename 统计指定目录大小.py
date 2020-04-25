import os
size = 0
def get_dir_size(target_dir):
    global size
    d_list = os.listdir(target_dir)
    print(d_list)

    for f in d_list:
        f = os.path.join(target_dir, f)
        print(f, os.path.getsize(f))
        size += os.path.getsize(f)
    return size

dir_size = get_dir_size(r'C:\Users\Zhiyong Zhou\Desktop\info\AI')

print('总的大小:',dir_size)