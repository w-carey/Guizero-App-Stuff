
_USELESSBOX_					= Box(MENU_wafflelist, width="fill", height=5)
MENU_workoutguidesbox			= Box(MENU_wafflelist, width="fill", height=25)
MENU_workoutguidesbutton		= PushButton(MENU_workoutguidesbox, width="fill", height="fill", text="Workout Guides", command=commandsorter.get("TOworkoutguides"))
_USELESSBOX_					= Box(MENU_wafflelist, width="fill", height=5)
MENU_timetableplannerbox		= Box(MENU_wafflelist, width="fill", height=25)
MENU_timetableplannerbutton		= PushButton(MENU_timetableplannerbox, width="fill", height="fill", text="Timetable Planner", command=commandsorter.get("TOtimetableplanner"))
MENU_timetableplannerbutton.disable()
_USELESSBOX_					= Box(MENU_wafflelist, width="fill", height=5)
MENU_signoutbox					= Box(MENU_wafflelist, width="fill", height=25)
MENU_signoutbutton				= PushButton(MENU_signoutbox, width="fill", height="fill", text="Sign Out", command=commandsorter.get("SIGNOUT"))
_USELESSBOX_					= Box(MENU_wafflelist, width="fill", height=5)
MENU_homemenubox				= Box(MENU_wafflelist, width="fill", height=50)
MENU_homemenubutton				= PushButton(MENU_homemenubox, width="fill", height="fill", text="➡️ Home Menu", command=commandsorter.get("TOhomemenu"))
########
