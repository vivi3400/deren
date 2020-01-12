# coding=utf-8
import pandas as pd 
import numpy as np
import sys

# 为了展示所有数据，去除display限制
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# 默认使用UDP协议
args = 'UDP'

# 获取文件路径+文件
file = sys.argv[1]

try:
	
	# 获取参数 默认为UDP
	args = sys.argv[2]

	if args == '1':
		args = 'TLSv1.2'

except:
	# 异常那就是没有参数咯
	pass



data = pd.read_csv(file)

time_list = data['frame.time_relative']
#获取这个csv的最大时间
time_max = max(time_list)

print time_max

#小于329秒的话用时间时间，大于329秒就用329秒的数据来计算
if time_max<329:
	print('wrong data')
	duration = time_max
else:
	duration= 329.0

args = 17
# 获取前120s的数据 其余的去掉
data_ = data[(data['ip.proto']==int(args))&(data['frame.time_relative']<=125)&(data['frame.time_relative']>=60)]


duration = 125

# print data_


# 计算码率 将每一个value都用码率公式计算一次
# data_[u'frame.len'] = data_[u'frame.len'].map(lambda x: float(x*8/float(125)/float(1000)))


data_[u'frame.len'] = data_[u'frame.len'].map(lambda x: float(x/float(1024)/float(1024)))

# print data_[u'frame.len']

#行用Source 列用Destination value用计数的Length
data_1 = pd.pivot_table(data_,index=[u'ip.src'],columns=[u'ip.dst'],\
	values=[u'frame.len'],aggfunc='sum',margins=True)

print('------------------------------------')
print('CodeRate in %ss in %s protocol'%(duration,args))
print('------------------------------------')
print(data_1.sort_values(by=('frame.len','All'),ascending=False))

row2 = data_1.iloc[1]


print type(row2)







