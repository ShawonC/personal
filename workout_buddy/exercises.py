import requests
import json

exercises = requests.get('http://www.bodybuilding.com/exercises/')
exercises.text

neck = requests.get('http://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/6/muscle/neck')
neck.content
neck.encoding = 'json'
neck.text

# f = open('output.py', 'w')
# f.write(neck.text)
# f.close


# f = open('output.py', 'w')
# f.write(neck.text)
# f.close