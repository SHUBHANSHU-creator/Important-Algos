# A wallet consists of an array of size n
# for 1 dollar you can change a[i] to [a[i]+1,2*a[i]] or [ceil(a[i]/2),a[i]-1]
#return minimum amt of money to convert every one to same denomination



from collections import Counter
import math
def denomination(money):
    dp = Counter()
    for m in money:
        l=h = m

        req = 0
        while l != 1:
            dp[l] -=1
            l = math.ceil(l/2)
            req += 1
        dp[1] += req

        while h<=10**6:
            dp[h+1] += 1
            h*=2
    tot,cur = float('inf'),0
    for i in dp:
        cur += dp[i]
        tot = min(tot,cur)
    return tot

money = [1,2,3,3,5,2]
print(denomination(money))