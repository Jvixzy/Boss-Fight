# Boss fight with a % detertmining wether or not your attack lands
import random, time

swordPercentage = random.randint(1,100)
bowPercentage = random.randint(1,100)
devilPercentage = random.randint(1,100)
 
def attackMiss():
    print('Your attack has missed!')
    return True

def displayDevilHP(devilHP):
    print(f'The devils current hp is {devilHP}')
    return devilHP

def displayUserHealth(playerHP):
    print(f'Your current health {playerHP}')
    return playerHP
    
def percentageChange():
    global bowPercentage, swordPercentage
    swordPercentage = random.randint(1,100)
    bowPercentage = random.randint(1,100)

def devilDeath(devilHP):
    if devilHP == 0:
        print('The devil has fallen!')
    return True


playerHP = 100
devilHP = 100

print('A tall man stands before you, horns emerging from his head and wings unlike anything youve never seen before')
time.sleep(2)
print('You approach the figure with your sword drawn?')
time.sleep(1.5)

while True:
    print('What do you decide to do?')
    print(f'1. Attack the devil with your sword (Percentage to hit is {swordPercentage}/100)')
    print(f'2. Attack the devil with your bow (Percentage to hit is {bowPercentage}/100)')
    print('3. Check health')
    userAction = input()

    if userAction == '1':
        hitRoll = random.randint(1,100)
        if swordPercentage >= hitRoll:
            healthLoss = random.randint(1,15)
            time.sleep(1)
            print(f'Your attack lands on the creature dealing {healthLoss} damage.')
            devilHP = devilHP - healthLoss
            displayDevilHP(devilHP)
            break        
        else:
            attackMiss()
            break

    elif userAction == '2':
        hitRoll = random.randint(1,100)
        if bowPercentage >= hitRoll:
            healthLoss = random.randint(1,15)
            time.sleep(1)
            print(f'Your arrow strikes the devil dealing {healthLoss} damage.')
            devilHP = devilHP - healthLoss
            displayDevilHP(devilHP)
            break
        else:
            attackMiss()
            break

    elif userAction == '3':
        displayUserHealth(playerHP)
        continue

    else:
        print('Please enter a valid input!')
        time.sleep(1.5)
        continue

time.sleep(1.5)
print('The devil takes up a stance to strike you!')
hitRollDevil = random.randint(1,100)
if devilPercentage >= hitRollDevil:
    playerHealthLoss = random.randint(1,20)
    playerHP = playerHP - playerHealthLoss
    time.sleep(1.5)
    displayUserHealth(playerHP)
else:
    time.sleep(1)
    print('The devils attack has missed you!')

time.sleep(1.5)
percentageChange()
while True:
    print('You see an opening to attack the devil after his strike')
    print(f'1. Attack the devil with your sword (Percentage to hit is {swordPercentage}/100)')
    print(f'2. Attack the devil with your bow (Percentage to hit is {bowPercentage}/100)')
    print('3. Check health')
    userAction = input()

    if userAction == '1':
        hitRoll = random.randint(1,100)
        if swordPercentage >= hitRoll:
            healthLoss = random.randint(1,15)
            time.sleep(1)
            print(f'Your attack lands on the creature dealing {healthLoss} damage.')
            devilHP = devilHP - healthLoss
            displayDevilHP(devilHP)
            break
        else:
            attackMiss()
            break

    elif userAction == '2':
        hitRoll = random.randint(1,100)
        if bowPercentage >= hitRoll:
            healthLoss = random.randint(1,15)
            time.sleep(1)
            print(f'Your arrow strikes the devil dealing {healthLoss} damage.')
            devilHP = devilHP - healthLoss
            displayDevilHP(devilHP)
            break
        else:
            attackMiss()
            break

    elif userAction == '3':
      displayUserHealth(playerHP)
      continue

    else:
        print('Please select a valid input!')
        time.sleep(1.5)
        continue

if attackMiss == True:
    print('As your attack misses the devil, he begins to pull out a mystery weapon!')
else:
    print('As you finish up your attack the devil begins to unval a mystery weapon!') # If above condition is false
time.sleep(1.5)
print('The Devil unleashes a staff!')
time.sleep(1.5)
print('A staff? You think you yourself')
time.sleep(1.5)
print('Just as your thought wraps up the Devil slams the staff onto the ground')
time.sleep(1.5)
print('All of a suden the ground begins to shake!')
time.sleep(1.5)
print('3 Skeletons have just arisen out of the ground!')
time.sleep(1.5)

skeleton1HP = 20
skeleton2HP = 20
skeleton3HP = 25

while True:
    print('What is your next action?')
    print('1. Attack Skeleton 1')
    print('2. Attack Skeleton 2')
    print('3. Attack Skeleton 3')
    print('4. Attack the Devil')
    print('5. Check your health')
    userAction2 = input()

    if userAction2 == '1':
        break
    elif userAction2 == '2':
        break
    elif userAction2 == '3':
        break
    elif userAction2 == '4':
        break
    elif userAction2 == '5':
        displayUserHealth(playerHP)
        continue
    else:
        print('Please enter a valid input!')
        continue

percentageChange()

while True:
    if userAction2 == '1':
        print('You are attaking skeleton 1')
        print(f'1. Attack with your sword ({swordPercentage}/100)')
        print(f'2. Attack with your bow ({bowPercentage}/100)')
        userAction3 = input()
    
        if userAction3 == '1':
            hitRoll = random.randint(1,100)
            if swordPercentage >= hitRoll:
                skeletonHealthLoss1 = random.randint(1,12)
                skeleton1HP = skeleton1HP - skeletonHealthLoss1
                print(f'Your attack does {skeletonHealthLoss1} damage to the skeleton!')
                print(f'This skeletons current health is {skeleton1HP}')
                break
            else:
                attackMiss()
        elif userAction3 == '2':
            hitRoll = random.randint(1,100)
            if bowPercentage >= hitRoll:
                skeletonHealthLoss1 = random.randint(1,12)
                skeleton1HP = skeleton1HP - skeletonHealthLoss1
                print(f'Your attack does {skeletonHealthLoss1} damage to the skeleton!')
                print(f'This skeletons current health is {skeleton1HP}')
                break
            else:
                attackMiss()
        else:
            print('Input invalid!')
            continue

    if userAction2 == '2':
        print('You are attaking skeleton 2')
        print(f'1. Attack with your sword ({swordPercentage}/100)')
        print(f'2. Attack with your bow ({bowPercentage}/100)')
        userAction3 = input()
    
        if userAction3 == '1':
            hitRoll = random.randint(1,100)
            if swordPercentage >= hitRoll:
                skeletonHealthLoss2 = random.randint(1,12)
                skeleton2HP = skeleton2HP - skeletonHealthLoss2
                print(f'Your attack does {skeletonHealthLoss2} damage to the skeleton!')
                print(f'This skeletons current health is {skeleton2HP}')
                break
            else:
                attackMiss()
        elif userAction3 == '2':
            hitRoll = random.randint(1,100)
            if bowPercentage >= hitRoll:
                skeletonHealthLoss2 = random.randint(1,12)
                skeleton2HP = skeleton2HP - skeletonHealthLoss2
                print(f'Your attack does {skeletonHealthLoss2} damage to the skeleton!')
                print(f'This skeletons current health is {skeleton2HP}')
                break
            else:
                attackMiss()
        else:
            print('Input invalid!')
            continue

    if userAction2 == '3':
        print('You are attaking skeleton 3')
        print(f'1. Attack with your sword ({swordPercentage}/100)')
        print(f'2. Attack with your bow ({bowPercentage}/100)')
        userAction3 = input()
    
        if userAction3 == '1':
            hitRoll = random.randint(1,100)
            if swordPercentage >= hitRoll:
                skeletonHealthLoss3 = random.randint(1,12)
                skeleton3HP = skeleton3HP - skeletonHealthLoss3
                print(f'Your attack does {skeletonHealthLoss3} damage to the skeleton!')
                print(f'This skeletons current health is {skeleton3HP}')
                break
            else:
                attackMiss()
        elif userAction3 == '2':
            hitRoll = random.randint(1,100)
            if bowPercentage >= hitRoll:
                skeletonHealthLoss3 = random.randint(1,12)
                skeleton3HP = skeleton3HP - skeletonHealthLoss3
                print(f'Your attack does {skeletonHealthLoss3} damage to the skeleton!')
                print(f'This skeletons current health is {skeleton3HP}')
                break
            else:
                attackMiss()
        else:
            print('Input invalid!')
            continue

    if userAction2 == '4':
        hitRoll = random.randint(1,100)
        if swordPercentage >= hitRoll:
            healthLoss = random.randint(1,15)
            time.sleep(1)
            print(f'Your attack lands on the creature dealing {healthLoss} damage.')
            devilHP = devilHP - healthLoss
            displayDevilHP(devilHP)
            time.sleep(1)
            devilDeath(devilHP)
            break
        else:
            attackMiss()

        



        




        

        


    

            