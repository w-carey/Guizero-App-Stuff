def confirmquestionedits():
	try:
		newanswers, newotheroptions = QUESTIONANSWERSEDIT.value.split(","), QUESTIONOTHERSEDIT.value.split(",")
		newtitle, newpoints, selected = QUESTIONTITLEEDIT.value, int(QUESTIONPOINTSEDIT.value), questionlist.value
		global actualquestiondict
		selecteddict = actualquestiondict["questions"][int(selected)]
		selecteddict["questionname"] = newtitle
		selecteddict["answers"] = newanswers
		selecteddict["options"] = newotheroptions
		selecteddict["points"] = newpoints
		mainapp.info("success", "question data changed")
	except:mainapp.error("error", "exception thrown.. invalid data")
####
