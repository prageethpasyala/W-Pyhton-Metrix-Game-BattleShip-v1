# @PKPasyala_2022

import numpy as np
import boto3
import time

# Create an object for dynamoDB
dynamodb = boto3.resource('dynamodb',region_name='eu-west-2')
# Select your specific table
table = dynamodb.Table("Coordinates")
print("\n")
print(" WELCOME TO Python BattleShip Game ")
player = input("Would you like to play Pirate or Captain [p | c] ? : \n")

if player == "p":
    print("[PIRATE]")
    print("Enter your coordinates to deploy your pirates ships. Example. 2 2")
    print("Note: Please enter your digits between 0 to 4 ")
    # a=int(input("Number of elements in the array:-"))
    c1=list(map(int, input("1st Cordinate :  ").strip().split()))
    c2=list(map(int, input("2nd Cordinate :  ").strip().split()))
    c3=list(map(int, input("3rd Cordinate :  ").strip().split()))
    print("\n")
    print("Your coordinates are")
    print(c1,c2,c3)

    # Write:
    table.put_item(Item= {'id': '1', 'codin10': str(c1[0]), 'codin11': str(c1[1]) , 'codin20' : str(c2[0]), 'codin21': str(c2[1]), 'codin30': str(c3[0]), 'codin31': str(c3[1]) })
   
    # NumPy array
    A = np.array([  [1, 2, 3, 4, 5], 
                    [6, 7, 8, 9, 10],
                    [11, 12, 13, 14, 15],
                    [16, 17, 18, 19, 20],
                    [21, 22, 23, 24, 25] ])
                    
    # print(A)
    print("\n")
    shipCordinate1 = A[c1[0]][c1[1]]
    shipCordinate2 = A[c2[0]][c2[1]]
    shipCordinate3 = A[c3[0]][c3[1]]
    # print("First Pirate ship located in Area : " + str(shipCordinate1))
    # print("Second Pirate ship located in Area : " + str(shipCordinate2))
    # print("Third Pirate ship located in Area : " + str(shipCordinate3))
    
    print("Your Pirate ships are deployed [S] : \n")
    BB = np.array([  ['*', '*', '*', '*', '*'], 
                    ['*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*'] ])
    BB[c1[0]][c1[1]] = 'S'
    BB[c2[0]][c2[1]] = 'S'
    BB[c3[0]][c3[1]] = 'S'
    print(BB)
    print("------------------------------ \n")
elif player == "c":
    # print("C")

    # NumPy array
    A = np.array([  [1, 2, 3, 4, 5], 
                    [6, 7, 8, 9, 10],
                    [11, 12, 13, 14, 15],
                    [16, 17, 18, 19, 20],
                    [21, 22, 23, 24, 25] ])
    print("------------------------------ \n")                
   
    # Get item
    response = table.get_item(Key={'id': '1' })
    p_coordinates10 = int(response['Item']['codin10'])
    p_coordinates11 = int(response['Item']['codin11'])
    p_coordinates20 = int(response['Item']['codin20'])
    p_coordinates21 = int(response['Item']['codin21'])
    p_coordinates30 = int(response['Item']['codin30'])
    p_coordinates31 = int(response['Item']['codin31'])

    PshipCordinate1 = A[p_coordinates10][p_coordinates11]
    PshipCordinate2 = A[p_coordinates20][p_coordinates21]
    PshipCordinate3 = A[p_coordinates30][p_coordinates31]

    PShipCoordinateList = [PshipCordinate1, PshipCordinate2, PshipCordinate3]

    # print(p_coordinates31)
    # print(p_coordinates11)
    print("Enter your coordinates to set target for pirates ships. Example. 2 2")
    print("Note: Please enter your digits between 0 to 4 ")
    # a=int(input("Number of elements in the array:-"))
    cc1=list(map(int, input("1st Cordinate : ").strip().split()))
    cc2=list(map(int, input("2nd Cordinate : ").strip().split()))
    cc3=list(map(int, input("3rd Cordinate : ").strip().split()))
    print("\n")
    print("Your coordinates are")
    print(cc1,cc2,cc3)

    TargetArea1 = A[cc1[0]][cc1[1]]
    TargetArea2 = A[cc2[0]][cc2[1]]
    TargetArea3 = A[cc3[0]][cc3[1]]
    print ("\n")

    print("....ITS BATTLE TIME....")
    choice = input("Ready for launch Torpedos ?  y | n : ")

    B = np.array([  ['*', '*', '*', '*', '*'], 
                    ['*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*'] ])

    B[p_coordinates10][p_coordinates11] = 'S'
    B[p_coordinates20][p_coordinates21] = 'S'
    B[p_coordinates30][p_coordinates31] = 'S'
    B[cc1[0]][cc1[1]] = '@'
    B[cc2[0]][cc2[1]] = '@'
    B[cc3[0]][cc3[1]] = '@'
    print("\n")
    print("Map layout : [S]-Pirate Ship  [@]-Target")
    print("------------------------")
    print(B)
    print("\n")


    if choice == "y":
        # print(shipCordinate1,shipCordinate2,shipCordinate3)
        TargetAreas = [TargetArea1, TargetArea2, TargetArea3]
        TargetAreaList = set(TargetAreas) & set(PShipCoordinateList)
        # print(TargetAreaList)
        if len(TargetAreaList):
            print("BOOOOM! WELLDONE, YOU HAVE DISTROYED "+str(len(TargetAreaList))+" PIRATE SHIP")
 
        else:
                print("YOU MISSED, RECALCULATE YOUR COORDINATES, TRY AGAIN!")

    elif choice == "N":
        exit()
    else:
        print("Use lower cap or wrong letter")

else:
    print("Use lower cap or wrong letter ")


