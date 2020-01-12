import os,glob
import sys
# sys.path.append("E:\\a_Derren\\new\\audio_delay")
sys.path.append("./audio_delay")
# from audio_delay_master.audio_delay import *
import audio_delay
import numpy as np


xls_path = os.path.abspath(os.curdir)

try:
	file_arg = sys.argv[1]
except:
	print('plz enter relevant only filename')


for root,dirs,files in os.walk(xls_path):


	

	if 'Channel 2'in root and file_arg in root and 'Downlink' not in root:
		
	
		
		wav_filess =glob.glob(os.path.join(root,"*.wav"))

		print(root)
		audio_delay.get_delay_dir(root,'wav_filess')

	# for file in files:
	# 	# print(root)
	# 	filess = (os.path.join(root,file))

		
	# 	# print files

	# 	# print wav_filess
		
			
			# wav_filess =glob.glob(os.path.join(root,"*.wav"))
			
			# print wav_filess
