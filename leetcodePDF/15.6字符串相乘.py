"""
字符串相乘
"""
S1 = '8'
S2 = '235234566'


S1, S2 = (S2, S1) if len(S1) < len(S2) else( S1, S2)
m, n = len(S1), len(S2)

result =[0] * (m+n+1)


for i in range(n):
	residual = 0	# 置0 stuff

	for j in range(m):

		t = int(S1[m-1-j]) * int(S2[n-1-i]) + residual + result[m+n+1-1-i-j]

		result[m+n+1-1-i-j] = t % 10

		residual = t // 10


	# residual 可能还有剩余！ 没有这一行表现出大部分情况正常，但是小部分出现情况
	result[m+n+1-1-i-j-1] += residual

result = [str(i) for i in result]
print(int(''.join(result)) == int(S2)*int(S1))
print(result)
print(int(S2)*int(S1))