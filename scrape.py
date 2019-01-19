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

print("Breakfast:")
print(breakfastList)

print()

print("Lunch:")
print(lunchList)

print()

print("Dinner:")
print(dinnerList)

print()

if lateNightHappening:
    print("Late Night:")
    print(lateNightList)


