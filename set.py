birthplace_list = ['Argentina', 'Australia', 'Vienam', 'Italy', 'Vienam', 
'US', 'US', 'US', 'UK', 'UK', 'Inida', 'US', 'Peru']

print ('People are born in...')
print (birthplace_list)
print(birthplace_list[0])

birthplace_set = {'Argentina', 'Australia', 'Vienam', 'Italy', 'Vienam', 
'US', 'US', 'US', 'UK', 'UK', 'Inida', 'US', 'Peru'}

# print ('People are born in...')
# print (birthplace_set[0])

birthplace = ['Argentina', 'Australia', 'Vienam', 'Italy', 'Vienam', 
'US', 'US', 'US', 'UK', 'UK', 'Inida', 'US', 'Peru']
print ('People are born in...')
print (birthplace)
print('The unique countries are...')
print(set(birthplace))

birthplace = {'Argentina', 'Australia', 'Vienam', 'Italy', 'Vienam', 
'US', 'US', 'US', 'UK', 'UK', 'Inida', 'US', 'Peru'}
print('Anyone from Antarctica?')
print('Antarctica' in birthplace)
print('Anyone from Australia?')
print('Australia' in birthplace)

birthplace = {'Peru', 'Australia'}
birthplace.add('Italy')
birthplace.add('Italy')
birthplace.add('Italy')

print(birthplace)

birthplace = set() ##empty set 
birthplace.add('Canada') ##append method is for list!!!!
birthplace.add('Canada')
print(birthplace)

zoo = {'lion', 'tiger', 'cat'}
zoo = set()
zoo = set(['lion', 'tiger', 'cat'])