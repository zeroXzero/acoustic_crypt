KEY=['Q','A','Z','W','S','X','E','D','C','R','F','V','T',
'G','B','Y','H','N','U','J','M','I','K','O','L','P']

ADJ={
 		'Q':['Q','W','S','A'],
 		'A':['A','Q','W','S','Z'],
 		'Z':['Z','A','S','X'],
 		'W':['W','Q','A','S','D','E'], 
 		'S':['S','Q','A','Z','X','D','E','W'], 
 		'X':['X','Z','A','S','D','C'],
 		'E':['E','W','S','D','F','R'],
 		'D':['D','E','W','S','X','C','F','R'],
 		'C':['C','X','D','F','V'],
 		'R':['R','E','D','F','G','T'],
 		'F':['F','R','E','D','C','V','G','T'],
 		'V':['V','C','D','F','G','B'],
 		'T':['T','R','F','G','H','Y'],
 		'G':['G','T','R','F','V','B','H','Y'],
 		'B':['B','V','G','H','N'],
 		'Y':['Y','T','G','H','J','U'],
 		'H':['H','Y','T','G','B','N','J','U'],
 		'N':['N','B','H','J','M'],
 		'U':['U','Y','H','J','K','I'],
 		'J':['J','U','Y','H','N','M','K','I'],
 		'M':['M','N','J','K'],
 		'I':['I','U','J','K','L','O'],
 		'K':['K','I','U','J','M','L','O'],
 		'O':['O','I','K','L','P'],
 		'L':['L','O','I','K','P'],
 		'P':['P','O','L'],
	 }

NEAR={
  		'Q':['Q','W','A','E','S','Z','D','X'],
  		'A':['A','Q','Z','W','S','X','E','D'],
  		'Z':['Z','Q','A','W','S','X','E','D','C'], 
  		'W':['W','Q','A','Z','S','X','E','D','C','R','F'], 
  		'S':['S','Q','A','Z','W','X','E','D','C','R','F'],
  		'X':['X','Q','A','Z','W','S','E','D','C','F','V'],
  		'E':['E','Q','A','Z','W','S','X','D','C','R','F','V','T','G'],
  		'D':['D','Q','A','Z','W','S','X','E','C','R','F','V','T','G'],
  		'C':['C','W','S','Z','E','S','X','R','D','F','V','T','G','B'],
  		'R':['R','W','S','X','E','D','C','F','V','T','G','B','Y','H'],
  		'F':['F','W','S','X','E','D','C','R','V','T','G','Y','H','B'],
  		'V':['V','E','D','X','R','F','C','T','G','B','Y','H','N'],
  		'T':['T','E','D','C','R','F','V','G','Y','H','B','U','J','N'],
  		'G':['G','E','D','C','R','F','V','T','B','Y','H','N','U','J'],
  		'B':['R','D','C','T','F','V','G','Y','H','N','U','J','M'],
  		'Y':['Y','R','F','V','T','G','B','U','H','I','J','N'],
  		'H':['H','R','F','V','T','G','B','Y','U','J','N','I','K','M'],
  		'N':['N','T','F','V','Y','G','B','H','U','J','M','I','K'],
  		'U':['U','T','G','B','Y','H','N','I','J','O','K','M','L'],
  		'J':['J','T','G','B','Y','H','U','N','I','K','M','O','L'],
  		'M':['M','Y','H','B','U','J','N','I','K','O','L'],
  		'I':['I','Y','H','N','U','J','M','O','K','P','L'],
  		'K':['K','Y','H','N','U','J','M','I','O','L','P'],
  		'O':['O','U','J','M','I','K','P','L'],
  		'L':['L','U','J','N','I','K','M','O','P'],
  		'P':['P','I','J','M','I','K','O','L']
	 }

DIST={
  		'Q':['B','C','F','G','H','I','J','K','L','M','N','O','P','R','T','U','V','Y'], 
  		'A':['B','C','F','G','H','I','J','K','L','M','N','O','P','R','T','U','V','Y'],
  		'Z':['B','F','G','H','I','J','K','L','M','N','O','P','R','T','U','V','Y'],
  		'W':['B','G','H','I','J','K','L','M','N','O','P','T','U','V','Y'],
  		'S':['B','G','H','I','J','K','L','M','N','O','P','T','U','V','Y'],
  		'X':['B','G','H','I','J','K','L','M','N','O','P','R','T','U','Y'],
  		'E':['B','H','I','J','K','L','M','N','O','P','U','Y'],
  		'D':['B','H','I','J','K','L','M','N','O','P','U','Y'],
  		'C':['A','H','I','J','K','L','M','N','O','P','Q','U','Y'],
  		'R':['A','I','J','K','L','M','N','O','P','Q','U','Z'],
  		'F':['A','I','J','K','L','M','N','O','P','Q','U','Z'],
  		'V':['A','I','J','K','L','M','O','P','Q','S','U','W','Z'],
  		'T':['A','I','K','L','M','O','P','Q','S','W','X','Z',],
  		'G':['A','I','K','L','M','O','P','Q','S','W','X','Z'],
  		'B':['A','B','E','I','K','L','O','P','Q','S','W','X','Z'],
  		'Y':['A','C','D','E','K','L','M','O','P','Q','S','W','X','Z'],
  		'H':['A','C','D','E','L','O','P','Q','S','W','X','Z'],
  		'N':['A','C','D','E','L','O','P','Q','R','S','W','X','Z'],
  		'U':['A','C','D','E','F','P','Q','R','S','V','W','X','Z'],
  		'J':['A','C','D','E','F','P','Q','R','S','V','W','X','Z'],
  		'M':['A','C','D','E','F','G','P','Q','R','S','T','V','W','X','Z'],
  		'I':['A','B','C','D','E','F','G','Q','R','S','T','V','W','X','Z'],
  		'K':['A','B','C','D','E','F','G','Q','R','S','T','V','W','X','Z'],
  		'O':['A','B','C','D','E','F','G','H','N','Q','R','S','T','V','W','X','Y','Z'],
  		'L':['A','B','C','D','E','F','G','H','Q','R','S','T','V','W','X','Y','Z'],
  		'P':['A','B','C','D','E','F','G','H','N','Q','R','S','T','U','V','W','X','Y','Z']
	}

