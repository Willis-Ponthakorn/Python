def  isPalindrome(s):
   if   len (s)    <=  1:
      return True
   return  s[0] == s[len (s)  - 1] and isPalindrome(s[1 : len (s) - 1])

inp = input('Enter Input : ')
line = ""
for i in inp:
    if i.isalpha():
        line += i.lower()
ans = "'" + inp + "'"
if   isPalindrome(line):
      print (ans,"is palindrome")
else :
      print (ans,"is not palindrome")