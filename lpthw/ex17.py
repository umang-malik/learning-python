from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how? TRY THIS
#in_file = open(from_file)
indata = open(from_file).read()

print "This input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit REtuRN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, done."

out_file.close()
#in_file.close()


#Shortest => open(out_file,'w').write(open(in_file).read())
