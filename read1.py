data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:	# count 與1000 餘數 =0
			print(len(data))
print(len(data))
print(data[0])
print('-----------------------')
print(data[1])