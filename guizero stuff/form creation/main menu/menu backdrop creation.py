
keyforms = [WORKOUTGUIDES, TIMETABLE, HOMEMENU]
_USELESSBOX_					= Box(MENU, width=10, height=5, align="right")
MENU_firstwhite					= Box(MENU, width=mainbox.tk.winfo_width()-215, height=mainbox.tk.winfo_height()-75, align="right")
MENU_firstwhite.bg				= "#FFFFFF"
_USELESSBOX_					= Box(MENU_firstwhite, width="fill", height=10)
MENU_backdrop					= Box(MENU_firstwhite, width=mainbox.tk.winfo_width()-235, height=mainbox.tk.winfo_height()-95)
MENU_backdrop.bg				= "#E6E1C1"
_USELESSBOX_					= Box(MENU_backdrop, width="fill", height=10)
MENU_main						= Box(MENU_backdrop, width=MENU_backdrop.width-20, height=MENU_backdrop.height-20, border=True)
MENU_main.bg					= "#FFFFFF"
_USELESSBOX_					= Box(MENU_main, width=MENU_main.width, height=5)
_MENUTOPBAR_					= Box(MENU_main, width=MENU_main.width, height=30)
_MENUTOPBAR_.bg					= "#BFBFBF"
MENU_title						= Text(_MENUTOPBAR_, width="fill", height="fill")
_USELESSBOX_					= Box(MENU_main, width="fill", height=2)
_USELESSBOX_					= Box(MENU, width=10, height="fill", align="left")
MENU_wafflelist					= Box(MENU, width=mainbox.tk.winfo_width()-525, height=mainbox.tk.winfo_height()-75, align="left")
MENU_wafflelist.bg				= "#FFFFFF"
