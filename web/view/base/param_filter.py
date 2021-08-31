

def fnFileCheck(str):
	bAllow = True
	ft = str[-3]
	if ft == "asp" or ft == "htm" or ft == "xml" or ft == "tml" or ft == "cgi" or ft == "jsp" or ft == "php" or ft == "inc":
		bAllow = False
	ft = str[-2]
	if ft == "pl" or ft == "js":
		bAllow = False
	ft = str[-4]
	if ft == "php3" or ft == "html":
		bAllow = False
	return bAllow