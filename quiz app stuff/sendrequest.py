def sendrequest():
	global currentlyloggedinto
	newclass = INPCLASS_classroomid.value
	try:
		currentclassroomlist = eval(sqlExecutor(["SELECT classroom_joinrequests FROM gibjohn_classroom WHERE classroom_id == ?", (newclass,)])[0][0])
		currentclassroomlist.append(currentlyloggedinto)
		sqlExecutor(["UPDATE gibjohn_classroom SET classroom_joinrequests=? WHERE classroom_id == ?", (str(currentclassroomlist), newclass)])
		INPCLASS_errortext.value = " "
		mainapp.info("SUCCESS", "requested to join classroom id('{}')".format(newclass))
		sqlExecutor(["UPDATE gibjohn_user SET user_classroomid='WAITING' WHERE user_id == ?", (currentlyloggedinto,)])
		changewindow(LOGIN)
		currentlyloggedinto = -1
		mainapp.info("waiting", "please wait for your teacher to approve of your join request to the classroom")
	except:
		INPCLASS_errortext.value = "classroom does not exist"
	####
####
