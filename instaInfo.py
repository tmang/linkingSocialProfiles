from instagram.client import InstagramAPI
import createHistograms

api = InstagramAPI(client_id='56511a3cf82d4525befd4e7c669a7ab2', client_secret='50e62e2b2a674b0a920af8bed61ab756')

#returns a matching Instagram user from a Reddit username
def getMatch(user):
  try:
    return api.user_search(user)[0]
  except:
    username_error = user + " was no found"


# return a list of matching Instagram users from a list of Reddit usernames 
def getMatches(userlist):
  instalist = []
  
  for user in userlist:
      instalist.append(getMatch(user))
    
  print "There are " + str(len(instalist)) + " Instagram username matches out of the original " + str(len(userlist)) + " Reddit usernames.\n"
  return instalist


# get matching users from a txtfile of Reddit usernames
def getMatchesFromFile(txtfile):
  #parse the file for usernames
  myfile = open(txtfile, 'r')
  loadedlist = myfile.readlines()
  loadedlist = map(lambda s: s.strip(), loadedlist) #remove newline char
  myfile.close()
  
  return getMatches(loadedlist)


# return a dictionary of word counts for a specific user
def countWords(user):
  try:
    recentmedia = api.user_recent_media(user_id=user.id,count=20)
    
    allcaptions = []
    wordDict = {}
    
    # when retrieving captions, remove special characters and convert to lowercase
    for media in recentmedia[0]:
      try:
        allcaptions.append(media.caption.text.translate(None, '.,@#!$').lower().split())
      except:
        media_error = "media not found"
      
    # count occurences of words in all the captions
    for caption in allcaptions:
      for word in caption:
        try:
          wordDict[word] = wordDict[word] + 1
        except: 
          # first occurence of this word
          wordDict[word] = 1
    
    return wordDict
  except:
    print "This user is private."
    
# return a normalized dictionary of word counts for a specific user
def countNormWords(user):
  try:
    wordDict = countWords(user)
    return createHistograms.normalizeWordFreqs(wordDict) 
  except:
    print "This user has no available posts."


# return a normalized dictionary of posting counts (by hour, month, year) for a specific user
def countTimes(user):
  try:
    recentmedia = api.user_recent_media(user_id=user.id,count=20)
    hourDict = {}
    monthDict = {}
    yearDict = {}
    
    for media in recentmedia[0]:
      item = media.created_time

      try: 
        hourDict[item.hour] = timeDict[item.hour] + 1
      except: 
        hourDict[item.hour] = 1 #first occurence of this hour

      try:
        monthDict[item.month] = monthDict[item.month] + 1
      except:
        monthDict[item.month] = 1 #first occurence of this month

      try:
        yearDict[item.year] = yearDict[item.year] + 1
      except:
        yearDict[item.year] = 1 #first occurence of this year

    time = {'hours':hours,'months':months,'years':years}
    return time
    
  except:
    print "This user is private."
    
    
def countNormTimes(user):
  try:
    timeDict = countTimes(user)
    return createHistograms.normalizeTimeFreqs(timeDict[hours], timeDict[months], timeDict[years])

  except:
    print "This user has no available posts."
  

#print word counts and posting time counts for a list of Instagram users
def printAllUserCounts(userlist):
  for user in userlist:
    print "username: " + user.username
    
    #unnormalized
    print "\nWord Counts:"
    print countWords(user)
    print "\nPosting Time Counts:"
    print countTimes(user)

#print normalized word counts and posting time counts for a list of Instagram users
def printAllUserCounts(userlist):
  for user in userlist:
    print "username: " + user.username
    
    #normalized  
    print "\nNormalized Word Counts:"
    print countNormWords(user)
    print "\nNormalized Posting Time Counts:"
    print countNormTimes(user)
    print "\n\n"


