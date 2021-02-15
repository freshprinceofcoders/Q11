'''
product_grid = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
for prodct_grids in product_grid:
    if 

# Skeleton Program code for the AQA COMP1 Summer 2015 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA COMP1 Programmer Team
# developed in the Python 3.4 programming environment

BOARDDIMENSION = 8


def CreateBoard():
  Board = []
  for Count in range(BOARDDIMENSION + 1):
    Board.append([])
    for Count2 in range(BOARDDIMENSION + 1):# this is making the board without any lines using white spaces
      Board[Count].append("  ")
  return Board

def DisplayWhoseTurnItIs(WhoseTurn):
  if WhoseTurn == "W":
    print("It is White's turn") # this is using if statement to check who's turn it is
  else:
    print("It is Black's turn")

def GetTypeOfGame():
  TypeOfGame = input("Do you want to play the sample game (enter Y for Yes)? ")#This is making an input to ask if you want to play a sample 
  return TypeOfGame

def DisplayWinner(WhoseTurn):
  if WhoseTurn == "W":
    print("Black's Sarrum has been captured.  White wins!")#This just workes out the winner
  else:
    print("White's Sarrum has been captured.  Black wins!")

def CheckIfGameWillBeWon(Board, FinishRank, FinishFile):
  if Board[FinishRank][FinishFile][1] == "S":#this is where if the finish rank and finish file and the 1 nummber in that array equals s then it will print True
    return True
  else:
    return False

def DisplayBoard(Board):
  print()
  for RankNo in range(1, BOARDDIMENSION + 1):
    print("     _______________________")
    print(RankNo, end="   ")
    for FileNo in range(1, BOARDDIMENSION + 1):#this is making the board with lines
      print("|" + Board[RankNo][FileNo], end="")
    print("|")
  print("     _______________________")
  print()
  print("      1  2  3  4  5  6  7  8")# And the cooridinates for the board on the axis
  print()
  print()    

def CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, ColourOfPiece):
  CheckRedumMoveIsLegal = False#Setting the illegal move to false
  if ColourOfPiece == "W":
    if FinishRank == StartRank - 1:
      if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":#this is just setting the rules out and if the player does this then the move is illegal for each peice
        CheckRedumMoveIsLegal = True
      elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":#abs returns a number as a float and has no negativies
        CheckRedumMoveIsLegal = True
  elif FinishRank == StartRank + 1:#this is another condition that say if the finish rank is one away from start rank then move is not legal
    if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
      CheckRedumMoveIsLegal = True
    elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "W":
      CheckRedumMoveIsLegal = True
  return CheckRedumMoveIsLegal

def CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckSarrumMoveIsLegal = False
  if abs(FinishFile - StartFile) <= 1 and abs(FinishRank - StartRank) <= 1:
    CheckSarrumMoveIsLegal = True #this is just checking weather the user has done the right move with the sarrum and if the move is not tight thenn it will return True
  return CheckSarrumMoveIsLegal

def CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  GisgigirMoveIsLegal = False
  RankDifference = FinishRank - StartRank#this just caluculates the differences 
  FileDifference = FinishFile - StartFile
  if RankDifference == 0:#moves horizontally
    if FileDifference >= 1:#moving right
      GisgigirMoveIsLegal = True
      for Count in range(1, FileDifference):#checking its blank by increasing the file and adda the count each time to startfile 
        if Board[StartRank][StartFile + Count] != "  ":#if the square is not a blank then its false
          GisgigirMoveIsLegal = False
    elif FileDifference <= -1:#moving left
      GisgigirMoveIsLegal = True# this whole function checks if the move that is being made on the board is right 
      for Count in range(-1, FileDifference, -1):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
  elif FileDifference == 0:
    if RankDifference >= 1:#going down
      GisgigirMoveIsLegal = True
      for Count in range(1, RankDifference):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
    elif RankDifference <= -1:#going up
      GisgigirMoveIsLegal = True
      for Count in range(-1, RankDifference, -1):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
  return GisgigirMoveIsLegal

def CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckNabuMoveIsLegal = False
  if abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 1:#moving diagonal one place and when it moves diagonal the start and finish rank have to move the same number of spaces
    CheckNabuMoveIsLegal = True# this whole function checks if the move that is being made on the board is right 
  return CheckNabuMoveIsLegal

def CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckMarzazPaniMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) ==1):
    CheckMarzazPaniMoveIsLegal = True#this cecks the magnitude
  return CheckMarzazPaniMoveIsLegal# this whole function checks if the move that is being made on the board is right 

def CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckEtluMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) == 2):
    CheckEtluMoveIsLegal = True
  return CheckEtluMoveIsLegal# this whole function checks if the move that is being made on the board is right 

def CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  MoveIsLegal = True
  if (FinishFile == StartFile) and (FinishRank == StartRank):#not legal as it finished where it started
    MoveIsLegal = False
  else:
    PieceType = Board[StartRank][StartFile][1]#this prints the second character
    PieceColour = Board[StartRank][StartFile][0]#this prints the first character
    if WhoseTurn == "W":
      if PieceColour != "W":
        MoveIsLegal = False
      if Board[FinishRank][FinishFile][0] == "W":#if you land on another piece that is white it is illegal
        MoveIsLegal = False# this whole function checks if the piece can be moved to a certain place 
    else:
      if PieceColour != "B":
        MoveIsLegal = False
      if Board[FinishRank][FinishFile][0] == "B":#if you land on another piece that is black it is illegal
        MoveIsLegal = False
    if MoveIsLegal == True:
      if PieceType == "R":
        MoveIsLegal = CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, PieceColour)
      elif PieceType == "S":
        MoveIsLegal = CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)#this just assigns the piece type to the piece
      elif PieceType == "M":
        MoveIsLegal = CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "G":
        MoveIsLegal = CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "N":
        MoveIsLegal = CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "E":
        MoveIsLegal = CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
  return MoveIsLegal

def InitialiseBoard(Board, SampleGame):
  if SampleGame == "Y":
    for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):#this makes the board for the sample
        Board[RankNo][FileNo] = "  "
    Board[1][2] = "BG"
    Board[1][4] = "BS"
    Board[1][8] = "WG" # this is settiing out where the piecies start on the board 
    Board[2][1] = "WR"
    Board[3][1] = "WS"
    Board[3][2] = "BE"
    Board[3][8] = "BE"
    Board[6][8] = "BR"
  else:
    for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):
        if RankNo == 2:
          Board[RankNo][FileNo] = "BR"
        elif RankNo == 7:
          Board[RankNo][FileNo] = "WR"
        elif RankNo == 1 or RankNo == 8:
          if RankNo == 1:
            Board[RankNo][FileNo] = "B"
          if RankNo == 8:
            Board[RankNo][FileNo] = "W"
          if FileNo == 1 or FileNo == 8:#This is the cooridinates that needs a letter added to 
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "G"#this is adding the "G" to the coordinates on the board and adding the letter G  next to the letter B or W
          elif FileNo == 2 or FileNo == 7:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "E"
          elif FileNo == 3 or FileNo == 6:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "N"
          elif FileNo == 4:# There is one here as there is onlyone position to put it in
            if RankNo == 1:
              Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
            else:
              Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
          elif FileNo == 5:
            if RankNo ==1:#this is black 
              Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"#this makes it m if it is black 
            else:
              Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"#else leaves it
        else:
          Board[RankNo][FileNo] = "  "    
                    
def GetMove(StartSquare, FinishSquare):
  StartSquare = int(input("Enter coordinates of square containing piece to move (file first): "))#this ask you for the coordinates and then executute it and then check the other conditions to check if it is legal
  FinishSquare = int(input("Enter coordinates of square to move piece to (file first): "))
  return StartSquare, FinishSquare

def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  colour = "not_known"
  if Board[FinishRank][FinishFile][0] == "W":
    colour = "White"
  elif Board[FinishRank][FinishFile][0] == "B":
    colour = "Black"
  
  piece = "not_known"
  if Board[FinishRank][FinishFile][1] == "R":
    piece = "Redum"
  elif Board[FinishRank][FinishFile][1] == "S":
    piece = "Sarrum"
  elif Board[FinishRank][FinishFile][1] == "M":
    piece = "Marrzaz Pani"
  elif Board[FinishRank][FinishFile][1] == "G":
    piece = "Gisgigir"
  elif Board[FinishRank][FinishFile][1] == "N":
    piece = "Nabu"
  elif Board[FinishRank][FinishFile][1] == "E":
    piece = "Etlu"  
  
  if WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":#this is here to change the redum into a marzaz pani and if the finish rank is 1 and the colour is white and a redum it changes amd the new name of it is "WM"
    Board[FinishRank][FinishFile] == "WM"
    Board[StartRank][StartFile] = "  "

  elif WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":#this is changing the black redum into a marzaz pani if the redum has reached finish rank 8 so the first line of the white side
    Board[FinishRank][FinishFile] == "BM"
    Board[StartRank][StartFile] = "  "

  else:
    Board[FinishRank][FinishFile] = Board[StartRank][StartFile]
    Board[StartRank][StartFile] = "  "
  if colour != "not_known" and piece != "not_known":
    print(f" The colour {colour} and the piece {piece} was captured!")
  return colour, piece  

def GetTypeOfGame():
  SampleGame = input("Do you want to play the sample game (enter Y for Yes)? ")#asks if you want to play sample game
  if ord(SampleGame) >= 97 and ord(SampleGame) <= 122:#This checks to see if the letter is Y and if it is not then it returns no sample board
    SampleGame = chr(ord(SampleGame) - 32)
  return SampleGame#you need to return it

def GetPositions(StartSquare, FinishSquare):
  StartRank = StartSquare % 10#if the start rank was 14 then the answer would be 1
  StartFile = StartSquare // 10#the answer here would be 1
  FinishRank = FinishSquare % 10
  FinishFile = FinishSquare // 10
  return StartRank,StartFile,FinishRank,FinishFile

if __name__ == "__main__":#This is the main bit and this is where the actual game begins and the methds are all called here
  Board = CreateBoard() #
  StartSquare = 0 #
  FinishSquare = 0
  PlayAgain = "Y"
  

  
  while PlayAgain == "Y":#
    WhoseTurn = "W"
    GameOver = False#
    SampleGame = GetTypeOfGame()#
    InitialiseBoard(Board, SampleGame)
    while not(GameOver):
      
      DisplayBoard(Board)#print board
      
      DisplayWhoseTurnItIs(WhoseTurn) #says whose turn it is 
      MoveIsLegal = False#setting boolean
      while not(MoveIsLegal):
        StartSquare, FinishSquare = GetMove(StartSquare, FinishSquare)
        StartRank,StartFile,FinishRank,FinishFile  = GetPositions(StartSquare,FinishSquare)
        if not(MoveIsLegal):
          print("That is not a legal move - please try again")#this is just calling the method and printing a message if it is not met
      GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)
      colour, piece = MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
      if GameOver:
        DisplayWinner(WhoseTurn)
      if WhoseTurn == "W":#this is a condition if if this condition is met then whoseTurn = b else it = w
        WhoseTurn = "B"
      else:
        WhoseTurn = "W"
    PlayAgain = input("Do you want to play again (enter Y for Yes)? ")#checks if you want to play again
    if ord(PlayAgain) >= 97 and ord(PlayAgain) <= 122:#checking to see if your using y or not
      PlayAgain = chr(ord(PlayAgain) - 32)
'''
# Skeleton Program code for the AQA COMP1 Summer 2015 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA COMP1 Programmer Team
# developed in the Python 3.4 programming environment

BOARDDIMENSION = 8

def CreateBoard():
  Board = []
  for Count in range(BOARDDIMENSION + 1):
    Board.append([])
    for Count2 in range(BOARDDIMENSION + 1):
      Board[Count].append("  ")
  return Board

def DisplayWhoseTurnItIs(WhoseTurn):
  if WhoseTurn == "W":
    print("It is White's turn")
  else:
    print("It is Black's turn")

def GetTypeOfGame():
  SampleGame = input("Do you want to play the sample game (enter Y for Yes)? ")#asks if you want to play sample game
  if ord(SampleGame) >= 97 and ord(SampleGame) <= 122:#This checks to see if the letter is Y and if it is not then it returns no sample board
    SampleGame = chr(ord(SampleGame) - 32)
  return SampleGame#you need to return it

def GetTypeOfGame():
  TypeOfGame = input("Do you want to play the sample game (enter Y for Yes)? ")
  return TypeOfGame

def DisplayWinner(WhoseTurn):
  if WhoseTurn == "W":
    print("Black's Sarrum has been captured.  White wins!")
  else:
    print("White's Sarrum has been captured.  Black wins!")

def CheckIfGameWillBeWon(Board, FinishRank, FinishFile):
  if Board[FinishRank][FinishFile][1] == "S":
    return True
  else:
    return False

def DisplayBoard(Board):
  print()
  for RankNo in range(1, (BOARDDIMENSION + 1) + 1):
    print("     _______________________")
    FileNoRow = False
    if RankNo == BOARDDIMENSION + 1:#prints it including the 9
      FileNoRow = True
      print("", end="    ")#prints it sideways
    else:
      print(RankNo, end="   ")#goes to this to get rid of 9th one
    for FileNo in range(1, BOARDDIMENSION + 1):
      if FileNoRow:
        print(" " + str(FileNo) + " ", end="")#prints spaces between words 
      else:
        print("|" + Board[RankNo][FileNo], end="")
    if FileNoRow:
      print("")#gets rid of vertical line at the end
    else:
      print("|")
  print()
  print()
  print()
  
def CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, ColourOfPiece):
  CheckRedumMoveIsLegal = False
  if ColourOfPiece == "W":
    if FinishRank == StartRank - 1:
      if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
        CheckRedumMoveIsLegal = True
      elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
        CheckRedumMoveIsLegal = True
  elif FinishRank == StartRank + 1:
    if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
      CheckRedumMoveIsLegal = True
    elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "W":
      CheckRedumMoveIsLegal = True
  return CheckRedumMoveIsLegal

def CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckSarrumMoveIsLegal = False
  if abs(FinishFile - StartFile) <= 1 and abs(FinishRank - StartRank) <= 1:
    CheckSarrumMoveIsLegal = True
  return CheckSarrumMoveIsLegal

def CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  GisgigirMoveIsLegal = False
  RankDifference = FinishRank - StartRank
  FileDifference = FinishFile - StartFile
  if RankDifference == 0:
    if FileDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, FileDifference):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
    elif FileDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, FileDifference, -1):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
  elif FileDifference == 0:
    if RankDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, RankDifference):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
    elif RankDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, RankDifference, -1):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
  return GisgigirMoveIsLegal

def CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckNabuMoveIsLegal = False
  if abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 1:
    CheckNabuMoveIsLegal = True
  return CheckNabuMoveIsLegal

def CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckMarzazPaniMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) ==1):
    CheckMarzazPaniMoveIsLegal = True
  return CheckMarzazPaniMoveIsLegal

def CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckEtluMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) == 2):
    CheckEtluMoveIsLegal = True
  return CheckEtluMoveIsLegal

def CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  MoveIsLegal = True
  if (FinishFile == StartFile) and (FinishRank == StartRank):
    MoveIsLegal = False
  else:
    PieceType = Board[StartRank][StartFile][1]
    PieceColour = Board[StartRank][StartFile][0]
    if WhoseTurn == "W":
      if PieceColour != "W":
        MoveIsLegal = False
      if Board[FinishRank][FinishFile][0] == "W":
        MoveIsLegal = False
    else:
      if PieceColour != "B":
        MoveIsLegal = False
      if Board[FinishRank][FinishFile][0] == "B":
        MoveIsLegal = False
    if MoveIsLegal == True:
      if PieceType == "R":
        MoveIsLegal = CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, PieceColour)
      elif PieceType == "S":
        MoveIsLegal = CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "M":
        MoveIsLegal = CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "G":
        MoveIsLegal = CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "N":
        MoveIsLegal = CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "E":
        MoveIsLegal = CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
  return MoveIsLegal

def InitialiseBoard(Board, SampleGame):
  if SampleGame == "Y":
    for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):#this makes the board for the sample
        Board[RankNo][FileNo] = "  "
    Board[1][2] = "BG"
    Board[1][4] = "BS"
    Board[1][8] = "WG" # this is settiing out where the piecies start on the board 
    Board[2][1] = "WR"
    Board[3][1] = "WS"
    Board[3][2] = "BE"
    Board[3][8] = "BE"
    Board[6][8] = "BR"
  else:
    for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):
        if RankNo == 2:
          Board[RankNo][FileNo] = "BR"
        elif RankNo == 7:
          Board[RankNo][FileNo] = "WR"
        elif RankNo == 1 or RankNo == 8:
          if RankNo == 1:
            Board[RankNo][FileNo] = "B"
          if RankNo == 8:
            Board[RankNo][FileNo] = "W"
          if FileNo == 1 or FileNo == 8:#This is the cooridinates that needs a letter added to 
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "G"#this is adding the "G" to the coordinates on the board and adding the letter G  next to the letter B or W
          elif FileNo == 2 or FileNo == 7:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "E"
          elif FileNo == 3 or FileNo == 6:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "N"
          elif FileNo == 4:# There is one here as there is onlyone position to put it in
            if RankNo == 1:
              Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
            else:
              Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
          elif FileNo == 5:
            if RankNo ==1:#this is black 
              Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"#this makes it m if it is black 
            else:
              Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"#else leaves it
        else:
          Board[RankNo][FileNo] = "  "    
                    
def GetMove(StartSquare, FinishSquare):
  StartSquare = int(input("Enter coordinates of square containing piece to move (file first): "))
  FinishSquare = int(input("Enter coordinates of square to move piece to (file first): "))
  return StartSquare, FinishSquare

def GetPositions(StartSquare, FinishSquare):
  StartRank = StartSquare % 10#if the start rank was 14 then the answer would be 1
  StartFile = StartSquare // 10#the answer here would be 1
  FinishRank = FinishSquare % 10
  FinishFile = FinishSquare // 10
  return StartRank,StartFile,FinishRank,FinishFile

            
  
def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  destinationPeice = Board[FinishRank][FinishFile] #Storing the position of the previous piece that is there
  if WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "WM"
    Board[StartRank][StartFile] = "  "
  elif WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "BM"
    Board[StartRank][StartFile] = "  "
  else:
    Board[FinishRank][FinishFile] = Board[StartRank][StartFile]
    Board[StartRank][StartFile] = "  "
    
    if destinationPeice != "  ":#If there is no space to where your going to move to then print destination piece
      print("Captured! ", destinationPeice)


def CheckMoveIsValid (StartRank, StartFile, FinishFile,FinishRank):
    if BOARDDIMENSION < FinishFile or  BOARDDIMENSION < FinishRank or  BOARDDIMENSION < StartRank or  BOARDDIMENSION < StartFile:
        print("This move is not valid.")
        return False
    else:
        print("This is a valid move.", StartRank, StartFile, FinishFile,FinishRank, BOARDDIMENSION)
        return True

if __name__ == "__main__":
  Board = CreateBoard() 
  StartSquare = 0 
  FinishSquare = 0
  PlayAgain = "Y"
  while PlayAgain == "Y":
    WhoseTurn = "W"
    GameOver = False
    SampleGame = GetTypeOfGame()
    InitialiseBoard(Board, SampleGame)
    while not(GameOver):
        DisplayBoard(Board)
        DisplayWhoseTurnItIs(WhoseTurn)
        MoveIsLegal = False
        MoveIsValid = False
        while not(MoveIsValid) or not(MoveIsLegal):#this is looping through move is valid and legal until both conditions are meet
            StartSquare, FinishSquare = GetMove(StartSquare, FinishSquare)
            StartRank,StartFile,FinishRank,FinishFile  = GetPositions(StartSquare,FinishSquare)
            print("Checking move is valid...")
            MoveIsValid = CheckMoveIsValid(StartRank, StartFile, FinishFile,FinishRank)
            if MoveIsValid == True:#this is saying that if the move is valid then check if it is legal
                MoveIsLegal = CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
                if not(MoveIsLegal):
                    print("That is not a legal move - please try again")
        GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)
        MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
        if GameOver:
          DisplayWinner(WhoseTurn)
        if WhoseTurn == "W":
          WhoseTurn = "B"
        else:
          WhoseTurn = "W"
    PlayAgain = input("Do you want to play again (enter Y for Yes)? ")
    if ord(PlayAgain) >= 97 and ord(PlayAgain) <= 122:
      PlayAgain = chr(ord(PlayAgain) - 32)



