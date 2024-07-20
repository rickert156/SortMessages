#!/usr/bin/python3
import os, shutil

result_dir = 'Result'
exclude_list = 'Exclude'
re_mailing = 'Re_Mailing'
result_file = ['sorted_result.txt', 'sort_by_reason.txt']

for delete_file in result_file:
	if os.path.exists(delete_file):
		os.remove(delete_file)

if os.path.exists(result_dir):
	shutil.rmtree(result_dir)
if os.path.exists(exclude_list):
	shutil.rmtree(exclude_list)
if os.path.exists(re_mailing):
	shutil.rmtree(re_mailing)