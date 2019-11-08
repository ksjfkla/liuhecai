from random import randint
from textwrap import dedent
import math
import datetime
import matplotlib.pyplot as plt
import numpy as np


def welcome():
  global accountmoney
	#print("欢迎参加山寨版六合彩!")
	print(f"目前是第{i+1}位玩家的{qi}期摇号")
	#print(f"你现在的余额为： {accountmoney} 元")
	#while True:
		#charge = int(input("请问需要充值吗？需要请按1，不需要请按0\n"))
		#if charge == 1:
		#	code = input("请输入柜台密码：> ")
		#	if code == "1106":
		#		accountmoney += int(input("密码正确！请输入充值金额：\n"))
		#		print(f"充值后的余额为： {accountmoney} 元")
		#		break
		#		
		#	else:
		#		print("密码错误，不允许充值")
		#		break
			
		#elif charge == 0:
		#	print("好的，祝游戏愉快！")
		#	break
		#else:
		#	print("输入出错，请重新输入")

		
def touzhu():	
	global betmoney
	global betnumbers
	global accountmoney
	global indicator
	
	#betmoney = int(input(f"请输入第{qi}期每个号码投注金额:______\n"))
	#if accountmoney/betmoney >= 1:
	#	print(f"已确认，每个号码投注金额为{betmoney}元")
	#	print(f"根据账户余额，可投注的号码数量最大为：{math.floor(accountmoney/betmoney)}")
		
	#else:
	#	input("你的资金余额连一个号码都买不起，去充一下钱吧。请下期再来。")
	#	indicator.append(0)

	#if 0 not in indicator:
	#	while True:
	#		betnumber = input("请输入你想要投注的号码，用空格隔开，输入结束后直接按回车即可\n")
	betnumbers = [randint(1, 49)]
	#		if all(i.isdecimal() or i.isspace for i in betnumber) and \
	#		len(list(map(int, betnumber.split()))) <= math.floor(accountmoney/betmoney):
	#			betnumbers = list(map(int, betnumber.split()))
	#			break
	
	#		elif len(list(map(int, betnumber.split()))) > \
	#		math.floor(accountmoney/betmoney):
	#			input("你的资金余额买不起这么多号码，去充一下钱吧。请下期再来。")
	#			indicator.append(0)
	#			break
			
	#		else:
	#			print("输入有误，请重新输入\n")
			
		

	
def yaohao():
	
	#global betnumbers
	#print(f"你的投注号码为： {betnumbers}")
	#a = input("按回车后开始摇号……\n")
	i = 0
	
	#while i < 7:
	result[6] = randint(1, 49)
		#if a not in result:
		#	result.append(a)
		#	i += 1
		#else:
		#	continue
	
	#for i in range(6):
	#	print(f"第{i+1}个号码是:{result[i]}")
		
	#print(f"而特别号码是:{result[6]}")
	
def jiesuan():	
	global result
	global betnumbers
	global accountmoney	 
	global betmoney 
	global start
	global odds
	
	
	if result[6] in betnumbers:
		#print("恭喜你啊中奖啦！")
		accountmoney -= len(betnumbers) * betmoney
		accountmoney += betmoney * odds
		
	else:
		#print("很遗憾此次没有中奖。")
		accountmoney -= len(betnumbers) * betmoney
	
	#print(f"你现在的余额为： {accountmoney} 元")
	#print("-" * 10)
		
	#start = int(input("请问是否继续？继续请按1，结束请按0\n\n\n"))
	betnumbers = []
	result = [0,0,0,0,0,0,0]
	
	

starttime = datetime.datetime.now()

accountmoney = 1000
qi = 1
betnumbers = []
start = 1
result = [0,0,0,0,0,0,0]
betmoney = 1
indicator = []
kellyacm = []
kellyqi = []
odds = 49
times = 36500
#rounds = 3
#times = float('inf')
rounds = 200
all = 0
dict1 = {}
	
for i in range(rounds):
	innerlist = []
	while start and accountmoney >= 1 and qi <= times:	
			
		welcome()
		touzhu()
		if 0 in indicator:
			qi += 1
			indicator = []
			continue
		else:
			yaohao()
			jiesuan()
			qi += 1
			innerlist.append(accountmoney)
			#all += 1
			#print(all)
			
			
	else:
		#print("再见！\n\n")
		kellyacm.append(accountmoney)
		kellyqi.append(qi)
		dict1[i] = innerlist
		
	accountmoney = 1000
	qi = 1
	betnumbers = []
	start = 1
	result = [0,0,0,0,0,0,0]
	betmoney = 1


		
	
	
#print(kellyacm)
#print("*" * 10)
#print(kellyqi)
print("-" * 30)
print(f"本次测试的初始资金为1000元、每回合投注金额为1元、每轮最大回合数为{times}、共{rounds}轮")
print(f"池子共49个号码，赔率为1:{odds}")
#print("因此理论上最低参与回合数为1000次，预期每轮回合数为12250")
print("*" * 30)


for j in range(rounds):
	print(f"在第{j+1}次无限重复博弈中，总博弈回合数为{kellyqi[j] - 1}, 最终余额为{kellyacm[j]}")

print(f"""
玩家最终总资产为{sum(kellyacm)}, 
平均每位玩家总资产为{sum(kellyacm)/rounds},
最大赢家资产为 {max(kellyacm)}
最惨玩家资产为 {min(kellyacm)}
""")

c = 0
d = 0
e = 0
f = 0
g = 0

for k in kellyacm:

	if k == 0:
		c += 1
		
	elif k > 1000:
		d += 1
		e += (k-1000)
		
	else:
		f += 1
		g += (1000-k)

if d != 0 and f != 0:
	print(f"""
	there are {c} zeors, with a percentage of {c/rounds}.
	there are {d} winners, with an average profit of {e/d}
	there are {f + c} losers, with an average loss of {(g+c*1000) / (f + c)}
	""")
	
else:
	print(f"""
	there are {c} zeors, with a percentage of {c/rounds}
	there are {d} winners, with sum profit of {e}
	there are {f + c} losers, with sum loss of {g + c * 1000}
	""")

#print(dict1)


for l in range(rounds):
	plt.figure()
	plt.plot(list(range(1, len(dict1[l]) + 1)), dict1[l], linewidth = 1)
	plt.title(f"Career:{l+1}", fontsize=24) 
	plt.xlabel("number of games", fontsize=14)
	plt.ylabel("accountmoney", fontsize=14) 
	#plt.ylim((min(dict1[l]), max(dict1[l])))
	
	#my_x_ticks = np.arange(-5, 5, 0.5)
	my_y_ticks = np.arange(min(dict1[l]), max(dict1[l]), 500)
	#plt.xticks(my_x_ticks)
	plt.yticks(my_y_ticks)

	
	plt.tick_params(axis='both', labelsize=10)
	plt.savefig(f"Career:{l+1}.png")
	
endtime = datetime.datetime.now()
print(f"程序的运行时间为：{endtime-starttime}")
#plt.show()
