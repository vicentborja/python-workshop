import sys

try:
	f = open('integers.txt')
	s = f.readline()
	i = int(s.strip())

except IOError as (errno, strerror):
	print("I/O eror({0}): {1}".format(errno, strerror))
except ValueError:
	print("No valid integer in line")
except:
	print "Unexpected error:", sys.exc_info()[0]
	raise
finally:
	print("There may or may not have been an exception")
