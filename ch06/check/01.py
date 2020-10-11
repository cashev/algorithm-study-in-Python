text = '000000111111100111000000001111'

pre = text[0]
count = 1
ans = []
for i in range(1, len(text)):
  if text[i] == pre:
    count += 1
  else:
    ans.append(count)
    count = 1
  pre = text[i]

ans.append(count)

print(ans)
