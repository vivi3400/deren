import os,glob
import xlrd

def read_value(xlsfile):

	workbook =xlrd.open_workbook(xlsfile)

	worksheet = workbook.sheet_by_index(1)

	# print(worksheet)

	values = worksheet.cell_value(9,3)

	print xlsfile
	# print os.path.basename(os.path.normpath(xlsfile))
	# print os.path.normpath(xlsfile)

	try:
		print round(values,3)
	except:
		pass




xls_path = os.path.abspath(os.curdir)


for file in os.listdir(xls_path):


	file_path = os.path.join(xls_path,file)


	if os.path.isdir(file_path):
		# print(file_path)

		for files in os.listdir(file_path):



			files_path = os.path.join(file_path,files)

			

			if os.path.isdir(files_path):

		

				filess = glob.glob(os.path.join(files_path,"*.xlsx"))
				
				if filess:
					# read_value(filess[0])
					print filess
