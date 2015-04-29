import csv
import tfidf

stoplist = ['a','an','and','are','as','at','be','by','for','from','has','he',
'in','is','it','its','like','of','on','that','the','to','was','were','will','with']
#http://nlp.stanford.edu/IR-book/html/htmledition/dropping-common-terms-stop-words-1.html
#added like

#takes in dictionary frequencies{word:count}
#spits out normalized dictionary
def normalizeWordFreqs(frequencies):
	num = 0
	for entry in frequencies:
		if entry not in stoplist:
			num = num + frequencies.get(entry)

	normalized = {}
	total = 0
	for entry in frequencies:
		percent = (float(frequencies.get(entry))/num)
		normalized[entry] = percent

		total = total + (float(frequencies.get(entry))/num)

	print normalized 
	print 'total is',total


#takes in dictionary for hours, months, years breakdown of posts
#creates a normalized dictionary for hours, months, years
def normalizeTimeFreqs(hours,months,years):

	totalHours = 0
	for item in hours:
		totalHours = totalHours + hours.get(item)
	for item in hours:
		hours[item] = float(hours.get(item))/totalHours
	print hours

	totalMonths = 0
	for item in months:
		totalMonths = totalMonths + months.get(item)
	for item in months:
		months[item] = float(months.get(item))/totalMonths
	print months

	totalYears = 0
	for item in years:
		totalYears = totalYears + years.get(item)
	for item in years:
		years[item] = float(years.get(item))/totalYears
	print years

	time={'hours':hours,'months':months,'years':years}
	return time






