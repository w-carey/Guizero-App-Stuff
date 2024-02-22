def addquestiontoselectedlist():
	global actualquestiondict
	currentquestions = actualquestiondict.get("questions").keys()
	newindex = 1
	if len(currentquestions)!=0:
		newindex = list(currentquestions)[-1]+1
	actualquestiondict["questions"][newindex] = {
		"questionname":"this is a default question",
		"answers":["default"],
		"options":["not default", "wow"],
		"points":1
	}
	questionlist.append(newindex)
####
