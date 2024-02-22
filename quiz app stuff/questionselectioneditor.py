def questionselectioneditor():
	editquestionbox.show()
	selected = questionlist.value
	global actualquestiondict
	if not selected:return
	selecteddict = actualquestiondict["questions"][int(selected)]
	QUESTIONTITLE.value = "QUESTION ({}):".format(selected)
	QUESTIONTITLEEDIT.value = selecteddict.get("questionname")
	QUESTIONANSWERSEDIT.value = ",".join(selecteddict.get("answers"))
	QUESTIONOTHERSEDIT.value = ",".join(selecteddict.get("options"))
	QUESTIONPOINTSEDIT.value = selecteddict.get("points")
####
