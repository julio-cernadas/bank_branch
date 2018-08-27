#!/usr/bin/env python3
import numpy as np
import pandas as pd
import datetime
from bank.Account import Account
from bank.User import User

def bank_Account(acnt_num,balance,type):
	return Account(acnt_num,balance,type)
def bank_User(first_name,last_name,pin_number, username, password):
	return User(first_name,last_name,pin_number, username, password)
def log(x, y, z, v, t):
	lst = [[x, y, z, v, t]]
	df  = pd.DataFrame(lst)
	df.to_csv('./user_logs/{}.csv'.format(y), index=False, header=False, mode='a')
def logging_in():
	exit = False
	while exit is not True:
		print("\nWelcome to Byte-Bank\n")
		print("Enter Command Number:")
		print("[  1  |  2  |  3  ]\n")
		print("1. Log In")
		print("2. Create Account")
		print('3. Leave Bank\n')
		cmd = int(input())
		if cmd == 1:
			df = pd.read_csv('user.csv', names=['First','Last','Pin','Username','Password','Account_Num','Balance','Type'])
			username = input('Enter Username:   ')
			password = input('Enter Password:   ')
			y = df['Username'].str.contains(username).sum()
			x = df['Password'].str.contains(password).sum()
			if y > 0 and x > 0:
				print('\nLogging In...\n')
				x = df[df['Username'].str.contains(username)]
				idx = np.where(df['Username']==username)[0]
				print(idx)
				del_itm = idx[0]
				df.drop([del_itm],axis=0,inplace=True)
				df.to_csv('user.csv', index=False, header=False, mode='w')
				keys = list(x.values.flatten())
				user = bank_User(keys[0],keys[1],keys[2],keys[3],keys[4])
				acnt = bank_Account(keys[5],keys[6],keys[7])
				print('\nWelcome Back {0} {1}'.format(user.first_name,user.last_name))
				print('You Are Now Logged In!')
				print('Enter Command Number: [ 1 | 2 | 3 | 4]')
				print('1. Deposit')
				print('2. Withdraw')
				print('3. Check Balance')
				print('4. Transactions')
				print('5. Log Out\n')
				cmd = int(input())
				while cmd != 5:
					if cmd == 1:
						print('')
						amount = int(input("How Much To Deposit:  "))
						acnt.deposit(amount)
						print("Your Balance Is Now:", acnt.check_balance())
						log(datetime.datetime.now(),acnt.acnt_num,user.first_name,user.last_name,acnt.balance)
					elif cmd == 2:
						print('')
						amount = int(input("How Much To Withdraw:  "))
						acnt.withdraw(amount)
						print("Your Balance Is Now:", acnt.check_balance())
						log(datetime.datetime.now(),acnt.acnt_num,user.first_name,user.last_name,acnt.balance)
					elif cmd == 3:
						print('')
						print("Balance Is: ", acnt.check_balance())
					elif cmd == 4:
						print('')
						df  = pd.read_csv('/Users/julio/Mecha/W3/w3d1/HW_WKND/user_logs/{}.csv'.format(acnt.acnt_num), names=['Date/Time','Account_Num','First','Last','Balance'])
						print(df,'')
					print('\nAny Additional Request?')
					print('1. Deposit')
					print('2. Withdraw')
					print('3. Check Balance')
					print('4. Transactions')
					print('5. Log Out\n')
					cmd = int(input())
				lst = []
				lst.append([user.first_name,user.last_name,user.pin_number,user.username,user.password,acnt.acnt_num,acnt.balance,acnt.type])
				df = pd.DataFrame(lst)
				df.to_csv('user.csv', index=False, header=False, mode='a')
				break
			else:
				print('\nTry Again!\n')
		if cmd == 2:
			first_name = input("What Is Your First Name?    ")
			last_name = input("What Is Your Last Name?     ")
			pin_number = input("Choose Your 4 Digit Pin Number:  ")
			username = input('Enter A Usename:     ')
			password = input('Enter A Password:    ')
			password1 = input('Confirm Password:    ')
			if password == password1:
				welcome = "y"
				if welcome == 'y':
					user = bank_User(first_name, last_name, pin_number, username, password)
					print("Account Type (Checking | Saving )")
					type = input("Type Your Choice:    ")
					acnt_num = np.random.randint(1010101000,1099999999)
					print(acnt_num)
					balance = 0
					acnt = bank_Account(acnt_num, balance, type)
					log(datetime.datetime.now(),acnt.acnt_num,user.first_name,user.last_name,acnt.balance)
					print('_____________________________________')
					print('')
					print("\nAccount created! Welcome: {0} {1}".format(user.first_name, user.last_name))
					print('')
					print('_____________________________________')
					print('')
					print('Here Is Your User Information: ')
					print("Your Account Number Is: {0}".format(acnt.acnt_num))
					print('Username: ', user.username)
					print('Password: ', user.password)
					print("Your Current Balance Is: {0}".format(acnt.balance))
					print('')
					print('_____________________________________')
					print('')
					print('You Are Now Logged In!')
					print('Enter Command Number: [ 1 | 2 | 3 | 4]')
					print('1. Deposit')
					print('2. Withdraw')
					print('3. Check Balance')
					print('4. Log Out\n')
					cmd = int(input())
					while cmd != 4:
						if cmd == 1:
							print('')
							amount = int(input("How Much To Deposit:  "))
							acnt.deposit(amount)
							print("Your Balance Is Now:", acnt.check_balance())
							log(datetime.datetime.now(),acnt.acnt_num,user.first_name,user.last_name,acnt.balance)
						elif cmd == 2:
							print('')
							amount = int(input("How Much To Withdraw:  "))
							acnt.withdraw(amount)
							print("Your Balance Is Now:", acnt.check_balance())
							log(datetime.datetime.now(),acnt.acnt_num,user.first_name,user.last_name,acnt.balance)
						elif cmd == 3:
							print('')
							print("Balance Is: ", acnt.check_balance())
						print('\nAny Additional Request?')
						print('1. Deposit')
						print('2. Withdraw')
						print('3. Check Balance')
						print('4. Log Out\n')
						cmd = int(input())
					lst = []
					lst.append([user.first_name,user.last_name,user.pin_number,user.username,user.password,acnt.acnt_num,acnt.balance,acnt.type])
					df = pd.DataFrame(lst)
					df.to_csv('user.csv', index=False, header=False, mode='a')
					break
			else:
				print("Passwords Do NOT Match!")
				exit = True
		else:
			exit = True

def analysis():
	df = pd.read_csv('user.csv', names=['First','Last','Pin','Username','Password','Account_Num','Balance','Type'])
	print('''

	          ______Master Bank Manager Section______
	          _______________________________________
	          Analysis of Clients ~ Risk/Transactions

	''')

	print(df)
	req = input('\n                  Select Account_Num, Then Enter It Here:  ')
	df  = pd.read_csv('/Users/julio/Mecha/W3/w3d1/HW_WKND/user_logs/{}.csv'.format(req), names=['Date/Time','Account_Num','First','Last','Balance'])
	print(df,'')
	to_plot = df[['Date/Time','Balance']]
	x = to_plot.plot(style=['o','rx'],title='Balance History')
	fig = x.get_figure()
	fig.savefig("output.png")

if __name__ == '__main__':
	logging_in()
	analysis()


