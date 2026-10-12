def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	
	means = []
	if mode == 'row':
		row_sum = 0
		for row in matrix:
			for element in row:
				row_sum += element
			row_avg = row_sum / len(row)
			means.append(row_avg)
			row_sum = 0
	else:
		col_sum = 0
		for j in range(len(matrix[0])):
			for i in range(len(matrix)):
				col_sum += matrix[i][j]
			col_avg = col_sum / len(matrix)
			means.append(col_avg)
			col_sum = 0					


	return means