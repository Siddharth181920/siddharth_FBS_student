'''Calulate total salary based on bsic. if basic <=5000 da, 
# ta and hra will be 10% 20% and 25% respectively otherwise da,ta and hra
# will be 15%, 25% and 30% respectively'''


basic = int(input("Enter the basic salary : "))

if(basic<=5000):
    da = basic/10
    ta = basic/20
    hra = basic/25

    salary = basic+da+ta+hra

    print(f"total salary is : {salary}")

else: 
     da= basic/15
     ta= basic/25
     hra= basic/30

     salary_1 = basic+ta+da+hra
     print(f"The total salary is : {salary_1}")

   # print(f"Enter the proper value")