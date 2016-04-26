def howOld():
    print("Let's see how long you have lived in days, minutes and seconds!")
    name = input("name: ")
    print("Great,", name, ". Now go ahead and enter your age.")
    age = int(input("age: "))
    days = age * 365
    minutes = age * 852948
    seconds = age * 31556926
    print (name, "has been alive for a shocking ", days, " days ", minutes, " minutes and ", seconds, " seconds! Holy Toledo!")
howOld()
