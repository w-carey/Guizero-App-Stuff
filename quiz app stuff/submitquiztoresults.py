def submitquiztoresults():
	if len(questionlistbox2.items)>0:
		if not mainapp.yesno("confirmation","you still have {} questions left, are you sure you want to submit this quiz?".format(len(questionlistbox2.items))):
			return
		####
	####
	sqlExecutor(["INSERT INTO gibjohn_results(results_id,results_quizid,results_date,results_data,results_userid) VALUES(?,?,?,?,?)",
(None,int(quizlist2.value.split(":")[1]),str(datetime.datetime.now()),str(current_question_answers),currentlyloggedinto)])
	refreshselectedquizoption()
	mainapp.info("success","quiz completed")
####
