def calculate(min, max):
        sum=0
        for n in range(min,max+1):
                sum+=n
        print("計算結果:",sum)
               
calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30
