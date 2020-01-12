import os,glob
import sys
sys.path.append("E:\\Rival_test\\bigolive_September\\Mos\\audio_delay_master")
# from audio_delay_master.audio_delay import *
import audio_delay
import numpy as np


xls_path = os.path.abspath(os.curdir)



for root,dirs,files in os.walk(xls_path):


	

	if 'Channel 2'in root and 'Waka' in root and 'Downlink' not in root:
		
	
		
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
