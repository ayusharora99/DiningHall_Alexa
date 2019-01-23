from bs4 import BeautifulSoup
import requests
import re
from boto.s3.connection import S3Connection, Bucket, Key
import boto3
from botocore.client import Config

s3 = boto3.resource(
	's3',
	aws_access_key_id=ACCESS_KEY_ID,
	aws_secret_access_key=ACCESS_SECRET_KEY,
	config=Config(signature_version='s3v4')
)

bucket = s3.Bucket('dininghall')

bucket.objects.all().delete()

def getNineTenMeals():

	page_link = "https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=40&locationName=Colleges+Nine+%26+Ten+Dining+Hall&sName=&naFlag="

	#cowell - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=05&locationName=Cowell+Stevenson+Dining+Hall&sName=&naFlag=

	#crown - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=20&locationName=Crown+Merrill+Dining+Hall&sName=&naFlag=

	#porter - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=25&locationName=Porter+Kresge+Dining+Hall&sName=&naFlag=

	#rc - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=30&locationName=Rachel+Carson+Oakes+Dining+Hall&sName=&naFlag=

	#ten - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=40&locationName=Colleges+Nine+%26+Ten+Dining+Hall&sName=&naFlag=

	page_response = requests.get(page_link, timeout=5)

	page_content = BeautifulSoup(page_response.content, "html.parser")

	textcontent = []
	breakfastList = []
	lunchList = []
	dinnerList = []
	lateNightList = []

	lateNightHappening = False

	htmlMeals = page_content.find_all("div", attrs={'class': "menusamprecipes"})

	for i in range(len(htmlMeals)):
	    textcontent.append(htmlMeals[i].text)

	#------
	htmlMeals = page_content.find_all('td', attrs={'valign': 'top'})
	meals = ''

	for i in range(0, len(htmlMeals)):
		meals = meals + htmlMeals[i].text

	if len(meals) == 0:
		return

	b = meals.split("Lunch")
	breakfast = b[0]
	l = b[1].split("Dinner")
	lunch = l[0]
	dinner = l[1]
	ln = dinner.split("Late Night")
	if len(ln) > 1:
	    lateNight = ln[1]
	    dinner = ln[0]
	    lateNightHappening = True

	breakfast = re.sub(r'\W+', ' ', breakfast)
	lunch = re.sub(r'\W+', ' ', lunch)
	dinner = re.sub(r'\W+', ' ', dinner)
	if lateNightHappening:
	    lateNight = re.sub(r'\W+', ' ', lateNight)

	for s in textcontent:
	    if s in breakfast and s not in breakfastList:
	        breakfastList.append(s)

	for s in textcontent:
	    if s in lunch and s not in lunchList:
	        lunchList.append(s)

	for s in textcontent:
	    if s in dinner and s not in dinnerList:
	        dinnerList.append(s)

	if lateNightHappening:
	    for s in textcontent:
	        if s in lateNight and s not in lateNightList:
	            lateNightList.append(s)

	bf = open("NineTenbreakfast.txt", "w")
	lun = open("NineTenlunch.txt", "w")
	din = open("NineTendinner.txt", "w")
	if lateNightHappening:
		late = open("NineTenlateNight.txt", "w")

	for i in range(len(breakfastList)):
		if '&' in breakfastList[i]:
			breakfastList[i].replace("&", "and")
		if(i < len(breakfastList) - 1):
			bf.write(breakfastList[i] + ", ")
		else:
			bf.write("and " + breakfastList[i])

	for i in range(len(lunchList)):
		if '&' in lunchList[i]:
			lunchList[i].replace("&", "and")
		if(i < len(lunchList) - 1):
			lun.write(lunchList[i] + ", ")
		else:
			lun.write("and " + lunchList[i])

	for i in range(len(dinnerList)):
		if '&' in dinnerList[i]:
			dinnerList[i].replace("&", "and")
		if(i < len(dinnerList) - 1):
			din.write(dinnerList[i] + ", ")
		else:
			din.write("and " + dinnerList[i])

	if lateNightHappening:
		for i in range(len(lateNightList)):
			if '&' in lateNightList[i]:
				lateNightList[i].replace("&", "and")
			if(i < len(lateNightList) - 1):
				late.write(lateNightList[i] + ", ")
			else:
				late.write("and " + lateNightList[i])

	bf.close()
	lun.close()
	din.close()
	if lateNightHappening:
		late.close()

	if not lateNightHappening:
		filenames = ['NineTenbreakfast.txt', 'NineTenlunch.txt', 'NineTendinner.txt']
	else:
		filenames = ['NineTenbreakfast.txt', 'NineTenlunch.txt', 'NineTendinner.txt', 'NineTenlateNight.txt']

	conn = S3Connection(aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=ACCESS_SECRET_KEY)

	for fname in filenames:
	    bucket = conn.get_bucket("dininghall")
	    content = open(fname, 'r')
	    read_data = content.read()
	    key = bucket.new_key(fname).set_contents_from_string(read_data)
	    print ("uploaded file %s" % fname)

def getCowellStevensonMeals():

	page_link = "https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=05&locationName=Cowell+Stevenson+Dining+Hall&sName=&naFlag="

	#cowell - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=05&locationName=Cowell+Stevenson+Dining+Hall&sName=&naFlag=

	#crown - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=20&locationName=Crown+Merrill+Dining+Hall&sName=&naFlag=

	#porter - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=25&locationName=Porter+Kresge+Dining+Hall&sName=&naFlag=

	#rc - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=30&locationName=Rachel+Carson+Oakes+Dining+Hall&sName=&naFlag=

	#ten - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=40&locationName=Colleges+Nine+%26+Ten+Dining+Hall&sName=&naFlag=

	page_response = requests.get(page_link, timeout=5)

	page_content = BeautifulSoup(page_response.content, "html.parser")

	textcontent = []
	breakfastList = []
	lunchList = []
	dinnerList = []
	lateNightList = []

	lateNightHappening = False

	htmlMeals = page_content.find_all("div", attrs={'class': "menusamprecipes"})

	for i in range(len(htmlMeals)):
	    textcontent.append(htmlMeals[i].text)

	#------
	htmlMeals = page_content.find_all('td', attrs={'valign': 'top'})
	meals = ''

	for i in range(0, len(htmlMeals)):
		meals = meals + htmlMeals[i].text

	if len(meals) == 0:
		return

	b = meals.split("Lunch")
	breakfast = b[0]
	l = b[1].split("Dinner")
	lunch = l[0]
	dinner = l[1]
	ln = dinner.split("Late Night")
	if len(ln) > 1:
	    lateNight = ln[1]
	    dinner = ln[0]
	    lateNightHappening = True

	breakfast = re.sub(r'\W+', ' ', breakfast)
	lunch = re.sub(r'\W+', ' ', lunch)
	dinner = re.sub(r'\W+', ' ', dinner)

	if lateNightHappening:
	    lateNight = re.sub(r'\W+', ' ', lateNight)

	for s in textcontent:
	    if s in breakfast and s not in breakfastList:
	        breakfastList.append(s)

	for s in textcontent:
	    if s in lunch and s not in lunchList:
	        lunchList.append(s)

	for s in textcontent:
	    if s in dinner and s not in dinnerList:
	        dinnerList.append(s)

	if lateNightHappening:
	    for s in textcontent:
	        if s in lateNight and s not in lateNightList:
	            lateNightList.append(s)

	bf = open("CowellStevensonbreakfast.txt", "w")
	lun = open("CowellStevensonlunch.txt", "w")
	din = open("CowellStevensondinner.txt", "w")
	if lateNightHappening:
		late = open("CowellStevensonlateNight.txt", "w")

	for i in range(len(breakfastList)):
		if '&' in breakfastList[i]:
			breakfastList[i].replace("&", "and")
		if(i < len(breakfastList) - 1):
			bf.write(breakfastList[i] + ", ")
		else:
			bf.write("and " + breakfastList[i])

	for i in range(len(lunchList)):
		if '&' in lunchList[i]:
			lunchList[i].replace("&", "and")
		if(i < len(lunchList) - 1):
			lun.write(lunchList[i] + ", ")
		else:
			lun.write("and " + lunchList[i])

	for i in range(len(dinnerList)):
		if '&' in dinnerList[i]:
			dinnerList[i].replace("&", "and")
		if(i < len(dinnerList) - 1):
			din.write(dinnerList[i] + ", ")
		else:
			din.write("and " + dinnerList[i])

	if lateNightHappening:
		for i in range(len(lateNightList)):
			if '&' in lateNightList[i]:
				lateNightList[i].replace("&", "and")
			if(i < len(lateNightList) - 1):
				late.write(lateNightList[i] + ", ")
			else:
				late.write("and " + lateNightList[i])

	bf.close()
	lun.close()
	din.close()
	if lateNightHappening:
		late.close()

	if lateNightHappening:
		late.close()

	if not lateNightHappening:
		filenames = ['CowellStevensonbreakfast.txt', 'CowellStevensonlunch.txt', 'CowellStevensondinner.txt']
	else:
		filenames = ['CowellStevensonbreakfast.txt', 'CowellStevensonlunch.txt', 'CowellStevensondinner.txt', 'CowellStevensonlateNight.txt']

	conn = S3Connection(aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=ACCESS_SECRET_KEY)

	for fname in filenames:
	    bucket = conn.get_bucket("dininghall")
	    content = open(fname, 'r')
	    read_data = content.read()
	    key = bucket.new_key(fname).set_contents_from_string(read_data)
	    print ("uploaded file %s" % fname)

def getCrownMerrilMeals():

	page_link = "https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=20&locationName=Crown+Merrill+Dining+Hall&sName=&naFlag="

	#cowell - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=05&locationName=Cowell+Stevenson+Dining+Hall&sName=&naFlag=

	#crown - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=20&locationName=Crown+Merrill+Dining+Hall&sName=&naFlag=

	#porter - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=25&locationName=Porter+Kresge+Dining+Hall&sName=&naFlag=

	#rc - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=30&locationName=Rachel+Carson+Oakes+Dining+Hall&sName=&naFlag=

	#ten - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=40&locationName=Colleges+Nine+%26+Ten+Dining+Hall&sName=&naFlag=

	page_response = requests.get(page_link, timeout=5)

	page_content = BeautifulSoup(page_response.content, "html.parser")

	textcontent = []
	breakfastList = []
	lunchList = []
	dinnerList = []
	lateNightList = []

	lateNightHappening = False

	htmlMeals = page_content.find_all("div", attrs={'class': "menusamprecipes"})

	for i in range(len(htmlMeals)):
	    textcontent.append(htmlMeals[i].text)

	#------
	htmlMeals = page_content.find_all('td', attrs={'valign': 'top'})
	meals = ''

	for i in range(0, len(htmlMeals)):
		meals = meals + htmlMeals[i].text

	if len(meals) == 0:
		return

	b = meals.split("Lunch")
	breakfast = b[0]
	l = b[1].split("Dinner")
	lunch = l[0]
	dinner = l[1]
	ln = dinner.split("Late Night")
	if len(ln) > 1:
	    lateNight = ln[1]
	    dinner = ln[0]
	    lateNightHappening = True

	breakfast = re.sub(r'\W+', ' ', breakfast)
	lunch = re.sub(r'\W+', ' ', lunch)
	dinner = re.sub(r'\W+', ' ', dinner)
	if lateNightHappening:
	    lateNight = re.sub(r'\W+', ' ', lateNight)

	for s in textcontent:
	    if s in breakfast and s not in breakfastList:
	        breakfastList.append(s)

	for s in textcontent:
	    if s in lunch and s not in lunchList:
	        lunchList.append(s)

	for s in textcontent:
	    if s in dinner and s not in dinnerList:
	        dinnerList.append(s)

	if lateNightHappening:
	    for s in textcontent:
	        if s in lateNight and s not in lateNightList:
	            lateNightList.append(s)

	bf = open("CrownMerrilbreakfast.txt", "w")
	lun = open("CrownMerrillunch.txt", "w")
	din = open("CrownMerrildinner.txt", "w")
	if lateNightHappening:
		late = open("CrownMerrillateNight.txt", "w")

	for i in range(len(breakfastList)):
		if '&' in breakfastList[i]:
			breakfastList[i].replace("&", "and")
		if(i < len(breakfastList) - 1):
			bf.write(breakfastList[i] + ", ")
		else:
			bf.write("and " + breakfastList[i])

	for i in range(len(lunchList)):
		if '&' in lunchList[i]:
			lunchList[i].replace("&", "and")
		if(i < len(lunchList) - 1):
			lun.write(lunchList[i] + ", ")
		else:
			lun.write("and " + lunchList[i])

	for i in range(len(dinnerList)):
		if '&' in dinnerList[i]:
			dinnerList[i].replace("&", "and")
		if(i < len(dinnerList) - 1):
			din.write(dinnerList[i] + ", ")
		else:
			din.write("and " + dinnerList[i])

	if lateNightHappening:
		for i in range(len(lateNightList)):
			if '&' in lateNightList[i]:
				lateNightList[i].replace("&", "and")
			if(i < len(lateNightList) - 1):
				late.write(lateNightList[i] + ", ")
			else:
				late.write("and " + lateNightList[i])

	bf.close()
	lun.close()
	din.close()
	if lateNightHappening:
		late.close()

	if not lateNightHappening:
		filenames = ['CrownMerrilbreakfast.txt', 'CrownMerrillunch.txt', 'CrownMerrildinner.txt']
	else:
		filenames = ['CrownMerrilbreakfast.txt', 'CrownMerrillunch.txt', 'CrownMerrildinner.txt', 'CrownMerrillateNight.txt']

	conn = S3Connection(aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=ACCESS_SECRET_KEY)

	for fname in filenames:
	    bucket = conn.get_bucket("dininghall")
	    content = open(fname, 'r')
	    read_data = content.read()
	    key = bucket.new_key(fname).set_contents_from_string(read_data)
	    print ("uploaded file %s" % fname)

def getPorterKresgeMeals():

	page_link = "https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=25&locationName=Porter+Kresge+Dining+Hall&sName=&naFlag="

	#cowell - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=05&locationName=Cowell+Stevenson+Dining+Hall&sName=&naFlag=

	#crown - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=20&locationName=Crown+Merrill+Dining+Hall&sName=&naFlag=

	#porter - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=25&locationName=Porter+Kresge+Dining+Hall&sName=&naFlag=

	#rc - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=30&locationName=Rachel+Carson+Oakes+Dining+Hall&sName=&naFlag=

	#ten - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=40&locationName=Colleges+Nine+%26+Ten+Dining+Hall&sName=&naFlag=

	page_response = requests.get(page_link, timeout=5)

	page_content = BeautifulSoup(page_response.content, "html.parser")

	textcontent = []
	breakfastList = []
	lunchList = []
	dinnerList = []
	lateNightList = []

	lateNightHappening = False

	htmlMeals = page_content.find_all("div", attrs={'class': "menusamprecipes"})

	for i in range(len(htmlMeals)):
	    textcontent.append(htmlMeals[i].text)

	#------
	htmlMeals = page_content.find_all('td', attrs={'valign': 'top'})
	meals = ''

	for i in range(0, len(htmlMeals)):
		meals = meals + htmlMeals[i].text

	if len(meals) == 0:
		return

	b = meals.split("Lunch")
	breakfast = b[0]
	l = b[1].split("Dinner")
	lunch = l[0]
	dinner = l[1]
	ln = dinner.split("Late Night")
	if len(ln) > 1:
	    lateNight = ln[1]
	    dinner = ln[0]
	    lateNightHappening = True

	breakfast = re.sub(r'\W+', ' ', breakfast)
	lunch = re.sub(r'\W+', ' ', lunch)
	dinner = re.sub(r'\W+', ' ', dinner)
	if lateNightHappening:
	    lateNight = re.sub(r'\W+', ' ', lateNight)

	for s in textcontent:
	    if s in breakfast and s not in breakfastList:
	        breakfastList.append(s)

	for s in textcontent:
	    if s in lunch and s not in lunchList:
	        lunchList.append(s)

	for s in textcontent:
	    if s in dinner and s not in dinnerList:
	        dinnerList.append(s)

	if lateNightHappening:
	    for s in textcontent:
	        if s in lateNight and s not in lateNightList:
	            lateNightList.append(s)

	bf = open("PorterKresgebreakfast.txt", "w")
	lun = open("PorterKresgelunch.txt", "w")
	din = open("PorterKresgedinner.txt", "w")
	if lateNightHappening:
		late = open("PorterKresgelateNight.txt", "w")

	for i in range(len(breakfastList)):
		if '&' in breakfastList[i]:
			breakfastList[i].replace("&", "and")
		if(i < len(breakfastList) - 1):
			bf.write(breakfastList[i] + ", ")
		else:
			bf.write("and " + breakfastList[i])

	for i in range(len(lunchList)):
		if '&' in lunchList[i]:
			lunchList[i].replace("&", "and")
		if(i < len(lunchList) - 1):
			lun.write(lunchList[i] + ", ")
		else:
			lun.write("and " + lunchList[i])

	for i in range(len(dinnerList)):
		if '&' in dinnerList[i]:
			dinnerList[i].replace("&", "and")
		if(i < len(dinnerList) - 1):
			din.write(dinnerList[i] + ", ")
		else:
			din.write("and " + dinnerList[i])

	if lateNightHappening:
		for i in range(len(lateNightList)):
			if '&' in lateNightList[i]:
				lateNightList[i].replace("&", "and")
			if(i < len(lateNightList) - 1):
				late.write(lateNightList[i] + ", ")
			else:
				late.write("and " + lateNightList[i])

	bf.close()
	lun.close()
	din.close()
	if lateNightHappening:
		late.close()

	if not lateNightHappening:
		filenames = ['PorterKresgebreakfast.txt', 'PorterKresgelunch.txt', 'PorterKresgedinner.txt']
	else:
		filenames = ['PorterKresgebreakfast.txt', 'PorterKresgelunch.txt', 'PorterKresgedinner.txt', 'PorterKresgelateNight.txt']

	conn = S3Connection(aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=ACCESS_SECRET_KEY)

	for fname in filenames:
	    bucket = conn.get_bucket("dininghall")
	    content = open(fname, 'r')
	    read_data = content.read()
	    key = bucket.new_key(fname).set_contents_from_string(read_data)
	    print ("uploaded file %s" % fname)

def getCarsonOakesMeals():

	page_link = "https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=30&locationName=Rachel+Carson+Oakes+Dining+Hall&sName=&naFlag="

	#cowell - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=05&locationName=Cowell+Stevenson+Dining+Hall&sName=&naFlag=

	#crown - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=20&locationName=Crown+Merrill+Dining+Hall&sName=&naFlag=

	#porter - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=25&locationName=Porter+Kresge+Dining+Hall&sName=&naFlag=

	#rc - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=30&locationName=Rachel+Carson+Oakes+Dining+Hall&sName=&naFlag=

	#ten - https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=40&locationName=Colleges+Nine+%26+Ten+Dining+Hall&sName=&naFlag=

	page_response = requests.get(page_link, timeout=5)

	page_content = BeautifulSoup(page_response.content, "html.parser")

	textcontent = []
	breakfastList = []
	lunchList = []
	dinnerList = []
	lateNightList = []

	lateNightHappening = False

	htmlMeals = page_content.find_all("div", attrs={'class': "menusamprecipes"})

	for i in range(len(htmlMeals)):
	    textcontent.append(htmlMeals[i].text)

	#------
	htmlMeals = page_content.find_all('td', attrs={'valign': 'top'})
	meals = ''

	for i in range(0, len(htmlMeals)):
		meals = meals + htmlMeals[i].text

	if len(meals) == 0:
		return

	b = meals.split("Lunch")
	breakfast = b[0]
	l = b[1].split("Dinner")
	lunch = l[0]
	dinner = l[1]
	ln = dinner.split("Late Night")
	if len(ln) > 1:
	    lateNight = ln[1]
	    dinner = ln[0]
	    lateNightHappening = True

	breakfast = re.sub(r'\W+', ' ', breakfast)
	lunch = re.sub(r'\W+', ' ', lunch)
	dinner = re.sub(r'\W+', ' ', dinner)
	if lateNightHappening:
	    lateNight = re.sub(r'\W+', ' ', lateNight)

	for s in textcontent:
	    if s in breakfast and s not in breakfastList:
	        breakfastList.append(s)

	for s in textcontent:
	    if s in lunch and s not in lunchList:
	        lunchList.append(s)

	for s in textcontent:
	    if s in dinner and s not in dinnerList:
	        dinnerList.append(s)

	if lateNightHappening:
	    for s in textcontent:
	        if s in lateNight and s not in lateNightList:
	            lateNightList.append(s)

	bf = open("CarsonOakesbreakfast.txt", "w")
	lun = open("CarsonOakeslunch.txt", "w")
	din = open("CarsonOakesdinner.txt", "w")
	if lateNightHappening:
		late = open("CarsonOakeslateNight.txt", "w")

	for i in range(len(breakfastList)):
		if '&' in breakfastList[i]:
			breakfastList[i].replace("&", "and")
		if(i < len(breakfastList) - 1):
			bf.write(breakfastList[i] + ", ")
		else:
			bf.write("and " + breakfastList[i])

	for i in range(len(lunchList)):
		if '&' in lunchList[i]:
			lunchList[i].replace("&", "and")
		if(i < len(lunchList) - 1):
			lun.write(lunchList[i] + ", ")
		else:
			lun.write("and " + lunchList[i])

	for i in range(len(dinnerList)):
		if '&' in dinnerList[i]:
			dinnerList[i].replace("&", "and")
		if(i < len(dinnerList) - 1):
			din.write(dinnerList[i] + ", ")
		else:
			din.write("and " + dinnerList[i])

	if lateNightHappening:
		for i in range(len(lateNightList)):
			if '&' in lateNightList[i]:
				lateNightList[i].replace("&", "and")
			if(i < len(lateNightList) - 1):
				late.write(lateNightList[i] + ", ")
			else:
				late.write("and " + lateNightList[i])

	bf.close()
	lun.close()
	din.close()
	if lateNightHappening:
		late.close()

	if not lateNightHappening:
		filenames = ['CarsonOakesbreakfast.txt', 'CarsonOakeslunch.txt', 'CarsonOakesdinner.txt']
	else:
		filenames = ['CarsonOakesbreakfast.txt', 'CarsonOakeslunch.txt', 'CarsonOakesdinner.txt', 'CarsonOakeslateNight.txt']

	conn = S3Connection(aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=ACCESS_SECRET_KEY)

	for fname in filenames:
	    bucket = conn.get_bucket("dininghall")
	    content = open(fname, 'r')
	    read_data = content.read()
	    key = bucket.new_key(fname).set_contents_from_string(read_data)
	    print ("uploaded file %s" % fname)

getNineTenMeals()

getCowellStevensonMeals()

getCrownMerrilMeals()

getPorterKresgeMeals()

getCarsonOakesMeals()
