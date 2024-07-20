import csv, re, os

result_dir = 'Result'
exclude_list = 'Exclude'
re_mailing = 'Re_Mailing'

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

address_not_found = "Your message wasn't delivered to", "because the address couldn't be found, or is unable to receive mail.", "couldn't be found. Check for typos or unnecessary spaces and try again."#Исключаем
message_not_delivered = "There was a problem delivering your message to", "See the technical details below.", "See the technical details below."#Исключаем
recipient_inbox_full = "Your message couldn't be delivered to", "Their inbox is full, or it's getting too much mail right now." #Просто забит ящик получателя, оставляем
message_blocked = "Your message to", "has been blocked. See technical details below for more information." #Исключаем
repid_send_message = "There was a temporary problem delivering your message to", "You'll be notified if the delivery fails permanently."#Оставляем

class WriteResult:

	def resultWrite(result_dir, status, email):
		with open(f'{result_dir}/{status}.txt', 'a+') as status:
			status.write(f'{email}\n')

		with open(f'sort_by_reason.txt', 'a+') as all_result:
			all_result.write(f'{email}\n')

	def resultExeption(exclude_list, status, email):
		with open(f'{exclude_list}/{status}.txt', 'a+') as status:
			status.write(f'{email}\n')

	def resultRepid(re_mailing, status, email):
		with open(f'{re_mailing}/{status}.txt', 'a+') as status:
			status.write(f'{email}\n')

	def creatDir():
		if not os.path.exists(result_dir):
			os.makedirs(result_dir)
			print(f'Создана директория: {result_dir}')

		if not os.path.exists(exclude_list):
			os.makedirs(exclude_list)
			print(f'Создана директория: {exclude_list}')

		if not os.path.exists(re_mailing):
			os.makedirs(re_mailing)
			print(f'Создана директория: {re_mailing}')

write_result = WriteResult
write_result.creatDir()

with open('Inbox.mbox', 'r') as file_mbox:
	num=0
	for strings in file_mbox.readlines():
		if address_not_found[0] in strings and address_not_found[1] in strings or address_not_found[2] in strings:
			num+=1
			emails = re.search(email_pattern, strings)
			email = emails.group()
			status = 'address_not_found_txt'
			print(f'[{num}] Address Not Found: {email}')
			write_result.resultWrite(result_dir, status, email)
			write_result.resultExeption(exclude_list, status, email)


		if message_not_delivered[0] in strings and message_not_delivered[1] in strings:
			num+=1
			emails = re.search(email_pattern, strings)
			email = emails.group()
			status = 'message_not_delivered'
			print(f'[{num}] Message not delivered: {email}')
			write_result.resultWrite(result_dir, status, email)
			write_result.resultExeption(exclude_list, status, email)

		if recipient_inbox_full[0] in strings and recipient_inbox_full[1] in strings:
			num+=1
			emails = re.search(email_pattern, strings)
			email = emails.group()
			status = 'recipient_inbox_full'
			print(f'[{num}] Recipient inbox full: {email}')
			write_result.resultWrite(result_dir, status, email)
			write_result.resultExeption(re_mailing, status, email)

		if message_blocked[0] in strings and message_blocked[1] in strings:
			num+=1
			emails = re.search(email_pattern, strings)
			email = emails.group()
			status = 'message_blocked'
			print(f'[{num}] Message blocked: {email}')
			write_result.resultWrite(result_dir, status, email)
			write_result.resultExeption(exclude_list, status, email)		

		if repid_send_message[0] in strings and repid_send_message[1] in strings:
			num+=1
			emails = re.search(email_pattern, strings)
			email = emails.group()
			status = 'repid_send_message'
			print(f'[{num}] Gmail will retry: {email}')
			write_result.resultWrite(result_dir, status, email)
			write_result.resultExeption(re_mailing, status, email)
			

