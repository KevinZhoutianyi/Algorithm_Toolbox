![](https://github.com/OnlyDrinkWater/MarkDown_Python/blob/master/Markdown/assert/8.PNG?raw=true)





Question:  knapsack has capacity 10,ask max value of gold without repetition



step 1-4 ( choose each gold or not )

for example the last value 46 is derived from whether choose the fouth gold(must from last row)

if not choose, the total value equals to without choosing means the last row same column

if choose, column number minus the choosen gold's capacity 10-2=8 get the value 30

​	means that if choose, the total value is 30(max at that situation) + 9=39

​	which is less than not choose.

therefore, the value is 46 from the same column last row.





##### choose each gold or not means contain all the selection 

##### choose or not are all derived from last row means contain all situation and optimal!



