def find(*nums):
    a = len(nums)
    total = (a+1)*(a+2)/2
    summ = sum(nums)
    result = int(total - summ)
    return result

def solution(*nums):
    m = max(nums) 
    if m < 1:
        print("All numbers are negative, so: ", 1) 
    else:
        if find(*nums) == 0:
            miss = max(nums) + 1
            print("Missing number is: ", miss)
        else:
            print("Missing number is: ", find(*nums))

solution(1,2,3,4,6)
solution(1,2,3)
solution(-1,-2,-6)
