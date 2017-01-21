import os
import sys
import datetime
import subprocess

class setup:
	def __init__(self, configfile):
		self.configfile = configfile
		self.name = None
		self.height = None
		self.weight = None
		self.workout_week = None
		self.goals = None
		self.exercises = configfile
