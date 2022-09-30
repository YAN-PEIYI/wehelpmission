#要求一
def calculate(min, max, step):
    sum = min
    # min + n * step <= max    
    end = (max - min) // step #(range)/step=n
    for n in range(1, end + 1):
        #print('n:',n)
        value = min + n * step
        if value <= max:
            sum = sum + value
    print (sum)
    return sum

calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0

#要求二
def avg(data):
    avg = 0
    total = 0 #總和
    count = 0 #人數
    # 請用你的程式補完這個函式的區塊
    for x in data['employees']:
        if x['manager'] == False:
            #print(x)            
            count = count + 1 #count+=1  滿足條件的人數
            total = total + x['salary'] #累計薪資總和
            #print(sum)
    avg = total / count
    print ('avg: ', avg)

avg({    
    "employees":[
        {
            "name":"John",
            "salary":30000,
            "manager":False
        },
        {
            "name":"Bob",
            "salary":60000,
            "manager":True
        },
        {
            "name":"Jenny",
            "salary":50000,
            "manager":False
        },
        {
            "name":"Tony",
            "salary":40000,
            "manager":False
        }
    ]
}) # 呼叫 avg 函式

#要求三
def func(a):
    def func2(b, c):
        print (a + (b * c))
        return a + (b * c)
    return func2
# 請用你的程式補完這個函式的區塊

func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

#要求四
def maxProduct(nums):
    # print ('nums: ', nums)
# 請用你的程式補完這個函式的區塊
    value = float('-inf')
    for x in nums:
        for y in nums:
            # print ('x: ', x, ', y: ', y)
            if x != y and x * y > value:
                value = x * y
                # print ('value: ', value)
                    
    print (value)

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10

#要求五
def twoSum(nums, target):
    result = []
    length = len(nums) #列表長度
    for x in range(0, length): #開始造訪位置
        # print('x',x)
        for y in range(0, length): 
            #print("x:",x,"y:",y)
            if y > x:
                if nums[x] + nums[y] == target: # 找出兩個值相加是否等於target
                    #print ('nums[x]: ', nums[x], ', nums[y]: ', nums[y], ', target: ', target)
                    #print ('x:', x, ', y:', y) #找出位置
                    result = result + [x]
                    result = result + [y]
                    #break
    return result
# your code here
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

#要求六
def maxZeros(nums):

    n = len(nums)
    count = 0
    result2 = 0
 
    for i in range(0, n): #造訪list中所有的位置
     
        if nums[i] == 1:
            count = 0
 
        else:
            count+= 1
            result2 = max(result2, count)
         
    print (result2)
    return result2
                            
# 請用你的程式補完這個函式的區塊
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3