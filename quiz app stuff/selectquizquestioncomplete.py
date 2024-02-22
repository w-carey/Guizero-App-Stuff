def selectquizquestioncomplete():
	quizduesetdate.value = "set on {} | due on {}".format(current_question_data.get("set_date"),current_question_data.get("due_date"))
	if questionlistbox2.value == None:return
	selectedquestion = current_question_data["questions"].get(int(questionlistbox2.value))
	questiontitle3.value = selectedquestion.get("questionname")
	newlist = selectedquestion.get("answers")+selectedquestion.get("options")
	questionpointscount.value = "worth '{}' points".format(selectedquestion.get("points"))
	random.shuffle(newlist)
	answerlistbox.clear()
	[answerlistbox.append(x)for x in newlist]
	topbox55.show()
####
