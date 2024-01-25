def dograph(graphdata):
	# This procedure creates a graph 
	xaxis = [x[0] for x in graphdata] # This takes all of the time recordings and merges them into one list
	if len(xaxis)==2:
		xaxis = xaxis[0] + xaxis[1]
	####
	xaxis.sort()
	def updateyaxis(x):
		reformattedyaxis = [0 for x in xaxis]
		value = 0
		for date in xaxis:
			index = xaxis.index(date)
			for data in [[str(x[0][y])+"||"+str(x[1][y]) for y in range(len(x[0]))] for x in graphdata][x]:
				if data.split("||")[0]==date:
					value = float(data.split("||")[1])
					break
				####
			####
			reformattedyaxis[index] = value
		####
		return reformattedyaxis
	####
	if len(graphdata)==2:
		# This plots the graph if the user selected "compare"
		plt.plot(xaxis, updateyaxis(0))
		plt.plot(xaxis, updateyaxis(1))
	else:
		# This plots the graph if the suer selected "display"
		for data in graphdata:
			plt.plot(*data)
		####
	####
	plt.gcf().autofmt_xdate()
	plt.xlabel("DATES", size=12)
	plt.xticks(rotation=25)
	plt.ylabel("WEIGHT")
	plt.show()
####
