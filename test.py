from selenium import webdriver
from lxml import etree
import unicodedata

team1_fg_array = {}
team2_fg_array = {}

# Selenium

chrome_path = r"C:\Users\Oscar Tu\Desktop\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)

driver.get("http://www.basketball-reference.com")
driver.find_element_by_xpath("""//*[@id="header"]/div[3]/form/div/div/input[2]""").send_keys("2015 Bulls")
driver.find_element_by_xpath("""//*[@id="header"]/div[3]/form/input[1]""").click()
csv_per_game = driver.find_element_by_xpath("""//*[@id="div_per_game"]""")

# Get stats

cpg = unicodedata.normalize('NFKD', csv_per_game.text).encode('ascii','ignore')
big_list = cpg.split()
name_index_locator = 29

print ("Your starting lineup is: \n" + big_list[name_index_locator] + " " + big_list[name_index_locator+1]),
for i in range(2,6):
	 print (", " + big_list[i*name_index_locator] + " " + big_list[(i*name_index_locator)+1]),

#


def make_team(year, team, team_website):
	print "Your starting lineup for the " + year + " " + team + " is: "  

'''def main():
	print 'This is a test NBA simulator. Please enter in the season year (2017 for the 2016-2017 season) followed by the full team name for the two teams you wish to pit against each other.' 
	season1 = raw_input('First Team\'s year: ')
	team_name1 = raw_input('First Team\'s Name: ')
	stat_website1 = 'http://www.basketball-reference.com/search/search.fcgi?hint=&search=' + season1 + '+' + team_name1 + '&pid='
	season2 = raw_input('Second Team\'s year: ')
	team_name2 = raw_input('Second Team\'s Name: ')
	stat_website2 = 'http://www.basketball-reference.com/search/search.fcgi?hint=&search=' + season2 + '+' + team_name2 + '&pid='

	make_team(season1, team_name1, stat_website1)
	make_team(season2, team_name2, stat_website2)

if __name__ == "__main__":
	main()'''