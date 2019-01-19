from bs4 import BeautifulSoup
import requests
import re

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

b = meals.split("Lunch")
breakfast = b[0]
l = b[1].split("Dinner")
lunch = l[0]
dinner = l[1]
ln = dinner.split("Late Night")
if len(ln) > 1:
    lateNight = ln[1]
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

endBreakfastWord = breakfastList[len(breakfastList)-1]
endBreakfastIndex = textcontent.index(endBreakfastWord) + 1
endBreakfast = textcontent[0:endBreakfastIndex]

startLunchIndex = endBreakfastIndex
endLunchWord = lunchList[len(lunchList)-1]
endLunchIndex = textcontent.index(endLunchWord) + 1
endLunch = textcontent[startLunchIndex:endLunchIndex]

startDinnerIndex = endLunchIndex
endDinnerWord = dinnerList[len(dinnerList)-1]
endDinnerIndex = textcontent.index(endDinnerWord) + 1
endDinner = textcontent[startDinnerIndex:endDinnerIndex]

if lateNightHappening:
	startLateNightIndex = endDinnerIndex
	endLateNightWord = LateNightList[len(dinnerList)-1]
	endLateNightIndex = textcontent.index(endLateNightWord) + 1
	endLateNight = textcontent[startLateNightIndex:endLateNightIndex]

print(endBreakfast)

print(endLunch)

print(endDinner)

if lateNightHappening:
	print(lateNightHappening)

bf = open("breakfast.txt", "w")
lun = open("lunch.txt", "w")
din = open("dinner.txt", "w")
if lateNightHappening:
	late = open("lateNight.txt", "w")

for i in range(len(endBreakfast)):
	if(i < len(endBreakfast)-1):
		bf.write(endBreakfast[i] + ", ")
	else:
		bf.write(endBreakfast[i] + ".")

for i in range(len(endLunch)):
	if(i < len(endLunch)-1):
		lun.write(endLunch[i] + ", ")
	else:
		lun.write(endLunch[i] + ".")

for i in range(len(endDinner)):
	if(i < len(endDinner)-1):
		din.write(endDinner[i] + ", ")
	else:
		din.write(endDinner[i] + ".")

if lateNightHappening:
	for i in range(len(endLateNight)):
		if(i < len(endLateNight)-1):
			late.write(endLateNight[i] + ", ")
		else:
			late.write(endLateNight[i] + ".")


