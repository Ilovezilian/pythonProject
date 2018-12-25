print("hello! shuaishuai\n 每一朵雪花飘下，每一个烟火燃起，每一秒时间流动，都代表着要送你的每一个平安祝福。\n--来自潘帅python程序的祝福 -- 代码要不要贴一下呢？")


print('Interest Calculator:')
amount = float(input('Principal amount ?'))
roi = float(input('Rate of Interest ?'))
years = int(input('Duration (no. of years) ?'))
total = (amount * pow(1 + (roi / 100), years))
interest = total - amount
print('\nInterest = %0.2f' % interest)
