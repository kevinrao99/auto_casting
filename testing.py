import func
import pandas as pd
import numpy as np
import math


if __name__ == "__main__":
	dance_names = ['Alaisha Sharma', 
		'Lani + Nina U.', 
		'Linda Qin', 
		'Marisa + Maureen', 
		'Maureen', 
		'Nina C. ft. Daniel', 
		'Sheila De La Cruz', 
		'YG']
	func.assign_dance_ids(dance_names)
	func.read_dancer_data()

	print func.name_dict()

	manual_cast = np.array(pd.read_csv("data/manual_cast.csv"))
#	print manual_cast

	for i in range(len(dance_names)):
		for j in range(len(manual_cast)):
			if not type(manual_cast[j][i]) == type("hello!"):
				break
			manual_cast[j][i] = manual_cast[j][i].strip()
			dancer_id = func.get_dancer_id(manual_cast[j][i])
			if dancer_id == -1:
				continue


