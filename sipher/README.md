Help Sofia to make a decipher for the passwords that Nikola will encrypt in the map.

A cipher grille is a 4 × 4 paper square in which four windows are cut out. Putting the grille on a paper sheet of the same size, the chairman writes down the first four symbols of his password in the windows (see fig. below). After that the chairman turns the grille clockwise by 90 degrees. The symbols written earlier become hidden under the grille and clean paper appears in the windows. He writes down the next four symbols of the password in the windows and again turns the grille by 90 degrees. Then he writes down the following four symbols and turns the grille once more. After that he writes down the last four symbols of the password. Now, without the same cipher grille, it is very difficult to restore the password from the resulting square with 16 symbols. Thus, the chairman is sure that no contestant will get access to the problems too early.

Write a module for the robots to remember their passwords with the codes easily when they come back.

__Input__ The first four lines contain the Robot's cipher grille. The next four lines contain the square with the ciphered password. All the symbols in the square are lowercase Latin letters.

__Output:__ Password

__Example:__

checkio([[
'X...',
'..X.',
'X..X',
'....'],[
'itdf',
'gdce',
'aton',
'qrdi']
]) == 'icantforgetiddqd'

checkio([[
'....',
'X..X',
'.X..',
'...X'],[
'xhwc',
'rsqx',
'xqzz',
'fyzr']
]) == 'rxqrwsfzxqxzhczy'