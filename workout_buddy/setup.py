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
	def get_height(self):
		height = input("What is your height?\n")
		self.height = height
	def get_weight(self):
		weight = input("What is your weight?\n")
	# def get_workout(self):
