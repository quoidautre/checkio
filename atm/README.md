Teach Sofia how to use an ATM. The ATM on their home island can give only 5F bills, which means that the machine will not give any bill not divisible by 5F. In addition to that, the commission for each cashing out is 0.5F + 1% from the taken out cash plus the robots cannot go beyond the card’s balance. After each operation, the bank rounds the balance to lower whole value (57.9 = 57, 61.1 = 61)

__Input:__ List of integers. First one denotes Robot’s account balance, second is a list of money amounts robot want to withdraw.

__Output:__ Account balance after all operations, Integer

__Example:__
# Withdraw without any incident 
# 120 - 10 - 0.5 - 1% = floor(109.4) = 109
# 109 - 20 - 0.5 - 1% = floor(88.3) = 88
# 88 - 30 - 0.5 - 1% = floor(57.2) = 57
checkio([120, [10, 20, 30]]) == 57
checkio([120, [200, 10]]) == 109
checkio([120,[3, 10]]) == 109
checkio([120, [200 , 119]]) == 120
checkio([120, [120, 10, 122, 2, 10, 10, 30, 1]]) == 56
