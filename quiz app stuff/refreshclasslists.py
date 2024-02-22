def refreshclasslists():
	listboxestorefresh = [USERRESULTSuserlist]
	[x.clear() for x in listboxestorefresh]
	get_requests = eval(sqlExecutor(["SELECT user_id FROM gibjohn_user WHERE user_classroomid == ?", (currentclassroom,)])[0])
	for x in get_requests:
		name = sqlExecutor(["SELECT user_forename, user_surname FROM gibjohn_user WHERE user_id == ?", (x,)])[0]
		fullname = name[0]+" "+name[1]+" :"+x
		print(fullname)
		[i.append(fullname) for i in listboxestorefresh]
	####
####
