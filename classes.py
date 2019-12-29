

class slot():
	def __init__(self, dance_id, pos_num):
		self.dance_id = dance_id
		self.pos_num = pos_num


class dance():
	def __init__(self, dance_cap, arr1, arr2, arr3, arr4):
		self.dance_cap = dance_cap
		self.dancer_ids = [-1 for i in range(dance_cap)]
		self.rank_1 = arr1;
		self.rank_2 = arr2;
		self.rank_3 = arr3;
		self.rank_4 = arr4;
		self.proposed = []

	def next_proposal(self):
		# returns the dance ID of the next person to propose to
		# this is where most of the design is going to happen
		# Current plan is to pick by 1) ranking, 2) number of dances already assigned, 3) returning or not

		# Based on Yuri's philosophy, it may be better to propose first to someone ranked 2nd but is returning and hasnt been assigned a dance yet
		
		

		return 1

	def remove_dancer(self, dancer_id):
		for i in range(len(self.dancer_ids)):
			if self.dancer_ids[i] == dancer_id:
				self.dancer_ids[i] = -1
				return i
		return -1



class dancer():
	def __init__(self, info):
		# define init based on how we read data into info array
		self.willing = info[0]
		self.returning = info[1]
		self.choices = [info[2], info[3], info[4]]
		self.dance_cap = info[5]
		self.ID = info[6]
		self.dances = []

	def disp(self):
		print "ID:", self.ID
		print "Top 3 choices:", self.choices, ";  Willing:", self.willing
		print "cap:", self.dance_cap, " returning:", self.returning
		print

	def recieve_proposal(self, dance_id):
		return 1

