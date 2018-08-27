#!/usr/bin/env python3

class Account:
	def __init__(self, acnt_num, balance, type):
		self.acnt_num = acnt_num
		self.balance  = balance
		self.type     = type

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		self.balance -= amount

	def check_balance(self):
		return self.balance

