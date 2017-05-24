import yaml
import json

with open("./exercises.yaml", 'r') as data:
	data = yaml.load(data)
	arms = data[0]
	arm_exercises = arms['Arms']
	parsed = json.dumps(arm_exercises['dumbbell_curl'], indent=4)
	print(parsed)