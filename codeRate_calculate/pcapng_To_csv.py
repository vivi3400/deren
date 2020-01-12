# coding=utf-8
import os,glob
import sys
import subprocess
def sharky(source_file,directory,destnation_file):


        # print(os.path.splitext(source_file))

        s = (source_file.split("\\")[-1])
        filename = os.path.basename(s)
        # filename=(s.split(".")[3])+".csv"
        filename = filename.split(".")[-2]+".csv"
        # print filename
        filename = directory+"_"+filename

        destnation_file=os.path.join(destnation_file,filename)


	# export pcapng as csv
        command_export = ("tshark -r %s -T fields -e frame.number -e frame.time_relative -e ip.src -e ip.dst -e ip.proto -e frame.len -E header=y -E separator=, -E quote=d -E occurrence=f > %s"%(source_file,destnation_file))


	# print(command_export)
        res2 = subprocess.call(command_export,shell=True,stdout = subprocess.PIPE)


def if_pcag(path):

	for lists in os.listdir(path):
		
		print(path)
		if os.path.splitext(lists)[-1] == ".pcap":

			return os.path.join(path,lists)
		else:

			return False

#默认以当前目录作为爬取目录
#遍历当前目录下所有一级文件夹下的pcap文件然后解析成csv放到log文件夹下
csv_path = os.path.abspath(os.curdir)
print( csv_path)

#可手动输入目录
try:
	csv_path = sys.argv[1]
except:
	pass

log_path = os.path.join(csv_path,"log")


#生成log目录
try:
    os.mkdir(log_path)
except:
    pass

for file in os.listdir(csv_path):


	file_path = os.path.join(csv_path,file)


	if os.path.isdir(file_path):
		# print(file_path)
		files = glob.glob(os.path.join(file_path,"*.pcap"))
		
		des = file_path


		for i in files:
			sharky(i,file,log_path)
			
