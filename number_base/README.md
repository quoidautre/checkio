http://www.checkio.org/mission/number-radix/

Do you remember the radix and Numeral systems from math class? Let's practice with it.

You are given a positive number as a string along with the radix for it. Your function should convert it into decimal form. The radix is less than 37 and greater 2. The task uses digits and the letters A-F for the strings.

Watch out for cases when the number cannot be converted. For example: "1A" cannot be converted with radix 9. For these cases your function should return -1.

Hints: You can easily solve this task with int() conversion and handling exceptions (Look at ValueError).

Input: Two arguments. A string and an integer.

Output: The number. An integer.

Example:
checkio("AF", 16) == 175
checkio("101", 2) == 5
checkio("101", 5) == 26
checkio("Z", 36) == 35
checkio("AB", 10) == -1
How it is used: Here you will learn how to work with the various numeral systems and handle exceptions.

We have an adviser team on CheckiO, so if you get stuck solving a challenge, use the “ask advisers” function to ask someone a question about it.