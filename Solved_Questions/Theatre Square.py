# A. Theatre Square
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# Theatre Square in the capital city of Berland has a rectangular shape with the size n × m meters. On the occasion of the city's anniversary, a decision was taken to pave the Square with square granite flagstones. Each flagstone is of the size a × a.

# What is the least number of flagstones needed to pave the Square? It's allowed to cover the surface larger than the Theatre Square, but the Square has to be covered. It's not allowed to break the flagstones. The sides of flagstones should be parallel to the sides of the Square.

# Input
# The input contains three positive integer numbers in the first line: n,  m and a (1 ≤  n, m, a ≤ 109).

# Output
# Write the needed number of flagstones.

n,m,a=map(int,input().split())
if m%a==0:
    ans=m//a
else:
    ans=m//a+1
if n%a==0:
    ans1=n//a
else:
    ans1=n//a+1
print(ans*ans1)
