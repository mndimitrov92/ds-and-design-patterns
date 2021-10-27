a = [
	[
		[]
	],
	[
		[
			[
				[],
				[],
				[]
			],
			[]
		],
		[]
	]
]

count = 6


def count_edges(data):
	if data:
		return sum([count_edges(n) for n in data])
	if not data:
		return 1

assert count == count_edges(a)