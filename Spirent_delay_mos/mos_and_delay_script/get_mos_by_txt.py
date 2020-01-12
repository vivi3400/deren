import os,glob
import sys
import numpy as np
import matplotlib.pyplot as plt
import numpy as np


xls_path = os.path.abspath(os.curdir)




def read_result(res_file,log_paths):

	f2 = open(res_file,"r")
	lines = f2.readlines()
	
	res_list = []
	lt = []

	for line3 in lines:

	    if 'SUMMARY_RESULT' in line3 and "Uplink" not in line3 :
	    	list3 = line3.split(",")
	    	# print list3[10],list3[13]
	    	lt.append(round(float(list3[10]),3))
	    	# lt.append(int(list3[10]))
	    	# lt.append(list3[10])
	list_len = [_ for _ in range(len(lt))]

	plt.plot(list_len,lt)
	# plt.plot(lt,list_len)

	plt.locator_params('x',nbins=30)
	plt.locator_params('y',nbins=30)


	para_path = os.path.dirname(res_file)

	plt_name = (para_path.split("\\")[-1])+".jpg"


	# des = os.path.join(log_path)
	paths = os.path.join(log_path,plt_name)

	# plt.show()
	plt.savefig(paths)

	plt.close()


	print res_file

	print 'mean  = ',np.mean(lt)





	lt = []



for root,dirs,files in os.walk(xls_path):


	

	if  'Channel 2' not in root and 'Channel 1' not in root and 'rHelloyo' in root and 'Downlink' not in root and 'S_2' not in root:
		
		log_path = os.path.join(os.path.dirname(root),"log")

	
		try:
			os.makedirs(log_path)  
		except:
			pass

	




		result_filess =glob.glob(os.path.join(root,"result.txt"))
		try:
			read_result(result_filess[0],log_path)
		except:
			pass

		
		# read_result(result_filess[0])
