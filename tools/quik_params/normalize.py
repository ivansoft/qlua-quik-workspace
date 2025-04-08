
def main():
	keys = []
	with open('PIF.txt', 'r', encoding='utf-8') as f:
		next(f)  # skip 1st line
		for line in f:
			key, value = line.rstrip('\n').split('\t')
			# print(key, value)
			keys.append(key)
	values = dict()
	with open('PIF_.txt', 'r', encoding='utf-8') as f:
		next(f)
		for line in f:
			key, value = line.rstrip('\n').split('\t')
			# print(key, value)
			values[key] = value

	with open('PIF__.txt', 'w', encoding='utf-8') as f:
		f.write("\tPIF\n")
		for key in keys:
			f.write(f"{key}\t{values[key]}\n")


if '__main__' == __name__:
	main()
