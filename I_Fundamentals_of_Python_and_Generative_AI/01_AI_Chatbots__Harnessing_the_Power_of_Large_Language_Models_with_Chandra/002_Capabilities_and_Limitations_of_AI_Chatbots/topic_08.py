words = ["Python", "is", "a", "fun", "language", "to", "learn!"]
long_words_upper_case = [word.upper() if len(word) > 3 else word for word in words]

print(" ".join(long_words_upper_case))
