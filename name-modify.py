import os
import glob

data_path = 'D:/workspace/SF-GNN/ideaSentence/1_Gothic_select/무'
files_list = glob.glob(data_path + '/*')

for f in files_list:
	new_f = f.replace('_무', '_mu')
	os.rename(f, new_f)
	print('{} --> {}'.format(f,new_f)