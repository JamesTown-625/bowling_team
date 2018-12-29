#Create an empty team dictionary to store all entered players and their scores
team = {}  
#Create a new txt file to write the results to with display summary function
outFile = open('./game_results.txt', 'w')

#function to create data structure of names and scores in the team dictionary
def bowling_team(data):
    splitData = data.split() 
    team[splitData[0]] = int(splitData[1])
    return team

#function to sort players in the order they were entered
def entered_team(team):
    print("\n===== Listed by Entry =====")
    outFile.write("\n===== Listed by Entry =====")
    for player in team:
        if team[player] == 300:
            print("\t*"+player+"\t\t"+str(team[player]))
            outFile.write("\n*"+player+"\t\t"+str(team[player]))
        else:
            print("\t"+player+"\t\t"+str(team[player]))
            outFile.write("\n"+player+"\t\t"+str(team[player]))

#function to sort the team by their score
def sort_team(team):
    top_score = sorted(team.items(), key=lambda kv: kv[1])
    top_score.reverse()
    print("\n===== Listed by Top Scorer =====")
    outFile.write("\n===== Listed by Top Scorer =====")
    highest_scorer = top_score[0][0]
    highest_score = top_score[0][1]
    for player in top_score:
        if player[1] == 300:
            print("\t*"+player[0] +"\t\t"+str(player[1]))
            outFile.write("\n*"+player[0] +"\t\t"+str(player[1]))
        else:
            print("\t"+player[0] +"\t\t"+str(player[1]))
            outFile.write("\n"+player[0] +"\t\t"+str(player[1]))
    return highest_score, highest_scorer

#function to alphabetize the players
def alpha_team(team):
    print("\n===== Listed Alphabetically =====")
    outFile.write("\n===== Listed Alphabetically =====")
    for player, score in sorted(team.items()):
        if score == 300:
            print("\t*"+player+"\t\t"+str(score))
            outFile.write("\n*"+player+"\t\t"+str(score))
        else:
            print("\t"+player+"\t\t"+str(score))
            outFile.write("\n"+player+"\t\t"+str(score))

#function to show the results of all function above
def display_summary(team):
    top_score = sorted(team.items(), key=lambda kv: kv[1])
    lowest_scorer = top_score[0][0]
    lowest_score = top_score[0][1]
    top_score.reverse()
    highest_scorer = top_score[0][0]
    highest_score = top_score[0][1]

    print("\nCongratulations "+ highest_scorer +"! You were the top score at "+str(highest_score)+"!")
    outFile.write("\nCongratulations "+ highest_scorer +"! You were the top score at "+str(highest_score)+"!")
    print("Sorry "+ lowest_scorer +", you were the lowest score at "+str(lowest_score)+". Keep practicing!")
    outFile.write("\nSorry "+ lowest_scorer +", you were the lowest score at "+str(lowest_score)+". Keep practicing!")
    sum = 0
    for player in top_score:
        sum = sum + player[1]

    avg = sum // len(team)
    print("\nThe average score for the team is: "+str(avg))
    outFile.write("\nThe average score for the team is: "+str(avg))

    
    return highest_score, highest_scorer, lowest_score, lowest_scorer
        
#First prompt that the User sees to know that they enter a name and a score
data = input('Enter the name of the player and their score separated by space i.e. John 280 >> ')
#Loop the prompt to allow them to enter as many players as they want, end with enter key
while data != '':
    bowling_team(data)
    data = input('Enter the name of the player and their score (End entry with "Enter")>> ')

#Call all defined functions to sort them into their individual needs and then finally display the summary from each function
entered_team(team)
sort_team(team)
alpha_team(team)
display_summary(team)

outFile.close()






