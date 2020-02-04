import func
import pandas as pd
import numpy as np
import math


if __name__ == "__main__":
	dance_names = ['AMY WANG & KEVIN RAO', 
		'CALLIA CHUANG', 
		'EMMA ROBERTSON', 
		'GIGI ZADES & ANNABEL BAXTER', 
		'NOAH RAMOS', 
		'SARAH YOON & IFY OGU', 
		'YG OHASHI']
	func.assign_dance_ids(dance_names)
	dancers = func.read_dancer_data()

	for person in dancers:
		person.disp()



