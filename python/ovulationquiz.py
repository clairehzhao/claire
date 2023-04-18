users = {}
def inputdata():
    def calculateov(lastperiodday, cyclelength, periodlength, lastperiodmonth):
        nextovulation = lastperiodday + (cyclelength - periodlength) // 2
        newovmonth = 0
        newovday = 0
        if nextovulation > 30:
            newovmonth = lastperiodmonth + 1
            newovday = nextovulation - 30
        else:
            newovmonth = lastperiodmonth
            newovday = nextovulation
        return [newovmonth, newovday]

    lastperiodmonth = int(input("When was your last period month: "))
    lastperiodday = int(input("when was your last period day: "))
    periodlength = int(input("How long is your period length (in days): "))
    cyclelength = int(input("How long is your period cycle (in days): "))

    temp_list = calculateov(lastperiodday, cyclelength, periodlength, lastperiodmonth)

    data_list = [lastperiodmonth, lastperiodday, periodlength, cyclelength] + temp_list
    return data_list

name = input("Hello! Please enter your first name and last initial: ")
print("Welcome " + name)

temp_data = inputdata()

#print(temp_data)
users[name] = [temp_data]

print("Your next ovulation date will be (month/day): " + str(temp_data[4]) + "/" + str((temp_data[5])))

while 1 > 0:
    moredata = input("Do you want to input more data? (yes/no): ")
    if moredata == "yes":
        temp_data = inputdata()
        users[name] = users[name] + [temp_data]
    else:
        month = int(input("Which previous ovulation month would you like to see: "))
        #print(users[name])
        found = 0
        for rec in users[name]:
            if rec[4] == int(month):
                print("Found your record:")
                print("Month: " + str(rec[4]))
                print("Day: " + str(rec[5]))
                found = 1
                break
        if found == 0:
            print("Did not find the record")
        exit() 