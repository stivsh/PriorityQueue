import random
from .PriorityQueue import PriorityQueue

def test_without_priority_changin():
	"""test without priority changing"""
	l = [ random.randint(-200,200) for i in range(200)]
	l = list(set(l))
	random.shuffle(l)

	p=PriorityQueue()
	for i in l: p.push(i,i*10)
	assert [ sorted(l)[i] for i in range(len(l)-1,-1,-1) ] == [ p.pop()/10 for i in range(len(l))]


def test_with_priority_changin():
	"""test with priority changing"""
	l = [ random.randint(-200,200) for i in range(200)]
	l = list(set(l))
	random.shuffle(l)

	p=PriorityQueue()
	for i in l: p.push(i,i*10)

	list_with_priority = [(i,i*10) for i in l ]
	max_prior = max(l)
	#make 20 random priority chandges
	for i in range(20):
    	max_prior += 1
    	random_inx = random.randint(0, len(l)-1)
    	val = list_with_priority[random_inx]
    	list_with_priority[random_inx] = (max_prior,val[1])
    	p.push(max_prior,val[1])

	l1 = [ p.pop() for i in range(len(l))]

	l2 = [ sorted(list_with_priority,key = lambda x:x[0])[i][1] for i in range(len(l)-1,-1,-1) ]

	assert l1 == l2