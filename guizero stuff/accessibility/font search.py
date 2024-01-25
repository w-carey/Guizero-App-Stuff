def updatefontsearch(event):
	# This procedure uses a search algorithm to look through a list of fonts depending on what the user has typed
	textbox, flist, allfonts = fontsearchtextbox, fontlist, list(tk.font.families())
	value = textbox.value.lower()
	if event.char=="\b":
		value = value[:-2]
    ####
	flist.clear()
	for item in allfonts:
		if value in item.lower()[:len(value)+1]:
			flist.append(item)
		####
	####
####
