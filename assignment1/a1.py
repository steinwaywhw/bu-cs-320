

import re


def tokenize(regexp, stream):
	tokens = [t for t in re.split(regexp, stream)]
	return [t for t in tokens if not t.isspace() and not t == ""]


def test_tokenize():
	print("test_tokenize()")

	cases = [
		(r"(\s+|red|blue)", 
			"red red blue red", 
			["red", "red", "blue", "red"]),
		(r"(\s+|true|false|and|or|not|,|\(|\))", 
			"and (or (and (true, false), not(false)), or (true, false))", 
			['and', '(', 'or', '(', 'and', '(', 'true', ',', 'false', ')', ',', 'not', '(', 'false', ')', ')', ',', 'or', '(', 'true', ',', 'false', ')', ')']),
		(r"(\s+|up|down|left|right|stop|;)", 
			"up; up; up; right; down; up; stop;",
			['up', ';', 'up', ';', 'up', ';', 'right', ';', 'down', ';', 'up', ';', 'stop', ';'])
		]

	for case in cases:
		if tokenize(case[0], case[1]) == case[2]:
			print("pass")
		else:
			print("fail")

