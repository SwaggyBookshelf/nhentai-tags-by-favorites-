import pickle
import csv

input_file = "tagsfavorites"
output_file = "raw_output"

savedfile = open(input_file,"rb")
tagdictionary = pickle.load(savedfile)
savedfile.close()

with open(output_file+".csv", "w+") as output:
    writer = csv.writer(output)
    for key, value in tagdictionary.items():
        writer.writerow([key+";"+str(value)])
