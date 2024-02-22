def displayuserresults():
	selected = USERRESULTSuserlist.value
	try:
		selected = selected.split(":")[1]
		selectedquiz = USERRESULTSquizlist.value.split(":")[1]
		quizdata2 = sqlExecutor(["SELECT quiz_data,quiz_duedate FROM gibjohn_quiz WHERE quiz_id == ?", (selectedquiz,)])[0]
		quizdata = eval(quizdata2[0])
		resultsdata2 = sqlExecutor(["SELECT results_data,results_date FROM gibjohn_results WHERE results_userid == ? AND results_quizid == ?", (selected,selectedquiz)])[0]
		resultsdata = eval(resultsdata2[0])
		outputdata = "date due: {}\n".format(quizdata2[1])
		outputdata += "date done: {}\n".format(resultsdata2[1].split(" ")[0])
		totalpoints,userpoints,totalanswers,useranswers = 0,0,0,0
		othertext = ""
		for question in list(quizdata.get("questions").keys()):
			#for qdata in quizdata.get("questions").get(question):
			qdata = quizdata.get("questions").get(question)
			totalpoints += qdata.get("points")
			totalanswers += 1
			correctornot = ""
			if qdata.get("answers")==[resultsdata.get("answers").get(question)]:
				userpoints += qdata.get("points")
				useranswers += 1
				correctornot = "CORRECT"
			else:correctornot = "INCORRECT"
			####
			othertext += qdata.get("questionname")+"\n"
			optionslist = qdata.get("answers")+qdata.get("options");random.shuffle(optionslist)
			othertext += "options: "+",".join(optionslist)
			othertext += "\nchosen: {} \n{}\n\n".format(resultsdata.get("answers").get(question),correctornot)
				
			####
		####
		outputdata += "total points: {}/{}\n".format(userpoints,totalpoints)
		outputdata += "correct answers: {}/{}\n\n".format(useranswers,totalanswers)
		outputdata += othertext
		textboxdata.value = outputdata
	except:pass
####
