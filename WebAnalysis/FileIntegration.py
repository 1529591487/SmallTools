import os


data_path = './'

file_list = os.listdir(data_path)
for item in file_list:
    fileName = os.path.splitext(item)
    if fileName[1] == '.txt':
        print(item)
        with open(item, 'r') as fr:
            with open('Integration.txt','a+') as fw:
                fw.write(fr.read())