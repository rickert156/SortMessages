import csv, os

start_file = 'sort_by_reason'
sorted_result = 'sorted_result'
result_dir = 'Result'

unique_email = set()

with open(f'{start_file}.txt', 'r') as file_txt:
	number = 0
	for email in file_txt.readlines():
		email = email.strip()
		if email not in unique_email:
			unique_email.add(email)
			number+=1
			print(f'[{number}] {email}')
			with open(f'{sorted_result}.txt', 'a+') as file:
				file.write(f'{email}\n')

print('')
for list_strings in os.listdir(f'{result_dir}/'):
	num = 0
	with open(f'{result_dir}/{list_strings}', 'r') as read_strings:
		line_count = sum(1 for line in read_strings)
		print(f'{list_strings}: [ {line_count} ]')

with open(f'{sorted_result}.txt', 'r') as file:
	line_count = sum(1 for line in file)
	print(f'\nИтого уникальных имелов: [ {line_count} ]')