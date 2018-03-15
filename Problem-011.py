class Problem_011:
	"""
	In the 20x20 grid below, four numbers along a diagonal line have been marked in red.

	08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
	49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
	81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
	52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
	22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
	24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
	32 98 81 28 64 23 67 10[26]38 40 67 59 54 70 66 18 38 64 70
	67 26 20 68 02 62 12 20 95[63]94 39 63 08 40 91 66 49 94 21
	24 55 58 05 66 73 99 26 97 17[78]78 96 83 14 88 34 89 63 72
	21 36 23 09 75 00 76 44 20 45 35[14]00 61 33 97 34 31 33 95
	78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
	16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
	86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
	19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
	04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
	88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
	04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
	20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
	20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
	01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

	The product of these numbers is 26 x 63 x 78 x 14 = 1788696.

	What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20x20 grid?
	"""

	row_01 = [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8]
	row_02 = [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0]
	row_03 = [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65]
	row_04 = [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91]
	row_05 = [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80]
	row_06 = [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50]
	row_07 = [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70]
	row_08 = [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21]
	row_09 = [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72]
	row_10 = [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95]
	row_11 = [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92]
	row_12 = [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57]
	row_13 = [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58]
	row_14 = [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40]
	row_15 = [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66]
	row_16 = [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69]
	row_17 = [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36]
	row_18 = [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16]
	row_19 = [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54]
	row_20 = [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]

	full_grid = [row_01, row_02, row_03, row_04, row_05, row_06, row_07, row_08, row_09, row_10, row_11, row_12, row_13, row_14, row_15, row_16, row_17, row_18, row_19, row_20]

	def search_all_directions(self, n):
		"""
		Method to find the largest product of adjacent integers in a grid
		Arguments: <integer> n - the number of adjacent grid elements to multiply
		Returns: <integer> The largest product found
		"""

		largest_product = self.find_largest_horizontal_product(n)
		largest_product = self.find_largest_vertical_product(n)
		largest_product = self.find_largest_vertical_product(n)
		return largest_product

	def find_largest_horizontal_product(self, n):
		"""
		Method to find the largest product of horiontally adjacent integers in a grid
		Arguments: <integer> n - the number of adjacent grid elements to multiply
		Returns: <integer> The largest product found
		"""
		largest_product = 0
		for i in range(0, len(self.full_grid)):
			for j in range(0, len(self.row_01)-n):
				candidate = self.product_of_horizontal_adjacent(i, j, n)
				if candidate > largest_product:
					largest_product = candidate
		return largest_product

	def product_of_horizontal_adjacent(self, row, start, elements):
		"""
		Method to get the product of n elements in a row, starting with element
		Arguments: <integer> row, <integer> start, <integer> elements
		"""
		product = 1
		for i in range(0, elements):
			product *= self.full_grid[row][start+i]
		return product

	def find_largest_vertical_product(self, n):
		"""
		Method to find the largest product of vertically adjacent integers in a grid
		Arguments: <integer> n - the number of adjacent grid elements to multiply
		Returns: <integer> The largest product found
		"""
		largest_product = 0
		return

	def find_largest_forward_diagonal_product(self, n):
		"""
		Method to find the largest product of diagonally adjacent integers in a grid
		Arguments: <integer> n - the number of adjacent grid elements to multiply
		Returns: <integer> The largest product found
		"""
		largest_product = 0
		return

	def find_largest_backward_diagonal_product(self, n):
		"""
		Method to find the largest product of diagonally adjacent integers in a grid
		Arguments: <integer> n - the number of adjacent grid elements to multiply
		Returns: <integer> The largest product found
		"""
		largest_product = 0
		return

	def horz_srch(arr): # where arr is an array
		prod = 0
		largest = 0
		for e in range(len(arr)): # this goes through each line
			box_start = 0 # reset the start place to [0]
			for i in range(len(arr[e])-4): # this goes through each element
				prod = (arr[e][box_start] * arr[e][box_start+1] * arr[e][box_start+2] * arr[e][box_start+4])
				if prod > largest:
					largest = prod
				box_start += 1 # move the box!
		for f in range(len(arr)-3): # this is for vertical checks.
			box_start = 0
			for j in range(len(arr[f])):
				prod = (arr[f][box_start] * arr[f+1][box_start] * arr[f+2][box_start] * arr[f+3][box_start])
				if prod > largest:
					largest = prod
				box_start += 1
		for g in range(len(arr)-3):
			box_start = 0
			for k in range(len(arr[g])-4):
				prod = (arr[g][box_start] * arr[g+1][box_start+1] * arr[g+2][box_start+2] * arr[g+3][box_start+3])
				if prod > largest:
					largest = prod
				box_start += 1
			box_start = 3
			for m in range(3, len(arr)):
				prod = (arr[g][box_start] * arr[g+1][box_start-1] * arr[g+2][box_start-2] * arr[g+3][box_start-3])
				if prod > largest:
					largest = prod
				box_start += 1
		return largest

if __name__ == "__main__":
	import sys
	solver = Problem_011()
	arg = sys.argv[1]
	print("The largest product of four adjacent numbers is {}.".format(solver.horz_srch(solver.full_grid)))