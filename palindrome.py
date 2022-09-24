def palindrome(a):
  
    mid = (len(a)-1)//2    
    start = 0                
    last = len(a)-1
    flag = 0

    while(start <= mid):
  
        if (a[start]== a[last]):
             
            start += 1
            last -= 1
             
        else:
            flag = 1
            break;
             
    if flag == 0:
        return True
    else:
        return False

def change_base(num,base):
    base_num = ""
    while num>0:
        dig = int(num%base)
        if dig<10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10)
        num //= base
    base_num = base_num[::-1] 
    return base_num


basis = input()

for num in range(1, 300):
    power_num = pow(num, 2)
    new_power_num = change_base(power_num, int(basis))
    new_num = change_base(num, int(basis))
    if palindrome(str(new_power_num)):
        print(str(new_num) + ' ' + str(new_power_num))