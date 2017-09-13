import argparse

parser = argparse.ArgumentParser(description='Compute inverse of string.')
parser.add_argument('input', type=str, help='an string')

args = parser.parse_args()

def inverse(l):
	"""
	Given a string l, return its inverse.

	e.g. 'abc' => 'cba'

	Big O(n), linear since each element in 
	string needs to be visited once.
	"""
	l_copy = l

	res = ''
	for x in l:
		res += l_copy[-1]
		l_copy = l_copy[:-1]
	return res


print( inverse(args.input) )