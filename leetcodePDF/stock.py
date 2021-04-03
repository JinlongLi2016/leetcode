price = input().strip()
price = [int(i) for i in price.split(' ')]

down = price[0]
pro1 = []
for i in range(len(price)):
    down = min(down, price[i])
    pro1.append(price[i] - down)

l = len(price)
top = price[-1]
pro2 = [-1] * len(price)
for i in range(len(price)-1, -1, -1):
    top = max(top, price[i])
    pro2[i] = top - price[i]
for i in range(len(price)-2, -1, -1):
    pro2[i] = max(pro2[i+1], pro2[i])


print(max([pro2[i] + pro1[i] for i in range(l)]))