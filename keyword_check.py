import keyword
def check_keyword(s1):
	if keyword.iskeyword(s1):
		print(s1+" is a keyword")
	else:
		print(s1+" is not a keyword")

while True:
	s1=str(input("Enter keyword"))
	check_keyword(s1)