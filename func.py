import pandas as pd
import numpy as np
import math
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

def get_dance_name(dance_id):
	if dance_id in id_to_dance:
		return id_to_dance[dance_id]
	print "Input \"", str(dance_id), "\" not a registered dance ID"
	return -1

def get_dancer_name(dancer_id):
	if dancer_id in id_to_name:
		return id_to_name[dancer_id]
	print "Input \"", dancer_id, "\" not a registered dancer ID"
	return -1

def get_dancer_id(name):
	if name in name_to_id:
		return name_to_id[name]
	print "Input \"", name, "\" not a registered dancer name"
	return -1

def name_dict():
	return name_to_id

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
		name_to_id[id_dat[i][0].strip()] = id_as_int
		id_to_name[id_as_int] = id_dat[i][0].strip()

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


def read_choreo_data(dancers): # Figure out how to do choreographer data
	# Make sure each number only appears once in each choreographer's sheet

	filenames = ["data/alaisha_fall_2019.csv", 
		"data/lani_fall_2019.csv",
		"data/linda_fall_2019.csv",
		"data/marisa_fall_2019.csv",
		"data/mo_fall_2019.csv",
		"data/nina_fall_2019.csv",
		"data/sheila_fall_2019.csv",
		"data/yg_fall_2019.csv"]

	dance_caps = [30, 31, 32, 33, 34, 35, 36, 37]

	dances = []

	for f in range(len(filenames)):
		dance_dat = np.array(pd.read_csv(filenames[f]))
		arrs = [[], [], [], []]
		track = []

		for i in range(4):
			for j in range(len(dance_dat)):
				if math.isnan(dance_dat[j][i]):
					break
				else:
					val = int(dance_dat[j][i])
					if val in track:
		#				print val, "appears twice for dance", f, "!"
						pass
					else:
						track.append(val)
						for dancer in dancers:
							if dancer.ID == val:
								arrs[i].append(dancer)
								break

		temp_obj = classes.dance(f, dance_caps[f], arrs)
		dances.append(temp_obj)

	return dances

def write_cast_list(dances, filename = "data/cast_list.csv"):



	name_list = []
	for i in range(len(dances)):
		name_list.append([])
		name_list[i].append(get_dance_name(dances[i].ID))
		for dancer_id in dances[i].dancer_ids:
			temp = get_dancer_name(dancer_id)
			if temp != -1:
				name_list[i].append(temp)

	for i in range(len(name_list)):
		name_list[i] = name_list[i][0:1] + sorted(name_list[i][1:])

	max_len = 0
	for dance_list in name_list:
		max_len = max(max_len, len(dance_list))

	for dance_list in name_list:
		while len(dance_list) < max_len:
			dance_list.append("")


	name_list = np.array(name_list)
	for i in range(len(name_list)):
		name_list[i] = np.array(name_list[i])

	print name_list.shape
	name_list = np.transpose(name_list)
	print name_list.shape
	
	print len(name_list[0]), name_list[0]

	pd.DataFrame(name_list).to_csv(filename)













