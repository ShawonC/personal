- Arms:
	dumbbell_curl:
		'name': 'Dumbbell Curl'
		'exercise_type': 'Weights'
		'exercise_mode':
			-'Strength'
			-'Muscle Building'
			-'Endurance'
		'muscle_worked': 'Bicep'
		'equipment': 'Dumbbell'
		'level': 'Beginner'
		'url': 'https://www.bodybuilding.com/exercises/detail/view/name/dumbbell-bicep-curl'

hammer_curl = {
	'name': 'Hammer Curl',
	'exercise_type': 'Weights',
	'exercise_mode': ['Strength', 'Muscle Building', 'Endurance'],
	'muscle_worked': 'Bicep',
	'equipment': 'Dumbbell',
	'level': 'Beginner',
	'url': 'https://www.bodybuilding.com/exercises/detail/view/name/alternate-hammer-curl'
}

barbell_curl = {
	'name': 'Barbell Curl',
	'exercise_type': 'Weights',
	'exercise_mode': ['Strength', 'Muscle Building', 'Endurance'],
	'muscle_worked': 'Biceps',
	'equipment': 'Barbell',
	'level': 'Beginner',
	'url': 'https://www.bodybuilding.com/exercises/main/popup/name/barbell-curl'
}

concentration_curl = {
	'name': 'Concentration Curl',
	'exercise_type': 'Weights',
	'exercise_mode': ['Strength', 'Muscle Building', 'Endurance'],
	'muscle_worked': 'Biceps',
	'equipment': 'Barbell',
	'level': 'Beginner',
	'url': 'https://www.bodybuilding.com/exercises/main/popup/name/concentration-curls'
}

tricep_extension = {
	'name': 'Tricep Extension',
	'exercise_type': 'Weights',
	'exercise_mode': ['Strength', 'Muscle Building', 'Endurance'],
	'muscle_worked': 'Triceps',
	'equipment': 'Dumbbell',
	'level': 'Beginner',
	'url': 'https://www.bodybuilding.com/exercises/main/popup/name/standing-dumbbell-triceps-extension'
}

tricep_kickback = {
	'name': 'Tricep Extension',
	'exercise_type': 'Weights',
	'exercise_mode': ['Strength', 'Muscle Building', 'Endurance'],
	'muscle_worked': 'Tricep',
	'equipment': 'Dumbbell',
	'level': 'Beginner',
	'url': 'https://www.bodybuilding.com/exercises/detail/view/name/tricep-dumbbell-kickback'
}

tricep_pushdown = {
	'name': 'Tricep Pushdown',
	'exercise_type': 'Weights',
	'exercise_mode': ['Strength', 'Muscle Building', 'Endurance'],
	'muscle_worked': 'Tricep',
	'equipment': 'Cable Machine',
	'level': 'Beginner',
	'url': 'https://www.bodybuilding.com/exercises/main/popup/name/triceps-pushdown'	
}

"""Chest Exercises"""
bench_press = {
	'name': 'Bench Press',
	'exercise_type': 'Weights',
	'exercise_mode': ['Strength', 'Muscle Building', 'Endurance'],
	'muscle_worked': 'Pectorals',
	'equipment': ['Barbell', 'Bench', 'Dumbbell'],
	'level': 'Beginner',
	'url': 'https://www.bodybuilding.com/exercises/detail/view/name/barbell-bench-press-medium-grip'
}

incline_press = {
	'name': 'Incline Press',
	'exercise_type': 'Weights',
	'exercise_mode': ['Strength', 'Muscle Building', 'Endurance'],
	'muscle_worked': 'Pectorals',
	'equipment': ['Barbell', 'Bench', 'Dumbbell'],
	'level': 'Beginner',
	'url': 'https://www.bodybuilding.com/exercises/detail/view/name/barbell-incline-bench-press-medium-grip'
}


# arms['Dumbbell Curl'] = dumbbell_curl
# arms['Hammer Curl'] = hammer_curl
# arms['Tricep Kickback'] = tricep_kickback
arms = [dumbbell_curl, hammer_curl, barbell_curl, concentration_curl, tricep_extension, tricep_kickback, tricep_pushdown]
print(json.dumps(arms, indent=4, sort_keys=True))