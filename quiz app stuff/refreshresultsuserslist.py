def refreshresultsuserslist():
	listboxcomp, listboxincomp, selectedquiz = USERRESULTSuserlist, USERRESULTSincompletelist, USERRESULTSquizlist.value
	try:selectedquiz = USERRESULTSquizlist.value.split(":")[1]
	except:pass
	listboxcomp.clear();listboxincomp.clear()
	try:
		usersassigned = sqlExecutor(["SELECT user_id FROM gibjohn_user WHERE user_classroomid == ? AND user_type == 0", (currentclassroom,)])
		for user2 in usersassigned:
			user = user2[0]
			user_name = sqlExecutor(["SELECT user_forename, user_surname FROM gibjohn_user WHERE user_id == ? AND user_type == 0", (user,)])[0]
			user_fullname = user_name[0]+" "+user_name[1]+" :"+str(user)
			try:
				resultsfound = sqlExecutor(["SELECT results_userid FROM gibjohn_results WHERE results_userid == ? AND results_quizid == ?", (user, selectedquiz)])[0][0]
				# found
				listboxcomp.append(user_fullname)
			except Exception as error:
				# not found
				listboxincomp.append(user_fullname)
			####
		####
	except Exception as error:
		print("error :", error)
	####
