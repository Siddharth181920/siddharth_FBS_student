# WAP to accept basic salary of n emp. (n should be accepted from user ). 
# If basic salary is below 20000 then da = 10% , ta = 12%, and hra = 15% otherwise da = 15% , ta = 18% and 
# hra = 20% . based on this calculate the total salary of each emp and also total salary of all emp .

bas_sal = int (input("Enter a basic salary :"))

if (20000<0):

    da = bas_sal%10
    ta = bas_sal%12
    hra = bas_sal%15

    tot_sal = bas_sal+da+ta+hra

    print(tot_sal)

else:
     da = bas_sal%15
     ta = bas_sal%18
     hra = bas_sal%20

     tot_sal2= bas_sal+da+ta+hra

     print(tot_sal2)