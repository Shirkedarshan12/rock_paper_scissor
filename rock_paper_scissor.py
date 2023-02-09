import random
l=["rock","paper","scissor"]
# rock vs paper - paper wins
# rock vs scissor - rock wins
# paper vs scissor - scissor wins

while(True):
    ucount=0
    ccount=0
    userChoice=int(input('''
    Game start
    1 yes
    2 no
    '''))
    if userChoice==1:
        for a in range(1,6):
            userInput=int(input('''
            1.rock
            2.paper
            3.scissor
            '''))
            if userInput==1:
                uchoice='rock'
            elif userInput==2:
                uchoice='paper'
            elif userInput==3:
                uchoice='scissor'

            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("user value", uchoice)
                print("computer value", Cchoice)
                print("game is draw")

            elif (uchoice=='rock' and Cchoice=='scissor') or (uchoice=='scissor' and Cchoice=='paper') or(uchoice=='paper' and Cchoice=='rock'):
                print("user value", uchoice)
                print("computer value", Cchoice)
                print("you win")
                ucount=ucount+1

            else:
                print("user value", uchoice)
                print("computer value", Cchoice)
                print("computer win")
                ccount=ccount+1

            if ucount==ccount:
                print("user score",ucount)
                print("computer score", ccount)
                print("match is draw")

            elif ucount > ccount:
                print("user score",ucount)
                print("computer score", ccount)
                print("you win the game")

            else:
                print("user score",ucount)
                print("computer score", ccount)
                print("computer win the game")

            
    else:
        break