# Skeleton Program code for the AQA COMP1 Summer 2015 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA COMP1 Programmer Team
# developed in the Python 3.4 programming environment
import csv

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
  SampleGame = input("Do you want to play the sample game (enter Y for Yes, L/l for Loading saved game.)? ")
  if ord(SampleGame) >= 97 and ord(SampleGame) <= 122:
    SampleGame = chr(ord(SampleGame) - 32)
  return SampleGame

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

def GetSavedGame():
  board = []
  with open('C:/Users/milan/OneDrive/Desktop/project euler/Q11/test.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
      del row[-1]      
      board.append(row)
    del board[-1]
  return board

def InitialiseBoard(Board, SampleGame):
  if SampleGame == "L" or SampleGame == "l":
    return GetSavedGame()
  else:
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
  return Board

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

def SaveGame(Board, WhoseTurn):
  with open ("C:/Users/milan/OneDrive/Desktop/project euler/Q11/test.csv","w", newline='') as filedata:
    writer = csv.DictWriter(filedata, skipinitialspace=True, delimiter=',', fieldnames=['0', '1','2','3','4','5','6','7','8', '9']) 
    print('*** Board:',Board)
    for row in Board:
      newRow = {}
      for i in range(0,9):
        newRow[str(i)] = row[i]
      writer.writerow(newRow)
    writer.writerow({ '0': WhoseTurn })


if __name__ == "__main__":
  Board = CreateBoard() 
  StartSquare = 0 
  FinishSquare = 0
  PlayAgain = "Y"
  while PlayAgain == "Y":
    WhoseTurn = "W"
    GameOver = False
    SampleGame = GetTypeOfGame()
    initialiseBoard = InitialiseBoard(Board, SampleGame)
    while not(GameOver):
        print('Just before Diaplsy method 2 ----', Board, initialiseBoard)
        DisplayBoard(initialiseBoard)
        DisplayWhoseTurnItIs(WhoseTurn)
        MoveIsLegal = False
        MoveIsValid = False
        while not(MoveIsValid) or not(MoveIsLegal):#this is looping through move is valid and legal until both conditions are meet
            StartSquare, FinishSquare = GetMove(StartSquare, FinishSquare)
            if StartSquare == -1:
              SaveGame(initialiseBoard,WhoseTurn)
            StartRank,StartFile,FinishRank,FinishFile  = GetPositions(StartSquare,FinishSquare)
            print("Checking move is valid...")
            MoveIsValid = CheckMoveIsValid(StartRank, StartFile, FinishFile,FinishRank)
            if MoveIsValid == True:#this is saying that if the move is valid then check if it is legal
                MoveIsLegal = CheckMoveIsLegal(initialiseBoard, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
                if not(MoveIsLegal):
                    print("That is not a legal move - please try again")
        GameOver = CheckIfGameWillBeWon(initialiseBoard, FinishRank, FinishFile)
        MakeMove(initialiseBoard, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
        if GameOver:
          DisplayWinner(WhoseTurn)
        if WhoseTurn == "W":
          WhoseTurn = "B"
        else:
          WhoseTurn = "W"
    PlayAgain = input("Do you want to play again (enter Y for Yes)? ")
    if ord(PlayAgain) >= 97 and ord(PlayAgain) <= 122:
      PlayAgain = chr(ord(PlayAgain) - 32)



