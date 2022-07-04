
def calculator ():

	number1= input("Enter the first number:")
	
	number2= input("Enter the second number:")
	if number2.isdigit() and number1.isdigit():
		 
		
	

		operation1= input("Choose the operation (+, -, /, *):")
		if operation1 == "+":
			total = (int(number1)+int(number2))
			print (f"the answer is {total}")
		elif operation1 =="*":
			total = (int(number1)*int(number2))
			print (f"the answer is {total}")
		elif operation1 =="-":
			total = (int(number1)-int(number2))
			print (f"the answer is {total}")
		elif operation1 =="/":
				total = (int(number1))/(int(number2))
				
		else:
				print ("the operation is not valid")


			
	else:
		print ("the numbers were invalid")


    


def main():
	#write your code here
	pass







calculator()




if __name__ == '__main__':
	main()
