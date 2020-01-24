# List: []
# Dictionary: {}
# Tuple: ()

# Tuple: immutable 
# List: mutable

post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# Tuple unpacking
title, sub_heading, content = post

# Equivalent to Tuple unpacking
# title = post[0]
# sub_heading = post[1]
# content = post[2]

print(title)
print(sub_heading)
print(content)

# adding elements to tuple
post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

print(id(post))
print(id(post))

post += ('published',)# you cant change a tuple - we are reasigning the name post to a new tuple

print(id(post)) # id changes

title, sub_heading, content, status = post

print(title)
print(sub_heading)
print(content)
print(status)

# nesting lists into tuples
post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')

tags = ['python', 'coding', 'tutorial']

post += (tags,)

print(post[-1][1]) # how to grab items in tuple and lists


# slicing tuples
post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

print(post[1::2])


# removing elements in tuple
post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

# Removing elements from end
post = post[:-1]

# Removing elements from beginning
post = post[1:]

# Removing specific element (messy/not recommended)
post = list(post)
post.remove('published')
post = tuple(post)

print(post)

# using tuples as keys
priority_index = {
  (1, 'premier'): [1, 34, 12],
  (1, 'mvp'): [84, 22, 24],
  (2, 'standard'): [93, 81, 3],
}

# call as a list otherwise it would just be a view object
print(list(priority_index.keys()))