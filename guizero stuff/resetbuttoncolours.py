def resetbuttoncolours(other):
	# This procedure changes the button colours everytime the user changes tab on the mainmenu
	for x in [MENU_workoutguidesbutton, MENU_timetableplannerbutton, MENU_homemenubutton, MENU_viewsetgoalsbutton, MENU_viewsetgoalsbutton]:
		if x==other:
			x.tk.config(bg="#E6E1C1", fg="#4E4398", font=(defaultfont, 11), borderwidth=0, activebackground="#E6E1C1")
			continue
		####
		x.tk.config(bg="#BFBFBF", fg="#000000", font=(defaultfont, 11), borderwidth=0, activebackground="#BFBFBF")
	####
####
