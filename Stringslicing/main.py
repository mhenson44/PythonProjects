#String Slicing = create a substring by extracting elements from another string
#indexing [] or slice ()
#[start:stop:step]

#indexing
#name = 'Michael Henson'

#first_name = name[:7]
#last_name = name[8:]
#funky_name = name[::1]
#reversed_name = name[::-1]

#print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])
