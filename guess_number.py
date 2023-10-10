
import random

# true_value = random.randint(1,100)
true_value = 48
print("숫자를 맞춰보세요(1~100)")

input_value = 99999
while true_value != input_value : 
    
    input_value = int(input())
    
    if input_value > true_value :
        print("숫자가 너무 큽니다")

    elif input_value < true_value :
        print("숫자가 너무 작습니다")
    
print(f"정답입니다. 입력한 숫자는 {true_value}")

