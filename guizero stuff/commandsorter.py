commandsorter = {
	"login"		: lambda:print(),
	"signup"	: lambda:print(),
	"TOforgotP"	: lambda:[
		mainapp.info("ERROR!", "currently unavailable")
	],
	"TOlogin"	: lambda:[
		[x.hide() for x in allForms],
		[[placeholderfunc(x, "reset", False)] for x in alltextboxes if type(x) == type(tk.Entry())],
		LOGIN_errortext.tk.config(text=""),
		LOGIN.show(),
		#fillresizer()
	],
	"TOsignup"	: lambda:[
		[x.hide() for x in allForms],
		[[placeholderfunc(x, "reset", False)] for x in alltextboxes if type(x) == type(tk.Entry())],
		SIGNUP.show(),
		SIGNUP_errortext.tk.config(text=""),
		SIGNUP_cookies.tk.deselect(),
		SIGNUP_terms.tk.deselect(),
		#fillresizer()
	]
}
