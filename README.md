# Searching

Kumar wants to buy a keyboard and USB drive from a store.The store has several models.He wants to spend as much as for the 2 items from her budget.

Given the Price lists for the store's keyboard and USB drives, and Poojitha's budget,find and print the amount of money Poojitha spend.

if she doesn't have enough money to both a keyboard and USB drive,print -1 instead.She will buy only the two required items.

INPUT FOMRAT:

  First line contains three space-seperated integers b,n and m,her budget,the number of keyboard models and the number of USB drive models.
  
  Second line contains n space-separated integers keyboard[i],the prive of each keyboard model.
  
  Third line contains m space-seperated integers drivers,the price of USB drives.

OUTPUT FORMAT:

  Print a single integer denoting the amount of money Poojitha will spend.If she doesn't have enough money to buy one keybourd and one USB drive,print -1 instead

Input-1:

10 2 3

3 1

5 2 8

output:

9

EXPLANATION:

She can buy the 2nd keyboard and the 3rd usb drive for a total cost of 8+1 = 9

Input-2:

5 1 1

4

5

output-2:

-1

EXPLANTION:

There is no way to buy one keyboard and one usb drive because 4 + 5 > 5,so we print -1

