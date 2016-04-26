counter = 1
for counter in range (1,101):
    if counter % 3 == 0 and counter % 5 == 0:
        print 'FizzBuzz'
    elif counter % 3 == 0:
        print 'Fizz'
    elif counter % 5 == 0:
        print 'Buzz'
    else:
        print counter
    
