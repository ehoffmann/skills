"""
Use this command to compute:
python euler17.py | sed 's/[ -]//g' | tr -d '\n' | wc -c
"""

dix = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
vintes =   dix + ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

dzaine = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

centaine = [ (num + ' hundred') for num in dix  ]

def countTilHund(postfix):
	""" count until 100 is reached !! """

	for i in range (1, 100):
		if i < 20:
			print postfix + vintes[i]
		elif i < 100:
			si = str(i)
			if si[1] == '0':
				print postfix + dzaine[int(si[0])]
			else:	
				print postfix + dzaine[int(si[0])] + '-' + dix[int(si[1])]	

countTilHund('')

for i in range(1,10):
	s = dix[i] + ' hundred'
	print s
	countTilHund(s + ' and ')

print 'one thousand'


