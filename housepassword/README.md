Help Nikola write a password security check module for Sofia. Password is considered to be strong enough if its length is more than or equal 10 symbols and it has at least one digit, one upper and one lower case letters.

__Input data:__ String which is a password.

__Output data:__ True if the password is safe.

__Example:__

checkio('A1213pokl')==False
checkio('bAse730onE')==True
checkio('asasasasasasasaas')==False
checkio('QWERTYqwerty')==False
checkio('123456123456')==False
checkio('QwErTy911poqqqq')==True
