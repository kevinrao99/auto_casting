import func
import classes
import random



def assign_slot(dance_slot):
	# Makes proposal and gives the slot to a dancer
	# If doing so frees a different slot, recursively reassignes that slot

	#print "Assigning :", str(dance_slot)

	proposee = dances[dance_slot.dance_id].next_proposal()

	if proposee is None:
	#	print "Out of proposees!"
		return None # We can ignore this return value because theres never any reason to propose to someone twice

	proposal_result = proposee.receive_proposal_edc(dance_slot)
	# The above line can also be receive_proposal_smm, which uses stable marriage matching theory to receive proposals. See dancer class for more

	if proposal_result is None:
	#	print "Success!"
		dances[dance_slot.dance_id].place_dancer(proposee.ID, dance_slot)
		return None
	elif proposal_result.dance_id == dance_slot.dance_id:
		assert proposal_result.pos_num == dance_slot.pos_num
	#	print "Bounced back"
		assign_slot(proposal_result)
	else:
	#	print "Evicted :", str(proposal_result)
		dances[proposal_result.dance_id].remove_dancer(proposee.ID)
		dances[dance_slot.dance_id].place_dancer(proposee.ID, dance_slot)
		assign_slot(proposal_result)






if __name__ == "__main__":
	global dances
	global dancers
	global all_slots

	dance_names = ['AMY WANG & KEVIN RAO', 
		'CECLEY HILL', 
		'EMMA ROBERTSON', 
		'GIGI ZADES & ANNABEL BAXTER', 
		'NOAH RAMOS',
		'SARAH YOON & IFY OGU',
		'YG OHASHI']
	func.assign_dance_ids(dance_names)


	dancers = func.read_dancer_data()
	dances = func.read_choreo_data(dancers)

	all_slots = []

	for dance in dances:
		temp = dance.create_slots()
		for slot in temp:
			all_slots.append(slot)

	

	while len(all_slots) > 0:
		assign_index = int(random.random() * len(all_slots))
		assigning = all_slots.pop(assign_index)
		assign_result = assign_slot(assigning)


	for dance in dances:
		print func.get_dance_name(dance.ID), " : ",
		demo = [0, 0, 0, 0]
		for num in dance.dancer_ids:
			if num == -1:
				continue
			for i in range(len(dance.ranks)):
				for dancer in dance.ranks[i]:
					if dancer.ID == num:
						demo[i] += 1

		print demo[0] + demo[1] + demo[2] + demo[3], " dancers"
		print "    ", demo[0], " Rank 1 dancers"
		print "    ", demo[1], " Rank 2 dancers"
		print "    ", demo[2], " Rank 3 dancers"
		print "    ", demo[3], " Rank 4 dancers"


	num_dances = [0, 0, 0, 0]
	for dancer in dancers:
		num_dances[len(dancer.dances)] += 1

	print
	for i in range(len(num_dances)):
		print num_dances[i], " dancers got", i, "dances"

	choice_cts = [0, 0, 0]
	slack_cts = [0, 0, 0, 0]
	for dancer in dancers:
		for assigned_dance in dancer.dances:
			for i in range(len(dancer.choices)):
				if assigned_dance.dance_id == dancer.choices[i]:
					choice_cts[i] += 1

		slack_cts[dancer.dance_cap - len(dancer.dances)] += 1

	print
	print choice_cts[0], "dancers got their first choice"
	print choice_cts[1], "dancers got their second choice"
	print choice_cts[2], "dancers got their third choice"

	print
	print slack_cts[0], "dancers got full dances"
	print slack_cts[1], "dancers got one less dance than their max"
	print slack_cts[2], "dancers got two less dances than their max"
	print slack_cts[3], "dancers got three less dances than their max"
	print "\n \n"

	func.write_cast_list(dances)

	for dance in dances:
		times_dict = dict([])
		day_names = ["Mon ", "Tues ", "Wed ", "Thurs ", "Fri ", "Sat ", "Sun "]

		for dancer_id in dance.dancer_ids:
			if dancer_id == -1:
				continue

			dancer_obj = None
			for temp_obj in dancers:
				if temp_obj.ID == dancer_id:
					dancer_obj = temp_obj
					break

			if dancer_obj is None:
				print dancer_id, "NOT FOUND IN DANCERS!!"
				continue

			for j in range(len(dancer_obj.times_arr)):
				times_as_arr = dancer_obj.times_arr[j].split(", ")
				for time_str in times_as_arr:
					dict_key = day_names[j] + time_str
					if dict_key in times_dict:
						times_dict[dict_key] += 1
					else:
						times_dict[dict_key] = 1

		availability_arr = []
		for dict_key in times_dict:
			availability_arr.append((times_dict[dict_key], dict_key))

		availability_arr.sort(reverse = True)

		print func.get_dance_name(dance.ID), " top times : "
		for i in range(5):
			(a, b) = availability_arr[i]
			print "    ", b, "  works for", a, "people"
		print

	for dance in dances:
		print func.get_dance_name(dance.ID), "one to one matches:"
		for dancer in dance.ranks[0]:
			if dancer.choices[0] == dance.ID:
				print "     ", func.get_dancer_name(dancer.ID)
		print











