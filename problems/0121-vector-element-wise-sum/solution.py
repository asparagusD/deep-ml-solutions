def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	
	c = []

	if len(a) == len(b):
		for i in range(len(a)):
			result = a[i] + b[i]
			c.append(result)

		return c
	else:
		return -1			