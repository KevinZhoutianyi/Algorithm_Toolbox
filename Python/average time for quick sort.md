



![wow](https://github.com/OnlyDrinkWater/MarkDown_Python/blob/master/Markdown/assert/5.PNG?raw=true)





![qwq](https://github.com/OnlyDrinkWater/MarkDown_Python/blob/master/Markdown/assert/2.PNG?raw=true)



n problem -> n/b problem

x time solution -> a * x  time



Practice：(When you write a recursion algorithm and want to get the time)

1. find the time used of the tree root f(n)

2. find the time used of the second line af(n/b)

   if equal: situation 2 (all the line matter)

   if decreasing: situation 1 (first line matter)

   if increasing: situation 3 (last line matter)





3 situations:   (i used)

1.  f(n) is important    d>logba   so O(n^d)

2.  both important      d=logba     so  O(n^d.logn)         f(n) * height of the tree

3.  leaves are important      d<logba    so O(n^logba)




