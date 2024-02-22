def createquizfromquestions():
	quiztitle = askstring("TITLE", "quiz title:")
	quizduedate = askstring("DUE DATE", "due date (any format):")
	global actualquestiondict
	actualquestiondict["title"] = quiztitle
	sqlExecutor(["INSERT INTO gibjohn_quiz(quiz_id, quiz_classroomid, quiz_setdate, quiz_duedate, quiz_data) VALUES(?,?,?,?,?)",
(None, currentclassroom, str(datetime.datetime.now()), quizduedate, str(actualquestiondict))])
	refreshselectedquizoption()
####
