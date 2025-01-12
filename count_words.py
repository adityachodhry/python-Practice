def CountWords(words):
	if words is not None:
		numberOfWords = [Eachword.count(' ') + 1 for Eachword in words]
		return numberOfWords
