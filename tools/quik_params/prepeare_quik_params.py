from typing import NamedTuple
from pprint import pp as pprint

class Param(NamedTuple):
	key: str
	type: str
	desc: str
	comment: list[str]


def read_file(name):
	with open(name, 'r', encoding='utf-8') as f:
		next(f)  # skip 1st line
		for line in f:
			yield line.rstrip('\n')


def main():
	PARAMS = dict()
	for line in read_file('PARAM.txt'):
		key,type,desc = line.split('\t')
		PARAMS.setdefault(key, Param(key,type,desc,[]))

	EMPTY = dict()
	SKIPPED = dict()

	def fill_params(filename,name):
		for line in read_file(f'{filename}.txt'):
			key,val,desc = line.split('\t')

			if val:
				if key not in PARAMS:
					arr = SKIPPED.setdefault(name,[])
					if key not in arr:
						arr.append(key)
			else:
				arr = EMPTY.setdefault(name,[])
				if key not in arr:
						arr.append(key)

			p = PARAMS.setdefault(key, Param(key,val,desc,[]))
			p.comment.append(name)

	fill_params('STOCK','STOCK')
	fill_params('PIF','PIF')
	fill_params('ETF','ETF')
	fill_params('FUT','FUT')
	fill_params('OFZ','BOND')
	fill_params('BOND','BOND')
	fill_params('OPT','OPT')
	fill_params('ETC','ETC')
	fill_params('OTC_STOCK','STOCK')
	fill_params('OTC_BOND','BOND')
	fill_params('CLT_FUT','CLT')
	fill_params('CLT_OPT','CLT')
	fill_params('LIST_BOND','BOND')
	fill_params('LIST_STOCK','STOCK')
	fill_params('FUT_F','FUT')

	# for line in read_file('STOCK.txt'):
	# 	key,val = line.split('\t')
	# 	if val:
	# 		if key in PARAMS:
	# 			PARAMS[key].comment.append('STOCK')
	# 		else:
	# 			SKIPPED.setdefault('STOCK',[]).append(key)
	# 	else:
	# 		EMPTY.setdefault('STOCK',[]).append(key)

	# for line in read_file('FUT.txt'):
	# 	key,val = line.split('\t')
	# 	if val:
	# 		if key in PARAMS:
	# 			PARAMS[key].comment.append('FORTS')
	# 		else:
	# 			SKIPPED.setdefault('FORTS',[]).append(key)
	# 	else:
	# 		EMPTY.setdefault('FORTS',[]).append(key)

	# for line in read_file('BOND.txt'):
	# 	key,val = line.split('\t')
	# 	if val:
	# 		if key in PARAMS:
	# 			PARAMS[key].comment.append('BOND')
	# 		else:
	# 			SKIPPED.setdefault('BOND',[]).append(key)
	# 	else:
	# 		EMPTY.setdefault('BOND',[]).append(key)

	# for line in read_file('OFZ.txt'):
	# 	key,val = line.split('\t')
	# 	if val:
	# 		if key in PARAMS:
	# 			PARAMS[key].comment.append('BOND')
	# 		else:
	# 			SKIPPED.setdefault('OFZ',[]).append(key)
	# 	else:
	# 		EMPTY.setdefault('OFZ',[]).append(key)

	# for line in read_file('OPT.txt'):
	# 	key,val = line.split('\t')
	# 	if val:
	# 		if key in PARAMS:
	# 			PARAMS[key].comment.append('OPT')
	# 		else:
	# 			SKIPPED.setdefault('OPT',[]).append(key)
	# 	else:
	# 		EMPTY.setdefault('OPT',[]).append(key)


	NONFILLED_1 = ['CFI_CODE','STOCKCODE','SEDOL','RIC','CUSIP','STOCKNAME','BSID']
	NONFILLED_2 = ['AGENT_ID', 'AUCTION_ID', 'ISSUER']
	NONFILLED_3 = ['REPOBASIS', ]

	print("= = "*20, "EMPTY")
	for e in EMPTY.values():
		e.sort()
		e[:] = [x for x in e if (x not in NONFILLED_1)]
	pprint(EMPTY,compact=True)
	print("= = "*20, "SKIPPED")
	for e in SKIPPED.values():
		e.sort()
		e[:] = [x for x in e if (x not in NONFILLED_1)]
	pprint(SKIPPED,compact=True)
	print("= = "*20)

	for e in PARAMS.values():
		key = f'"{e.key}",'
		type = f'"{e.type}",'
		desc = f'"{e.desc}"'
		line = f'{{ {key:27}{type:16}{desc} }},'
		default = ['STOCK','FORTS','BOND']
		default = ['STOCK','FUT','BOND','OPT','ETF','PIF','ETC','CLT']
		comment = ','.join([
			(c if c in e.comment else " "*len(c))
			for c in default
		])
		print(f'{line:103}--[[{comment}]]')


if '__main__' == __name__:
	main()
