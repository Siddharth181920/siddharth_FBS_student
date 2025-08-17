''' Accept no. of passengers from user and per ticket cost.
then accept age of each passenger and then calculate total amount to ticket
to travel for all of them based on following condition :

a. Children below 12 = 30% Discount
b. Senior citizen (above 59) = 50% Discount
c. Others need to pay full '''


no_of_pass = int(input("Enter the number of passengers : "))

per_tic_cos = int(input("Enter the cost of ticket : "))

i =0

while(i<no_of_pass):
    age = int(input("Enter the age of passenger :"))
    if(age<12):
        dis_amt = per_tic_cos*0.12
        to_amt = per_tic_cos-dis_amt
        print(to_amt)

    elif(age>59):
        dis_amt1 = per_tic_cos*0.5
        to_amt1= per_tic_cos-dis_amt1

        print(to_amt1)

    elif(age>12):
        to_amt2= per_tic_cos
        print(to_amt2)

    else:
        print(f"Enter a correct age")

    i +=1
