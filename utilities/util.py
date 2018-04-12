
def cls(lines = 100):
	import os
	if os.name == 'posix':
		os.system("clear")
	elif os.name in ("nt", "dos", "ce"):
		os.system("CLS")
	else:
		print('\n' * lines)

def yesOrNo(prompt = "(Y/N)?"):
	while 1:
		answer = raw_input(prompt)
		answer = answer.strip()
		answer = answer.lower()

		yes = ['yes', 'y', 'ye', 'Y', 'Yes', 'YES', 'YEs', 'yup', 'yep', 'Yup', 'YUP', 'YUp', 'Yep', 'YEP', 'YEp', 'yuh']
		no = ['no', 'n', 'No', 'NO', 'N', 'nope', 'NOPE', 'Nope', 'nah']

		if answer in yes:
			return True
		elif answer in no:
			return False
		else:
			continue
	return False
