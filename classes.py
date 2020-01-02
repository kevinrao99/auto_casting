import random

class slot():
	def __init__(self, dance_id, pos_num):
		self.dance_id = dance_id
		self.pos_num = pos_num

	def __str__(self):
		return str(self.dance_id) + ", slot " + str(self.pos_num)


class dance():
	def __init__(self, dance_id, dance_cap, arrs):
		self.ID = dance_id
		self.dance_cap = dance_cap
		self.dancer_ids = [-1 for i in range(dance_cap)]
		self.ranks = arrs # Arrays of dancer objects
		self.proposed = []

	def next_proposal(self):
		# returns the dance ID of the next person to propose to
		# this is where most of the design is going to happen
		# Current plan is to pick by 1) ranking, 2) number of dances already assigned, 3) returning or not

		# Depending on Yuri's philosophy, it may be better to propose first to someone ranked 2nd but is returning and hasnt been assigned a dance yet
	

		rank_candidates = []
		for rank in self.ranks:
			for dancer in rank:
				if not dancer.ID in self.proposed:
					rank_candidates.append(dancer)
			if len(rank_candidates) > 0:
				break

		assigned_candidates = []
		for i in range(4):
			for dancer in rank_candidates:
				if len(dancer.dances) == i:
					assigned_candidates.append(dancer)
			if len(assigned_candidates) > 0:
				break

		returning_candidates = []
		for i in [False, True]:
			for dancer in assigned_candidates:
				if dancer.returning or i:
					returning_candidates.append(dancer)
			if len(returning_candidates) > 0:
				break

		# If we cant propose any more, then so be it

		if len(returning_candidates) == 0:
			return None

		# If we have no further tiebreakers, just return a random one

		selection = returning_candidates[int(random.random() * len(returning_candidates))]
		self.proposed.append(selection.ID)

		return selection

	def remove_dancer(self, dancer_id):
		# removes a dancer, returns the index of their slot
		for i in range(len(self.dancer_ids)):
			if self.dancer_ids[i] == dancer_id:
				self.dancer_ids[i] = -1
				return i
		return -1

	def place_dancer(self, dancer_id, slot):
		assert slot.dance_id == self.ID
		assert self.dancer_ids[slot.pos_num] == -1
		self.dancer_ids[slot.pos_num] = dancer_id

	def create_slots(self):
		ans = []
		for i in range(self.dance_cap):
			temp_obj = slot(self.ID, i)
			ans.append(temp_obj)

		return ans

	def disp(self):
		for arr in self.ranks:
			for dancer in arr:
				print dancer.ID,
			print



class dancer():
	def __init__(self, info):
		# define init based on how we read data into info array
		self.willing = info[0]
		self.returning = info[1]
		self.choices = [info[2], info[3], info[4]]

		self.dance_cap = info[5]
		self.ID = info[6]

		for item in self.choices:
			try:
				self.willing.remove(item)
			except Exception, e:
				print self.ID, "Dancer has a choice not in willing"
			

		self.dances = [] # array of the slots held by this dancer

	def disp(self):
		print "ID:", self.ID
		print "Top 3 choices:", self.choices, ";  Willing:", self.willing
		print "cap:", self.dance_cap, " returning:", self.returning
		print

	def receive_proposal(self, slot):
		# Adds a proposed dance if has space, otherwise decides whether or not to evict a dance
		# returns None if had space, otherwise returns the slot not taken

		if not slot.dance_id in self.choices and not slot.dance_id in self.willing:
			return slot

		if len(self.dances) < self.dance_cap:
			self.dances.append(slot)
			return None

		# not enough space, time to evict one

		if slot.dance_id in self.willing:
			return slot

		for i in range(len(self.dances)):
			if self.dances[i].dance_id in self.willing:
				temp = self.dances[i]
				self.dances[i] = slot
				return temp

		if slot.dance_id == self.choices[2]:
			return slot

		for i in range(len(self.dances)):
			if self.dances[i].dance_id == self.choices[2]:
				temp = self.dances[i]
				self.dances[i] = slot
				return temp

		if slot.dance_id == self.choices[1]:
			return slot

		for i in range(len(self.dances)):
			if self.dances[i].dance_id == self.choices[1]:
				temp = self.dances[i]
				self.dances[i] = slot
				return temp


		print "Not supposed to be here in receive_proposal!"
		print "input was", str(slot)
		print "choices: ", self.choices
		print "willing: ", self.willing
		print "Current slots:"
		for slot_obj in self.dances:
			print "   ", str(slot_obj)
		return None



