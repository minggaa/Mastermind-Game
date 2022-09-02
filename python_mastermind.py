import random

#Introduction to the game
def intro():
    print ("Welcome to an on-screen version of 'MASTERMIND'!!!\n")
    print ("Rules:\n1) You are to predict the position of 4 different types of set colors.\n2) Now the position matters, so even if you picked the right colors as long as its not in the right place you will not get the answer right.\n3) Key in ONLY the initials (in upper or lower case)of the given colors with SPACE IN BETWEEN, and press 'Enter' when done.\n   Example: (Enter your four guesses: r y w g)\nGood Luck, Have Fun!!!\n")
    print ("Your color choices are:\nRed (R), Green (G), Blue (B), Yellow (Y), Orange (O), White (W), Pink (P)\n")

#Function for when all elements by user matches answer, and to check their position (correct color, correct place)
def corcolcorpl(color, user):
    (right_place, wrong_place) = (0, 0)             #Set counter for the colors in correct and wrong places.
    for x in range(4):
        if user[x] == color[x]:                     #If the user answer has the correct color in same place as the default answer,
            right_place+=1                              #then right place will increase by 1.
        else: 
            wrong_place+=1                              #else wrong place will increase by 1.
    return (right_place, wrong_place)
            
#Function for when not all elements by user matches answer, but still checks for position (correct color, wrong place)
def corcolwrgpl(color, user):
    (col, use)= (color[:], user[:])                 #Assigning new lists to deal with duplicates later on.
    (right_place, wrong_place) = (0, 0)
    for x in range(4):                              #A loop to check for correct colors when not all color/elements present in user answer.
        if use[x] == col[x]:
            right_place+=1
            col[x] = 0                              #When the correct color is present, the position in list col will be replaced with 0 to avoid duplicates.
    for x in range(4):                              #A nested loop to check for wrong colors by scanning through every element (y) in color list with user answer at each index (x).
        for y in range(4):
            if (use[x] == col[y]) and x != y:
                wrong_place+=1
                col[y] = 0                          #When there's a correct color but is in the wrong place, the col list will be updated with the color being replaced with 0.
                break                               #If statement is true then it will break the y nested loop to move on to the next index of user answer.
    return (right_place, wrong_place)
        
#Function for the main body of the games code (asking guesses, generating random colors, user input data validation)
def main_body():
    intro()
    colors = ['R', 'G', 'B', 'Y', 'O', 'W', 'P']                            #Color list.
    color_ans = []                                                          #User answer list.
    (yes_lst, no_lst) = (['Yes','yes', 'Y', 'y'], ['No','no', 'N', 'n'])    #Yes & No list (for when asking [Y/N] questions).
    guess = 0                                                               #Guess counter.
    replay = 1                                                              #Replay counter (for when user wants to play again).

    play = "Yes"
    while play in yes_lst:                                                  #While loop for the main game body to keep prompting user answer until correct answer is keyed.

        if len(color_ans) != 4:                                             #This is for when user replays, it checks if color_ans list is empty then it will generate another set of random colors for the new game.
            for count in range(4):
                x = random.choice(colors)                                   #Random color generator.
                color_ans.append(x)                                         #For each random color, the list will be updated/appended until loop ends.
        
        validt = False
        while validt == False:                                                      #This while loop is for checking is user answer is in valid format.
            validt = True
            
            ans = list(map(str, input("Enter your four guesses: ").split()))        #Prompts for user input/guesses
            user_ans = [x.upper() for x in ans]                                     #Makes user answer all upper case
            
            if len(user_ans) > 4:                                                   #Checks if user guess/input is more than 4 colors.
                print ("Error!: Input value exceeds required amount. Please enter ONLY FOUR colors!\n       (initials only with space in between)\n")
                validt = False
            elif len(user_ans) < 4:                                                 #Checks if user guess/input is less than 4 colors.
                print ("Error!: Input value does not meet required amount. Please enter ONLY FOUR colors!\n       (initials only with space in between)\n")
                validt = False
            else:
                for x in range(len(user_ans)):                                      #For loop to check if user answer is in the color list or not,
                    if user_ans[x] not in colors:                                       #if any color/answer is not present in the color list
                        print ("Error!: Invalid input. Please enter the given color initials selection.\n")     #error message will be shown
                        validt = False                                              #And causing the while loop to loop once more until everything is valid.
                        break
        guess+=1
        if sorted(user_ans) == sorted(color_ans):                                   #This statement is to check between the user answer and color answer if they all contain the same elements/color.
            (rp, wp) = corcolcorpl(color_ans, user_ans)                                 #If yes then calls the function corcolcorpl.
        else:
            (rp, wp) = corcolwrgpl(color_ans, user_ans)                                 #Else calls the function corcolwrgpl.

        if rp == 4:                                                                 #If user answer has all colors in the right place = right place is 4, then
            print("\nCongratulations, You Won!")                                        #prints winning message.
            if guess > 1:                                                           #This if statement is to see if the user takes one or more tries.
                print("You took", guess, "guesses!\n")
            else:
                print("And, you took only a single guess!! What a legend!\n")
                
            play = str(input("Do you wish to play again? [Y/N] "))                  #Prompts the user if they want to play again.
            while play not in yes_lst or play not in no_lst:                        #While loop for [Y/N] validation.
                if play in yes_lst:
                    replay+=1
                    color_ans.clear()                                                   #Resets the game toprepare for the next game.
                    guess-=guess
                    print("\n"*40)                                                      #Creates a new space and prints the intro again.
                    intro()
                    break
                elif play in no_lst:                                                    #Data validation for when the user doesn't want to play again.
                    if replay == 1:
                        print ("*"*11,"GAME OVER", "*"*11, "\nThank you for playing!")
                    else:
                        print ("*"*11,"GAME OVER", "*"*11, "\nYou played", replay, "times.\nThank you for playing!")
                    break
                else:                                                                   #If user enters anything other than the statement accepts, error message is shown.
                    print ("Error!: Invalid response. Please enter either in capital or lower case of y or n.")
                    play = str(input("Do you wish to play again? [Y/N]: "))
                
        else:                                                                           #Prints counter for the colors in right and wrong place.
            print("Correct Color in the Right Place: ", rp, " ||  Wrong Color in the Wrong Place: ", wp)
            
main_body()
