def refreshquizresultslist():
	boxes = [USERRESULTSquizlist, quizlist2]
	query = sqlExecutor(["SELECT quiz_id,quiz_data FROM gibjohn_quiz WHERE quiz_classroomid == ?", (currentclassroom,)])
	for listbox1 in boxes:
		listbox1.clear()
		if listbox1 == quizlist2:
			for x in query:
				try:query2 = sqlExecutor(["SELECT results_quizid FROM gibjohn_results WHERE results_userid == ? AND results_quizid == ?", (currentlyloggedinto,x[0])])[0][0]
				except:listbox1.append("{} :{}".format(eval(x[1]).get("title"),x[0]))
			####
			continue
		####
		[listbox1.append("{} :{}".format(eval(x[1]).get("title"),x[0]))for x in query]
	####
####
