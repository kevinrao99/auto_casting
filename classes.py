

class slot():
	def __init__(self, dance_id, pos_num):
		self.dance_id = dance_id
		self.pos_num = pos_num


class dance():
	def __init__(self, dance_cap, arr1, arr2, arr3, arr4):
		self.dance_cap = dance_cap
		self.dancer_ids = [0 for i in range(dance_cap)]
		self.rank_1 = arr1;
		self.rank_2 = arr2;
		self.rank_3 = arr3;
		self.rank_4 = arr4;


class dancer():
	def __init__(self, info):
		# define init based on how we read data into info array
		
