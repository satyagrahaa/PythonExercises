def pm_to_mil(time):

    return time + 12


inp = raw_input('Enter time in AM/PM format: ')

#strip instead of slice
min_sec = inp[3:-2]
hour = int(inp[:2])

if 'P' in inp:
    x = str(pm_to_mil(hour))
    print 'Military time: %s:%s' % (x, min_sec)
if 'A' in inp:
    print 'Military time: ' + inp[:-2]
