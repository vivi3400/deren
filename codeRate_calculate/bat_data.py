# coding=utf-8
import pandas as pd 
import numpy as np
import sys
import os,glob


csv_path = os.path.abspath(os.curdir)
log_path = os.path.join(csv_path,"log")

files = glob.glob(os.path.join(log_path,"*.csv"))

for i in files:
	# print i
	command = "python data_perspective_codeRate.py %s 17"%i
	# print command
	res = os.popen(command)

	
	s= i.split("/")[-1]
	filename = os.path.basename(s)
	print filename
	print res.read()

	break

