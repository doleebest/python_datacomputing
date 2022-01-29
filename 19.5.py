fruitdict = {'banana':400, 'mango':3000, 'apple':1000, 'grape':800, 'watermelon':5000}
fruits = ['mango', 'apple', 'mango', 'apple', 'mango'
          , 'banana', 'mango', 'apple', 'mango','mango',
          'grape', 'mango', 'watermelon', 'grape', 'banana',
          'apple', 'mango', 'mango', 'banana', 'mango']

for i in range (len(fruits)) :
    fruits[i] = fruitdict[fruits[i]]

sum=0
for i in fruits :
    sum += i
    
print(sum)




    
    
          


          
