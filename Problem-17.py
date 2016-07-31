"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
	then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
	in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
	forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
	20 letters. The use of "and" when writing out numbers is in compliance with
	British usage.
"""

# I'm doing extra work not converting this index into string lengths on the front end.

Singles = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 
			6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
Tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
Hundreds = ['Hundred']
Thousands = ['Thousand']

def find_singles(n):
	return Singles[n]

def find_tens(nn):
	TempTens, TempSingles = divmod(nn, 10)
	return Tens[TempTens - 2] + find_singles(TempSingles)

def find_hundreds(nnn):
	TempHundreds, TempRemain = divmod(nnn, 100)
    return Singles[TempHundreds] + Hundreds + find_tens(TempRemain)

def find_thousands(nnnn):
	TempThousands, TempRemain = divmod(nnnn, 1000)
	return Singles[TempThousands] + Thousands + find_hundreds(TempRemain)

def length_of_number(Number):
	LenOfNum = 0
    if 1 <= Number < 19:
        LenOfNum = find_singles(Number)
    elif 20 <= Number <= 99:
        LenOfNum = find_tens(Number)
    elif 100 <= Number <= 999:
    	LenOfNum = find_hundreds(Number)
    elif 1000 <= Number <=9999:
    	LenOfNum = find_thousands(Number)
    else:
        print("Number out of range")

# Nope. Run it like a cash register. The internet bites me.

def length_of_number(nnnn): # a function to find the length of an integer's english language equivalent.
	LenOfNum = 0
	TempNnnn = nnnn
	if 1000 <= nnnn <=9999:
		TempThousands, TempRemain = divmod(nnnn, 1000)
		LenOfNum = Singles[TempThousands]
