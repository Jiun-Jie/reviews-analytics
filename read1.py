data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:	# count 與1000 餘數 =0
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
a = sum_len / len(data)
print('每句留言長度為', a)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])
#進階簡寫版
good1 =[1 for d in data if 'good' in d]
print(good1)

bad = ['bad' in d for d in data]
print(bad)

# bad = []
# for d in data:
# 	bad.append('bad' in d)