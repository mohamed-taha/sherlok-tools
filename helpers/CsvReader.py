 #-*- coding: utf-8 -*-
import csv
import sys
import codecs

class CsvReader:
	"""docstring for CsvReader
	   read dataset csv files, extract data and transform it to convenient form """
	def __init__(self, file_name):
		self.file_name = file_name

	# read the file	
	def read(self):
		try:
			#input_file = open(self.file_name, 'rb', 'utf-8')
			reader = csv.reader(codecs.open(self.file_name, 'rb', 'utf-32'))
		except IOError, e:
			print "Error: Failed to open the input file"
			exit(1)
		try:			
			for row in reader:
				print "%s: %s" %(row[0], row[1])
		except csv.Error, e:
			sys.exit("file %s, line %d : %s" %(self.file_name, reader.line_num, e))		
		
		input_file.close()


c_reader = CsvReader('../unWeightedOMLexicon.csv')
c_reader.read()							

		

