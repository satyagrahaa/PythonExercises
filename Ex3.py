"""
Find top 10 most repeated words in a given text. A word is any
sequence of non-whitespace characters. Words are not case sensitive.
"""


def get_value(input):
    return input[1]


sentence = ('Do not dwell in the past do not dream of the future concentrate'
            ' the mind on the present moment')

words = sentence.split()
dic = {}

for word in words:
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

dic_set = dic.items()

print "This is your sentence: \n\t %s" % sentence
sorted_dic = sorted(dic_set, key=get_value, reverse=True)
first_elements = [x[0] for x in sorted_dic[0:10]]
print "These are the 10 most frequent words: \n\t %s" % first_elements





"""
count = 10
#solution 2:
for k, v in sorted(dic.iteritems(), key=lambda (k, v): (v, k), reverse=True):
    if count > 0:
        print k
        count -= 1
"""

"""
#solution 3:incomplete
print [k for k,v in dic.iteritems() if v == max(dic.values())]
"""
# for i in range, for indexing
# for word in words
# for i, word in enumerate(words)
# python generators
