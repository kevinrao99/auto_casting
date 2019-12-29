import pandas as pd
import numpy as np
import classes

global dance_to_id
global name_to_id
global id_to_dance
global id_to_name

def get_dance_id(name): # given the dance name returns an integer corresponding to the dance's dance_to_id
	if name in dance_to_id:
		return dance_to_id[name]
	print "Input \"", name, "\" not a registered dance name"
	return -1

def assign_dance_ids(dance_names):
	global dance_to_id
	global id_to_dance
	dance_to_id = dict([])
	id_to_dance = dict([])
	for i in range(len(dance_names)):
		dance_to_id[dance_names[i]] = i
		id_to_dance[i] = dance_names[i]

	for key in id_to_dance:
		print key, ":", id_to_dance[key]

	print


def read_dancer_data(filename = "data/dat_2019_fall.csv"): # reads in csv file of audition form responses
	# edit appropriately based on the format of the audition form
	global id_to_name
	global name_to_id

	all_dat = np.array(pd.read_csv(filename))


	id_dat = all_dat[:, [4, 21]] # We assume all ids are cleaned to unique integers
	name_to_id = dict([])
	id_to_name = dict([])
	for i in range(len(id_dat)):
		try:
			id_as_int = int(id_dat[i][1])
		except Exception, e:
			print "Not all ids are ints:", id_dat[i][1]
			continue
		name_to_id[id_dat[i][0]] = id_as_int
		id_to_name[id_as_int] = id_dat[i][0]

	# select columns for willing to work, danced with expressions, 1 2 3 choices, dance cap, dancer id, times
	relevant_dat = all_dat[:, [12, 13, 14, 15, 16, 17, 21, 22, 23, 24, 25, 26, 27, 28]]

	# Ignore time available for now

	dancers = []

	for i in range(len(relevant_dat)):
		info_arr = []

		work_arr = relevant_dat[i][0].split(", ")
		work_arr = list(map(get_dance_id, work_arr))
		info_arr.append(work_arr) # list of choreographers you're willing to work with

		info_arr.append(relevant_dat[i][1] == "Yes") # whether you've danced with expressions

		info_arr.append(get_dance_id(relevant_dat[i][2]))
		info_arr.append(get_dance_id(relevant_dat[i][3]))
		info_arr.append(get_dance_id(relevant_dat[i][4])) # First, second, third choice IDs

		info_arr.append(int(relevant_dat[i][5])) # dance cap

		info_arr.append(int(relevant_dat[i][6])) # dancer audition number, to be used as dancer ID

		###########

		# We ignore times for now

		###########

		temp_dancer = classes.dancer(info_arr)
		dancers.append(temp_dancer)

	return dancers


def read_choreo_data(): # Figure out how to do choreographer data
	return 1















