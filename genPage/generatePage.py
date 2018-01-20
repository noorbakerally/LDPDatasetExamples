import json
portals = json.load(open("PortalDetails.json","r"))
sources = json.load(open("sources.json","r"))
for portal in portals:
	readableName = portal["readableName"]
	portalUrl = portal["portalUrl"]
	name = portal["name"]

	print "##### "+readableName
	print "Portal URL: ["+portalUrl+"](" + portalUrl+ ")"
	for source in sources:
		if source["name"] == name:
			print "Source URL: "+source["url"]
	print	
	
	for i in range(1,9):
		baseLDP = "http://opensensingcity.emse.fr/ldpdfend/<context>/catalog"
		if i == 7:
			continue
		if i == 8:
			baseLDP = "http://opensensingcity.emse.fr/ldpdfend/<context>/resources"
		if i == 6:
			baseLDP = "http://opensensingcity.emse.fr/ldpdfend/<context>/classes"
		newName = baseLDP.replace("<context>",name+"/d"+str(i))
		print "###### LDP based on Design"+str(i)+":"
		print
		print "- URL:" + newName 
		print "- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri="+ newName
		print
	print
