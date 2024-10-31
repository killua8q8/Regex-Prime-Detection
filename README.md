# Regex Prime Detection

Using this RegEx `^.?$|^(..+?)\1+$` to detect any number whether it's a prime number or not.

This method is using a pattern matching to do the detection. It converts the the given number, `n`, to a string that contains a character repeated n times. 

###### ⚠️ This method will have performance issue on large numbers.

###### Examples:
> n = 3  
> 'xxx' ('x' repeated `3` times) is the string that will be matched by the RegEx  
> There should be no match found on this string, so `3` is a prime number.  

> n = 4  
> 'xxxx' ('x' repeated `4` times) is the string that will be matched by the RegEx  
> The RegEx will find match like this '`xx` `xx`'. So `4` is **NOT** a prime number.  

> n = 9  
> 'xxxxxxxxx' ('x' repeated `9` times) is the string that will be matched by the RegEx  
> The RegEx will find match like this '`xxx` `xxx` `xxx`'. So `9` is **NOT** a prime number.  
