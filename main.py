# Interface for the user to interact with
def Interface():
    running = True
    while running:
        choice = input("===Athlete Tracker===\n1. View statistics\n2. View rankings\n3. Store rankings\n4. Exit program\nInput: ")
        while len(choice) != 1 and int(choice).isnumeric() == False and choice < 1 and choice > 3:
            choice = input("===Athlete Tracker===\n1. View statistics\n2. View rankings\n3. Store rankings\n4. Exit program\nInput: ")
    
        ReadFile()
        match int(choice):
            case 1:
                ViewStatistics(athletes)
            case 2:
                ViewRankings()
            case 3: 
                StoreRankings()
            case 4:
                "Exiting program..."
                running = False
            case _ :
                print("Error - Input out of bounds")
        print("========================")
        ClearMemory()

# Clear memory to prevent extra copies of data in the variables    
def ClearMemory():
    athletes.clear()
    rankedAthletes.clear()

# Interface Option 1
def ViewStatistics(dictionary):
    for person in dictionary:
        print("========================")
        print(person)

# Interface Option 2
def ViewRankings():
    AddAverageRankingToDictionary()
    ViewStatistics(rankedAthletes)

# Interface Option 3
def StoreRankings():
    AddAverageRankingToDictionary()
    StoreRankedStatistics()
    print("Ranks stored.")

# Store the data from the rankedAthletes variable into the rankedDB.txt file
def StoreRankedStatistics():
    line = ""
    with open("./rankedDB.txt", "w") as file:
        for item in rankedAthletes:
            for key, value in item.items():
                line += f"{key}:{value} "
            file.write(f"{line}\n")
            line = ""

# Read the database file and append the values to the athletes variable
def ReadFile():
    with open("./database.txt") as file:
        for line in file.readlines():
            word = line.split()
            entry = dict(id = word[0], firstName = word[1], lastName = word[2], raceTime1 = word[3], raceTime2 = word[4])
            athletes.append(entry)

# Add average race time and ranking to athletes variable and 
# copy the athletes variable and add ranking to the rankedAthletes variable
def AddAverageRankingToDictionary():
    rankSort = []
    for person in athletes:
        avgTime = (float(person["raceTime1"]) + float(person["raceTime2"]))/2
        person.update(averageTime = avgTime, ranking = 0)
        rankSort.append([avgTime, person["id"]])
    rankSort.sort()
    rankPos = 1
    for rank in rankSort:
        for person in athletes:
            if rank[1] == person['id']:
                person["ranking"] = rankPos
                rankedAthletes.append(person)
        rankPos+=1

# Program starts here
athletes = []
rankedAthletes = []
Interface() # Start the interface