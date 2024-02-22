def gettotalpoints():
	allclassroomquiz = sqlExecutor(["SELECT quiz_id,quiz_data FROM gibjohn_quiz WHERE quiz_classroomid == ?", (currentclassroom,)])
	total = 0
	for quiz in allclassroomquiz:
		try:
			answers = {}
			points = 0
			q1 = eval(quiz[1])
			for question in list(q1.get("questions").keys()):
				maindict = q1.get("questions").get(question)
				answers[question] = [maindict.get("answers"),maindict.get("points")]
			####
			quizresults = sqlExecutor(["SELECT results_data FROM gibjohn_results WHERE results_quizid == ?", (quiz[0],)])
			for result in quizresults:
				r1 = None
				try:r1 = eval(result[0])
				except:continue
				data = list(r1.get("answers").keys())
				for y in data:
					thing = answers.get(y)
					if not thing:continue
					if r1.get("answers").get(y) in thing[0]:
						points+=int(thing[1])
					####
				####
			####
			total += points
		except Exception as error:print("error :",error)
	####
	return total
####
