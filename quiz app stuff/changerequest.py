def changerequest(_type):
	try:
		selected = _MENU_requestslistbox_.value[0][0]
		selectedid = sqlExecutor(["SELECT user_id FROM gibjohn_user WHERE user_name == ?", (str(selected),)])[0][0]
		currentclassroomlist = eval(sqlExecutor(["SELECT classroom_joinrequests FROM gibjohn_classroom WHERE classroom_id == ?", (int(currentclassroom),)])[0][0])
		currentclassroomlist.remove(selectedid)
		sqlExecutor(["UPDATE gibjohn_classroom SET classroom_joinrequests=? WHERE classroom_id == ?", (str(currentclassroomlist), currentclassroom)])
		refreshjoinrequests()
		if _type=="ACCEPT":
			sqlExecutor(["UPDATE gibjohn_user SET user_classroomid=? WHERE user_id == ?", (currentclassroom, selectedid)])
		####
	except Exception as error:
		mainapp.error("error", "invalid selection")
	####
####
