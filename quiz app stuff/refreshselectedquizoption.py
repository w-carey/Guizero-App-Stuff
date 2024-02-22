def refreshselectedquizoption():
	editquestionbox.hide()
	quizzesleftboxcreate.hide()
	quizzesleftboxcomplete.hide()
	editquestionbox.hide()
	completequizbox.hide()
	selected = optionsquizlistbox.value
	if selected=="create":
		quizzesleftboxcreate.show()
		global actualquestiondict
		actualquestiondict = copy.deepcopy(defaultquestiondict)
		questionlist.clear()
	elif selected=="complete":
		quizzesleftboxcomplete.show()
	else:
		pass
	####
####
