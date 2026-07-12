bees = ["bee1", "bee2", "bee3"]
for bee in bees:
    bees.remove(bee)  # 删了第一个后，索引移位，你会发现 bee2 被跳过了
print(bees) # 输出可能是 ['bee2']，没删干净！

bees = ["bee1", "bee2", "bee3"]
# 使用 bees[:] 创建一个切片副本进行迭代
for bee in bees[:]: 
    bees.remove(bee) 
print(bees) # 输出 []，全部正确删除