from collections import deque
QUEUE_SIZE = 10

def menu():
	print('Choice:');
	print('1. Add customer');
	print('2. Remove customer');
	print('3. Exit');
	
def main():	   
	choice = 0
	d = deque('')
	while choice != 3:
		menu()
		choice = (int)(input('> '))
		
		if choice == 1:
			if len(d) > QUEUE_SIZE - 1:
				print("Jono on jo täynnä")
			else:
				d.append('Asiakas (%d)' % (len(d)+1))
			print('Jonossa:', list(d))
		
		elif choice == 2: 
			if len(d) == 0:
				print("Jono on tyhjä")
			else:
				print("Jonosta poistettiin:", d.pop())
				print("Jonossa:", list(d))

				
main()