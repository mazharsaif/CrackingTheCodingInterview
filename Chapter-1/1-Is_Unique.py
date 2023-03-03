# O(N)
	
def is_unique(string):
	# Assume character set is ASCII (128 characters)
	
	if len(string) > 128:
		return False
	
	char_set = [False for i in range(128)]
	
	for char in string:
		char_idx = ord(char)
		if char_set[char_idx]:
			# Char found already
			return False
			
		char_set[char_idx] = True
		
	return True
	
	
	
