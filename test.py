from selenium import webdriver
from lxml import etree
import unicodedata
import csv

team_dict = {}

# Selenium

chrome_path = r"C:\Users\Oscar Tu\Desktop\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)

# Print teams


# TODO: parse roster table to get jersey numbers and to print starting 5
def make_team(year, team):
	driver.get("http://www.basketball-reference.com")
	driver.find_element_by_xpath("""//*[@id="header"]/div[3]/form/div/div/input[2]""").send_keys(year + " " + team)
	driver.find_element_by_xpath("""//*[@id="header"]/div[3]/form/input[1]""").click()
	csv_per_game = driver.find_element_by_xpath("""//*[@id="div_per_game"]""")
	
	cpg = unicodedata.normalize('NFKD', csv_per_game.text).encode('ascii','ignore')

	# Lines of player stat per game with first line being category
	cpg_lines_list = cpg.splitlines()
	print cpg_lines_list
	# Print out list of all players ranked by stats
	# len(cpg_lines_list) returns list of all players
	for i in range(1,len(cpg_lines_list)):
		player_stat_list = cpg_lines_list[i].split()
		
		# Algorithm to determine which elements to print for just the name due to
		# METTA WORLD PEACE being 3 words
		x = 1
		print ("Rank " + player_stat_list[0] + ":"),
		while (not is_number(player_stat_list[x])):
			print (player_stat_list[x]),
			x += 1
		field_goal_pct = player_stat_list[x+6] # Interesting stats, might not be useful to calculate
		three_point_pct = player_stat_list[x+9]

		# Important stats here

		effective_field_goal_pct = player_stat_list[x+13]
		free_throw_pct = player_stat_list[x+16]
		pts = player_stat_list[x+25] # Doesn't work for last person on roster
		print ("with " + pts + " points, "  + effective_field_goal_pct + " eFG% and " + free_throw_pct + " FT%.")


def is_number(str):
	try: 
		float(str)
		return True
	except ValueError:
		return False


#def make_stats():
	


def main():
	#print 'This is a test NBA simulator. Please enter in the season year (2017 for the 2016-2017 season) followed by the full team name for the two teams you wish to pit against each other.' 
	#season1 = raw_input('First Team\'s year: ')
	#team_name1 = raw_input('First Team\'s Name: ')
	#season2 = raw_input('Second Team\'s year: ')
	#team_name2 = raw_input('Second Team\'s Name: ')
	season1 = '2010'
	team_name1 = 'lakers'
	make_team(season1, team_name1)
	#make_team(season2, team_name2)

if __name__ == "__main__":
	main()