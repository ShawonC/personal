import os
import sys
import datetime
import subprocess

class setup:
	def __init__(self):
		# self.configfile = configfile
		self.name = ''
		self.height = ''
		self.weight = ''
		self.workout_week = ''
		self.goals = ''
		self.exercises = ''
	def get_name(self):
		name = input("What is your name?\n")
		self.name = name
