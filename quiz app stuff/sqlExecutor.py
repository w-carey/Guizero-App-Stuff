def sqlExecutor(sql):
	# Executes and commits sqlCode to database
	databaseConnection = sqlite3.connect(databaseFile)
	localCursor = databaseConnection.cursor()
	try:
		# Checks wether the sql can be executed as one statement
		localCursor.execute(*sql)
	except Exception as error:
		print("failed to complete SQL (1):", error)
		# If the sql contains multiple statements like the creation of the tables then it will need to use executescript() instead of execute()
		try:
			localCursor.executescript(*sql)
		except Exception as error:
			# If there is an error in the SQL it will be printed to the console 
			print("failed to complete SQL (2):", error)
		####
	####
	fetchedData = localCursor.fetchall() # Collects all the data from an SQL query
	databaseConnection.commit() # Commits the data to the sql database
	databaseConnection.close() # Closes connection to the database
	return(fetchedData) # Returns data from an sql query back
####
