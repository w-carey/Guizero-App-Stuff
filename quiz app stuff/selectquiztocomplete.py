def selectquiztocomplete():
	selected = quizlist2.value.split(":")[1]
	completequizbox.hide()
	try:
		lbox = questionlistbox2
		lbox.clear()
		quizdata3213 = sqlExecutor(["SELECT quiz_data,quiz_setdate,quiz_duedate FROM gibjohn_quiz WHERE quiz_id == ?", (int(selected),)])[0]
		get_questions = eval(quizdata3213[0])
		questions = list(get_questions.get("questions").keys())
		[lbox.append(x)for x in questions]
		completequizbox.show()
		global current_question_answers
		current_question_answers = {"answers":{}}
		global current_question_data
		current_question_data = copy.deepcopy(get_questions)
		current_question_data["set_date"] = quizdata3213[1].split(" ")[0]
		current_question_data["due_date"] = quizdata3213[2]
		quiztitle111.value = current_question_data.get("title")
		topbox55.show()
	except Exception as error:
		print("error :", error)
	####
####
