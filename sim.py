from selenium import webdriver
from lxml import etree
import unicodedata
import csv
import random # for chance

# Player class
import player

games_to_simulate = 100

team_dict = {}

# Selenium

chrome_path = r"C:\Users\Oscar Tu\Desktop\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)

# Print jersey numbers
def jersey_nums(year, team):
	numbers = driver.find_element_by_xpath("""//*[@id="div_roster"]""")
	numbers_list = unicodedata.normalize('NFKD', numbers.text).encode('ascii','ignore').splitlines()

	for i in numbers_list:
		print i

def make_team(year, team):
	driver.get("http://www.basketball-reference.com")
	driver.find_element_by_xpath("""//*[@id="header"]/div[3]/form/div/div/input[2]""").send_keys(year + " " + team)
	driver.find_element_by_xpath("""//*[@id="header"]/div[3]/form/input[1]""").click()
	csv_per_game = driver.find_element_by_xpath("""//*[@id="div_per_game"]""")
	cpg = unicodedata.normalize('NFKD', csv_per_game.text).encode('ascii','ignore')
	cpg_lines_list = cpg.splitlines()

	jersey_nums(year, team)
	print

	print "Here is your starting line up for the " + year + " " + team + ": "
	print

	# Print out list of all players ranked by stats
	# len(cpg_lines_list) returns list of all players
	for i in range(1,6):
		player_stat_list = cpg_lines_list[i].split()
		
		# Algorithm to determine which elements to print for just the name due to
		# METTA WORLD PEACE being 3 words
		x = 1
		
		while (not is_number(player_stat_list[x])):
			print (player_stat_list[x]),
			x += 1
		field_goal_pct = player_stat_list[x+6] # Interesting stats, might not be useful to calculate
		three_point_pct = player_stat_list[x+9]

		# Important stats here
		try:
			effective_field_goal_pct = player_stat_list[x+13]
			free_throw_pct = player_stat_list[x+16]
			pts = player_stat_list[x+25] # Doesn't work for last person on roster
			print ("with " + pts + " points, " + effective_field_goal_pct + " eFG%, and " + free_throw_pct + " FT%.")
		except IndexError as e:
			pts = "No data available"
			print ("with " + effective_field_goal_pct + " eFG% and " + free_throw_pct + " FT%.")

	
def is_number(str):
	try: 
		float(str)
		return True
	except ValueError:
		return False


# Will need to store player statistics in dictionaries

def simulate(team1, team2):

	games = 0

	score1 = 0
	score2 = 0

	while (games < games_to_simulate):
		for player in team1:
			player[field_goal_attempts] * player[field_goal_percentage]

	


def main():
	#print 'This is a test NBA simulator. Please enter in the season year (2017 for the 2016-2017 season) followed by the full team name for the two teams you wish to pit against each other.' 
	#season1 = raw_input('First Team\'s year: ')
	#team_name1 = raw_input('First Team\'s Name: ')
	#season2 = raw_input('Second Team\'s year: ')
	#team_name2 = raw_input('Second Team\'s Name: ')
	season1 = '2015'
	team_name1 = 'warriors'
	make_team(season1, team_name1)
	#make_team(season2, team_name2)

if __name__ == "__main__":
	main()