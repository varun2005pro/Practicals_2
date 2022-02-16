i = 0
team_dict = dict()
while i < 1:
   tn = input("Enter the team name/Type 'n' to cancel: ")
   if tn == 'n' or tn == 'N':
       break
   else:
       w = int(input("Enter the number of wins: "))
       l = int(input("Enter the number of losses: "))
       team_dict[tn] = [w, l]
       print()
print()
print("Your given dictionary: ")
print()
print("Team Name\t", "Wins\t", "Losses")
for i in team_dict:
   print(i, "\t\t", team_dict[i][0], "\t\t", team_dict[i][1])
#BY VARUN GAUTAM(XI-A)
