def removeselectedquestion():
	global actualquestiondict
	currentquestions = actualquestiondict.get("questions").keys()
	selected = questionlist.value
	if not selected:return
	try:
		del actualquestiondict["questions"][int(selected)]
		questionlist.remove(selected)
		editquestionbox.hide()
	except Exception as error:print(error)
####
