class guizerostuff:
	def createapp(sizex, sizey, appname):
		windowX, windowY = sizex, sizey
		mainapp = App(title=appname, width=windowX, height=windowY)
		mainbox = Box(mainapp, width=windowX-2, height=windowY-10)
		mainapp.bg = "#000000"
		mainbox.bg = "#3F3F3F"
		mainapp.tk.resizable(False, False) # PREVENTS WINDOW RESIZE
		mainapp.tk.bind_all("<Button-1>", lambda event: event.widget.focus_set()) # NEEDED FOR PLACEHOLDER STUFF
		mainbox.tk.pack();mainbox.tk.update()
		return mainapp, mainbox, Box(mainbox, width="fill", height="fill")
	####
	def createappwindow():
		NEWWINDOW = Box(newbox, height=mainbox.tk.winfo_height(), width=mainbox.tk.winfo_width())
		allForms.append(NEWWINDOW)
		return NEWWINDOW
	####
	def uselessbox(root, w, h):
		return Box(root, width=w, height=h)
	####
	def setupmainbox(root, _x, _y):
		_USELESSBOX_					= Box(root, width="fill", height=25)
		_backdrop						= Box(root, width=mainbox.tk.winfo_width()-_x, height=mainbox.tk.winfo_height()-_y)
		_backdrop.bg					= "#E6E1C1"
		_USELESSBOX_					= Box(_backdrop, width="fill", height=15)
		_main							= Box(_backdrop, width=_backdrop.width-30, height=_backdrop.height-30)
		_main.bg						= "#FFFFFF"
		return _backdrop, _main
	####
	def createtopbar(root, title):
		_USELESSBOX_			= Box(root, width=root.width, height=5)
		_TOPBAR					= Box(root, width=root.width, height=25, border=True)
		_TOPBAR.bg				= "#BFBFBF"
		_USELESSBOX_			= Text(_TOPBAR, width="fill", height="fill", text=title)
	####
	def createtextbox(*args):
		root,pholder = args[0],args[1]
		hidden = False
		try:hidden = args[2] or None
		except:pass
		placeholdertext[pholder] = pholder
		_textbox	= TextBox(root, width=35, placeholder=pholder)
		_textbox.tk.bind("<FocusIn>", lambda type: placeholderfunc(_textbox, str(type), hidden))
		_textbox.tk.bind("<FocusOut>", lambda type: placeholderfunc(_textbox, str(type), hidden))
		return _textbox
	####
	def errormessage(message):
		print("wwqdqwdq")
		mainapp.error("ERROR",message)
	####
	def createbutton(root, w, h, text, link):
		_buttonbox			= Box(root, width=w, height=h, border=True)
		_button				= PushButton(_buttonbox, width="fill", height="fill", text=text, command=link)
		_button.bg			= "#BFBFBF"
	####
	def changemenu(targetmenu):
		[x.hide() for x in allForms]
		[[placeholderfunc(x, "reset", False)] for x in alltextboxes if type(x) == type(tk.Entry())]
		targetmenu.show()
	####
	def createcheckbox(root, text, link):
		_checkbox	= CheckBox(root, text=text, command=link)
		_checkbox.tk.config(font=("Calibri", 8), cursor="hand2")
		return _checkbox
	####
	def splithorizontally(root, ratio):
		currentsize = root.width
		ratio = [int(x)for x in ratio.split(":")]
		total = sum(ratio)
		boxes = [Box(root, height=root.height, width=currentsize*(x/total),border=True, align="left")for x in ratio]
		[box.tk.pack() for box in boxes]
		[box.tk.update() for box in boxes]
		return boxes
	####
####
