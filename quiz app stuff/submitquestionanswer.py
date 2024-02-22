def submitquestionanswer():
	try:
		global current_question_answers
		selected = questionlistbox2.value
		if answerlistbox.value == None:mainapp.error("error","no answer selected");return
		current_question_answers["answers"][selected] = answerlistbox.value
		questionlistbox2.remove(selected)
		topbox55.hide()
		mainapp.info("success","question submitted")
	except Exception as error:
		print("error :", error)
	####
####
