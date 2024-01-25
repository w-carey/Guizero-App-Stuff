def fontchanger():
	# This procedure updates the users selected font on the database aswell as changes it in realtime
	selected = fontlist.value
	global defaultfont
	defaultfont = selected
	mainapp.font = selected
	sqlExecutor(["UPDATE tokafitnessDB_user SET user_font = ? WHERE user_ID == ?", (selected, currentlyloggedinto)])
####
