commandsorter = {
	"login"					: lambda:[
		login()
	],
	"signup"				: lambda:[
		signup(),
		print("signup")
	],
	"TOcreateaccount"		: lambda:[
		[x.hide() for x in allForms],
		[[placeholderfunc(x, "reset", False)] for x in alltextboxes if type(x) == type(tk.Entry())],
		SIGNUP.show(),
		SIGNUP_errortext.tk.config(text=""),
		SIGNUP_cookies.tk.deselect(),
		SIGNUP_terms.tk.deselect(),
		fillresizer()
	],
	"TOforgotpassword"		: lambda:[
		mainapp.info("ERROR!", "currently unavailable")
		#[x.hide() for x in allForms],
		#[[placeholderfunc(x, "reset", False)] for x in alltextboxes if type(x) == type(tk.Entry())],
		#FORGOTPASSWORD_errortext.tk.config(text=""),
		#FORGOTPASSWORD.show(),
		#fillresizer()
	],
	"TOlogin"				: lambda:[
		[x.hide() for x in allForms],
		[[placeholderfunc(x, "reset", False)] for x in alltextboxes if type(x) == type(tk.Entry())],
		LOGIN_errortext.tk.config(text=""),
		LOGIN.show(),
		fillresizer()
	],
	"SENDcode"				: lambda:[
		print("send code")	
	],
	"DISPLAYcookies"		: lambda:displaycookiesandterms("cookiestext.txt", SIGNUP_cookies) if SIGNUP_cookies.value==True else [],
	"DISPLAYterms"			: lambda:displaycookiesandterms("termsandconditionstext.txt", SIGNUP_terms) if SIGNUP_terms.value==True else [],
	"UPDATEfont"			: fontchanger,
	"UPDATEfontsearch"		: updatefontsearch,
	"CHANGEpassword"		: changepassword,
	"CHANGEemail"			: changeemail,
	"DISPLAYweight"			: displayweight,
	"COMPAREweight"			: compareuserdata,
	"SUBMITweight"			: submitweight,
	"BUYpremium"			: buypremium,
	"RESETweight"			: resetweight,
	"SHOWMENU"              : lambda:[
		[x.hide() for x in allForms],
		[[placeholderfunc(x, "reset", False)] for x in alltextboxes],
		MENU.show(),
		fillresizer()
	],
	"TOhomemenu"			: lambda:[
		[x.tk.pack_forget() for x in keyforms],
		HOMEMENU.tk.pack(),
		resetbuttoncolours(MENU_homemenubutton),
		commandsorter.get("UPDATEINFOSELECTION")(),
		fillresizer()
	],
	"TOworkoutguides"		: lambda:[
		[x.tk.pack_forget() for x in keyforms],
		WORKOUTGUIDES.tk.pack(),
		resetbuttoncolours(MENU_workoutguidesbutton),
		fillresizer()
	],
	"TOtimetableplanner"	: lambda:[
		[x.tk.pack_forget() for x in keyforms],
		TIMETABLE.tk.pack(),
		resetbuttoncolours(MENU_timetableplannerbutton),
		fillresizer()
	],
	"TObuypremium"			: buypremium,
	"TOviewsetgoals"		: removepremiumboxcover,
	"SIGNOUT"				: None,
	"UPDATEINFOSELECTION"	: lambda: [
		infoboxtext.tk.config(state=tk.DISABLED, fg="black"),
		infoboxtext.tk.config(state=tk.NORMAL),
		infoboxtext.tk.delete("1.0", tk.END),
		infoboxtext.tk.insert(tk.END, [x.get("description") for x in loadedjsonworkouts if x.get("exercise")==workoutlistbox.value][0]),
		infoboxtext.tk.config(state=tk.DISABLED, fg="black"),
		changeworkoutimage(workoutlistbox.value)
	]
}
