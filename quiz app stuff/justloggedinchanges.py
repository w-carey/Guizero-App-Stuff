def justloggedinchanges(usertype, userid):
	global currentclassroom
	optionsquizlistbox.clear()
	currentclassroom = sqlExecutor(["SELECT user_classroomid FROM gibjohn_user WHERE user_id == ?", (userid,)])[0][0]
	_MENU_currentclasstext_.value = "CLASSROOM ID: {}".format(currentclassroom)
	if usertype==1:
		teacherboxmenu.show()
		studentboxmenu.hide()
		_MENU_classroomtext_.value = "CLASSROOM STUFF"
		totalpointsteacher.value = "CLASSROOM POINTS: {}".format(gettotalpoints())
		refreshjoinrequests()
		####
		changewindow(MENU)
		optionsquizlistbox.append("create")
		refreshquizresultslist()
		refreshselectedquizoption()
		changemenu(QUIZZES)
	else:
		teacherboxmenu.hide()
		studentboxmenu.show()
		_MENU_classroomtext_.value = "YOUR STUFF"
		####
		if currentclassroom=="SENDREQUEST":
			changewindow(INPCLASS)
			return
		elif currentclassroom=="WAITING":
			mainapp.info("waiting", "please wait for your teacher to approve of your join request to the classroom")
			return
		####
		optionsquizlistbox.append("complete")
		changewindow(MENU)
		refreshselectedquizoption()
		changemenu(QUIZZES)
	####
####
