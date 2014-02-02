You are given number of sticks (N). These sticks are represented in a list by their length (integers). For this mission, you should calculate the number of combinations that cannot form a complete triangle (for this mission, the degenerated case when a+b=c is considered to be a complete triangle too). If you can figure out which triangles do not work, you can help Nikola and Stephen repair the generator.

For example: in the list of lengths [5, 2, 9, 6] the combinations (5, 2, 9) and (2, 9, 6) would not form a complete triangle, because 5+2<9 and 2+6<9. This means that out of all the possible combinations of numbers in that list, only 2 would not form a complete triangle.

Hints: It can be useful for solving the task Triangle_inequality

Input: A list of integers.

Output: An integer.