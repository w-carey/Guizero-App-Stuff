WORKOUTGUIDES					= Box(MENU_main, height=MENU_main.height, width=MENU_main.width)
WORKOUTGUIDESclonedbox          = Box(WORKOUTGUIDES, height="fill", width="fill")
_USELESSBOX_                    = Box(WORKOUTGUIDESclonedbox, height=10, width="fill", align="bottom")
_USELESSBOX_                    = Box(WORKOUTGUIDESclonedbox, height="fill", width=10, align="left")
_USELESSBOX_                    = Box(WORKOUTGUIDESclonedbox, height="fill", width=10, align="right")
WORKOUTGUIDESleftbox            = Box(WORKOUTGUIDESclonedbox, height="fill", width=140, align="left")
_USELESSBOX_                    = Box(WORKOUTGUIDESclonedbox, height="fill", width=5, align="left")
WORKOUTGUIDESrightbox           = Box(WORKOUTGUIDESclonedbox, height="fill", width="fill", align="right")
WORKOUTGUIDESworkoutlist        = Box(WORKOUTGUIDESleftbox, height="fill", width="fill")
_workoutlisttitlebox_           = Box(WORKOUTGUIDESworkoutlist, height=15, width="fill")
_workoutlsittitle_              = Text(_workoutlisttitlebox_, width="fill", height="fill", text="WORKOUTS")
_workoutlisttitlebox_.bg        = "#BFBFBF"
firstworkout					= [x.get("exercise") for x in loadedjsonworkouts][0]
workoutlistbox                  = ListBox(WORKOUTGUIDESworkoutlist, width="fill", height="fill", items=[x.get("exercise") for x in loadedjsonworkouts], selected=firstworkout, command=commandsorter.get("UPDATEINFOSELECTION"))
workoutlistbox.tk.config(highlightthickness=0, bd=0)
_tokafitnessresize_	            = ImageTk.PhotoImage((Image.open("logo.png")).resize((78, 21), Image.Resampling.LANCZOS))
_tokafitnesslogo_               = Picture(WORKOUTGUIDESworkoutlist, image=_tokafitnessresize_, align="bottom")
workoutinfobox					= Box(WORKOUTGUIDESrightbox, width="fill", height=150, align="top")
_workoutinfotitlebox_           = Box(workoutinfobox, height=15, width="fill")
_workoutinfotitle_              = Text(_workoutinfotitlebox_, width="fill", height="fill", text="INFO")
workoutinfobox.bg				= "#F2F2F2"
_workoutinfotitlebox_.bg        = "#BFBFBF"
_workoutimage_                  = Picture(workoutinfobox,  align="left")	
infobox							= Box(workoutinfobox, height=workoutinfobox.height-20, width="fill", align="left")
infoboxtext						= TextBox(infobox, width="fill", height="fill", text="..", multiline=True)
infoboxtext.tk.config(font=(defaultfont, 10, "italic"))
infoboxtext.text_color			= "black"
_USELESSBOX_					= Box(workoutinfobox, width=10, height="fill", align="right")
infobox.bg						= "#BFBFBF"
_USELESSBOX_					= Box(WORKOUTGUIDESrightbox, width="fill", height=10, align="bottom")
eatinginfobox					= Box(WORKOUTGUIDESrightbox, width="fill", height=150, align="bottom", premium="healthy eating advice")
eatinginfoboxmain				= Box(eatinginfobox, width="fill", height="fill")
_eatinginfotitlebox_			= Box(eatinginfoboxmain, height=15, width="fill", align="top")
_eatinginfotitle_				= Text(_eatinginfotitlebox_, width="fill", height="fill", text="HEALTHY EATING ADVICE")
eatinginfobox.bg				= "#F2F2F2"
_eatinginfotitlebox_.bg			= "#BFBFBF"
eatingcategorybuttonboxes		= Box(eatinginfoboxmain, width="fill", height=30, align="top")
eatingcategorytopbox			= Box(eatingcategorybuttonboxes, width="fill", height=15, align="top")
eatingcategorybotbox			= Box(eatingcategorybuttonboxes, width="fill", height=15, align="bottom")
eatingtopleft					= Box(eatingcategorytopbox, width=145, height="fill", align="left")
eatingtopright					= Box(eatingcategorytopbox, width=145, height="fill", align="right")
eatingbotleft					= Box(eatingcategorybotbox, width=145, height="fill", align="left")
eatingbotright					= Box(eatingcategorybotbox, width=145, height="fill", align="right")
eatingcategory1					= PushButton(eatingtopleft, width="fill", height="fill", align="left", text="Fruits and Vegetables", command=lambda:eatingcategorysorter(eatingcategory1))
eatingcategory2					= PushButton(eatingtopright, width="fill", height="fill", align="right", text="Whole Grains", command=lambda:eatingcategorysorter(eatingcategory2))
eatingcategory3					= PushButton(eatingbotleft, width="fill", height="fill", align="left", text="Lean Proteins", command=lambda:eatingcategorysorter(eatingcategory3))
eatingcategory4					= PushButton(eatingbotright, width="fill", height="fill", align="left", text="Healthy Fats", command=lambda:eatingcategorysorter(eatingcategory4))
eatingbottom					= Box(eatinginfoboxmain, width="fill", height="fill", align="bottom")
eatingleftside					= Box(eatingbottom, width=15, height="fill", align="left")
eatinglistbox					= ListBox(eatingleftside, width="fill", height="fill", items=[1, 2, 3, 4, 5], selected=1, command=reselecteatingcategory)
eatingrightside					= Box(eatingbottom, width="fill", height="fill", align="right")
eatingtipinfo					= TextBox(eatingrightside, width="fill", height="fill", multiline=True, text="None")
eatingtipinfo.text_color		= "black"
eatingtipinfo.tk.config(state=tk.DISABLED, fg="black")
eatingcategory1.tk.config(bg="grey")
eatingcategory2.tk.config(bg="white")
eatingcategory3.tk.config(bg="white")
eatingcategory4.tk.config(bg="white")
eatingcategory1.disable()
reselecteatingcategory()
