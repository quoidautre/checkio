http://www.checkio.org/mission/common-words/

Let's continue examining words. You are given two string with words separated by commas. Try to find what is common between these strings. The words are not repeated in the same string.

Your function should find all of the words that appear in both strings. The result must be represented as a string of words separated by commas in alphabetic order.

Hints: You can easily solve this task with several useful functions: str.split, str.join and sorted. Also try using the built-in type -- set.

Input: Two arguments. Strings.

Output: The common words as a string.

Example:
checkio("hello,world", "hello,earth") == "hello"
checkio("one,two,three", "four,five,six") == ""
checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"
How it is used: Here you can learn how to work with strings and sets. This knowledge can be useful for linguistic analysis.

In the world of CheckiO, you can explore new islands by solving missions and earning points solving challenges in the island that you have opened. We have over 100 missions for you to discover and play here at CheckiO!