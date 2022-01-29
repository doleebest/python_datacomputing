fruitprice = [ ['banana',400], ['apple',1000], ['mango',3000], ['watermelon',5000], ['grape',800]]

fruits =[ ]
prices =[ ]


for i in range (len(fruitprice)):
    fruits.append(fruitprice[i][0])
    prices.append(fruitprice[i][1])


print(fruits)
print(prices)
