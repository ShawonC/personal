import sys
from setup import setup

def main():
	setting = setup()
	setting.get_name()
	setting.get_height()
	setting.get_weight()

main()