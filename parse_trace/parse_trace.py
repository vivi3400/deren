import os,glob,sys
import subprocess



def trace_to(source_file,directory,destnation_file,process_args):
        # print(os.path.splitext(source_file))

        s = (source_file.split("\\")[-1])
        filename = os.path.basename(s)
        # filename=(s.split(".")[3])+".csv"
        filename = filename.split(".")[0]+".csv"
        filename = directory+"_"+filename

        destnation_file=os.path.join(destnation_file,filename)

	# export pcapng as csv
        # command_export = ("tshark -r %s -T fields -e frame.number -e frame.time_relative -e ip.src -e ip.dst -e ip.proto -e frame.len -E header=y -E separator=, -E quote=d -E occurrence=f > %s"%(source_file,destnation_file))

        command_cpu_process = ("python session.py cpu %s %s"%(source_file,process_args))

        command_cpu_process = ("python session.py cpu %s mediaserverd"%(source_file))

        command_gpu = ("python session.py gpu %s %s"%(source_file,process_args))

	# print(command_export)
        res2 = subprocess.call(command_cpu_process,shell=True,stdout = subprocess.PIPE)


# try:
# 	process_args = sys.argv[1]
# except:
# 	pass

process_args = sys.argv[1]


print process_args

cur_path = os.path.abspath(os.curdir)

print(cur_path)

log_path = os.path.join(cur_path,"log")




try:
    os.mkdir(log_path)
except:
    pass


for file in os.listdir(cur_path):


	file_path = os.path.join(cur_path,file)


	if os.path.isdir(file_path):
		# print(file_path)
		files = glob.glob(os.path.join(file_path,"*.trace"))

		print files
		
		des = file_path


		for i in files:
			trace_to(i,file,log_path,process_args)

