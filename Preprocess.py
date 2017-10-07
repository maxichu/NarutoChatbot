import os
import re
import json
from nstools.zhtools.langconv import *;

def tradition2simple(line):
    # 将繁体转换成简体
    line = Converter('zh-hans').convert(line);
    return line;

# i = 0
# path = "subtitles";
# out_path="training_data2"
# os.mkdir(out_path);
#
# filelist = os.listdir(path)  # 该文件夹下所有的文件（包括文件夹）
# for files in filelist:  # 遍历所有文件
#     i = i + 1
#     Olddir = os.path.join(path, files);  # 原来的文件路径
#     if os.path.isdir(Olddir):  # 如果是文件夹则跳过
#         continue;
#     filename = os.path.splitext(files)[0];  # 文件名
#     filetype = os.path.splitext(files)[1];  # 文件扩展名
#     Newdir = os.path.join(out_path, str(i).zfill(3) + ".txt");  # 新的文件路径
#     os.rename(Olddir, Newdir)  # 重命名

data=[];
out_path="training_data"

filelist = os.listdir(out_path);

i=0;

for file in filelist:
    with open(out_path+"\\"+file,"r",encoding="utf-8") as file_obj:
        try:
            i += 1;
            print(i);
            content=tradition2simple(file_obj.read());
            valid_str=re.findall(r',,.+,,(.+?)\s+',content);
            data.extend([item.replace("\\N","") for item in valid_str]);

        except Exception as e:
            print("Wrong with "+str(i));


f = open("data.json", "w", encoding = "utf-8" );
json.dump( data, f, ensure_ascii = False, indent = 2 );

out_path = "training_data2"

filelist = os.listdir(out_path);

i = 0;

for file in filelist:
    with open(out_path + "\\" + file, "r", encoding="utf-8") as file_obj:
        try:
            i += 1;
            print(i);
            content = tradition2simple(file_obj.read());
            valid_str = re.findall(r'[1-9]+\s+.+\s+(.+?)', content);
            data.extend([item.replace("\\N", "") for item in valid_str]);

        except Exception as e:
            print("Wrong with " + str(i));

f = open("data.json", "w", encoding="utf-8");
json.dump(data, f, ensure_ascii=False, indent=2);
