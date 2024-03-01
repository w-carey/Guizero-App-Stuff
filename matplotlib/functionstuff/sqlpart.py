def compareuserdata():
	# This procedure compares the weighttracker data of two users
	answer = askstring("USERNAME", "Enter other username to compare data:")
	if answer:
		try:
			otheruserid = sqlExecutor(["SELECT user_ID FROM tokafitnessDB_user WHERE user_name == ?", (answer, )])[0][0]
		except:
			# If the SQL fails, e.g. the user does not exist
			print("failed SQL")
			return
		####
		weightanddates = sqlExecutor(["SELECT weight_value, weight_date FROM tokafitnessDB_weightTracker WHERE weight_userID == ?", (currentlyloggedinto, )])
		weights, dates = [float(x[0]) for x in weightanddates], [x[1] for x in weightanddates] # str(x[1]).split(" ")[0] to cut off the time
		weightanddates = sqlExecutor(["SELECT weight_value, weight_date FROM tokafitnessDB_weightTracker WHERE weight_userID == ?", (otheruserid, )])
		weights2, dates2 = [float(x[0]) for x in weightanddates], [x[1] for x in weightanddates] # str(x[1]).split(" ")[0] to cut off the time
		dograph([[dates, weights], [dates2, weights2]])
		return
	####
	print("operation cancelled")
####
