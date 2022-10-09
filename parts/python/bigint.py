# Divide a large integer represented as a string of digits
# by 2 returning the new quotient and the remainder.
# Also have the function return whether the quotient is zero
def div2(s: str) -> (str,int,bool):
   q = ""
   z = True                  # assume the quotient is zero
   r = ord(s[0]) - ord('0')  # current remainder

   for i in range(len(s)):
       p = r//2  # partial quotient
       if p != 0:
           z = False

       # build up the quotient
       q = q + chr(p + ord('0'))  # same as q + str(p)

       # make sure we don't get an
       # out of bounds error on s.
       if i < len(s) - 1:
           r = (r - 2*p) * 10 + (ord(s[i+1]) - ord('0'))

   r = r - 2*p   # final remainder
   return (q,r,z)

def dec2bin(q: str) -> str:
   z = False
   bits = ""
   while not z:
       (q, r, z) = div2(q)
       bits = str(r) + bits
   return bits

if __name__ == "__main__":
   q = '817698798768767656544321240980988766657657657655765765'
   t = q[:]

   print(dec2bin(q))
   print(bin(int(t))[2:])