f = open("scores.txt")
content = f.readlines()
#turn f into strings
# note that content is a list of each line that still has the newlines at the end

f.close()
#close the folder/file

all_ratings = {}
#create new dict

for line in content:
	split_line = line.split(":")
	#split the line at :, making split_line a list of two items where what was on the left of the colon is the first item in the list and the stuff on the right is the second item on the list

	all_ratings[split_line[0]] = split_line[1].strip("\n")
	#add to the dict with key is split_line[0] and value is split_line[1] stripped of the "\n"

for key, value in sorted(all_ratings.iteritems()):
	#sorting the all_ratings dict and printing it line by line
	print "Restaurant '%s' is rated at '%s'." % (key, value)

"""
split each item in the content list at the colon => tuple or list of two items
assign it to a dictionary with the first one as a key and the second one as value
"""