def refreshjoinrequests():
	_MENU_requestslistbox_.clear()
	totalpointsteacher.value = "CLASSROOM POINTS: {}".format(gettotalpoints())
	get_requests = eval(sqlExecutor(["SELECT classroom_joinrequests FROM gibjohn_classroom WHERE classroom_id == ?", (currentclassroom,)])[0][0])
	for x in get_requests:
		name = sqlExecutor(["SELECT user_name FROM gibjohn_user WHERE user_id == ?", (x,)])	
		_MENU_requestslistbox_.append(name)
	####
####
