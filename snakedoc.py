#work on security

#Import Statements
import sys

path = ""
validExtensions = ["ino", "cpp", "INO", "CPP"]
variableDeclarationTypes = ["double", "int", "String", "bool", "float", "char", "Integer", "long", "unsigned", "Integer", "void", "string"]
documentedConstants = []
documentedVariables = []
documentedFunctions = []
currentLineIndex = 0

"""
***************************************************************
CLASS NAME:
	
  Library
  
DESCRIPTION:
	
  Object that repersents an imported library with the name of the imported file and description of usage in the program
  
*************************************************************** 
"""
class Library:
  
  """
  Function Name:
  
  	__init__

	Description:
  
  	Constructor for Library
    
  Variables:
  
  	String  name  the name of the imported library
   String  description  description of usage in the program
  """
  def __init__(self):
    self._name = ""
    self._description = ""
    
  def setName(self, name):
    self._name = name
    
  def setDescription(self, description):
     self._desription = description
      
  def getName(self):
    return self._name
    
  def getDescription(self):
     return self._description
    
  name = property(getName, setName)
  description = property(getDescription, setDescription)

      
"""
***************************************************************
CLASS NAME:
	
  Variable
  
DESCRIPTION:
	 
	object for containg details about variables throughout the program

***************************************************************
"""
class Variable:
  
  """
  Function Name:
  
  	__init__

	Description:
  
  	Constructor for Variable
    
  Variables:
  
  	String  _dataType  type of the variable
    String  _name  name of the variable
    String  _description  description of the variable
    String  _inital_value  the inital value set to the variable
    Functions[]  _usage  functions the variable is used in
    int  _pointer_depth  the pointer depth of the variable
  """
  def __init__(self):
    self._dataType = ""
    self._name = ""
    self._description = ""
    self._usage = []
    self._inital_value = ""
    self._pointer_depth = 0

  def setDataType(self, dataType):
     self._dataType = dataType
    
  def setName(self, name):
    self._name = name
    
  def setDescription(self, description):
  	self._description = description
      
  def setInitalValue(self, inital_value):
      self._inital_value = inital_value
      
  def setPointerDepth(self, pointer_depth):
      self._pointer_depth = pointer_depth
      
  def getDataType(self):
    return self._dataType
    
  def getName(self):
    return self._name
    
  def getDescription(self):
     return self._description
 
  def getUsage(self):
      return self._usage
  
  def getInitalValue(self):
      return self._inital_value
  
  def getPointerDepth(self):
      return self._pointer_depth
    
  dataType = property(getDataType, setDataType)
  name = property(getName, setName)
  description = property(getDescription, setDescription)
  usage = property(getUsage)
  inital_value = property(getInitalValue, setInitalValue)
  pointer_depth = property(getPointerDepth, setPointerDepth)
      
   
"""
***************************************************************
CLASS NAME:
	
  Constant
  
DESCRIPTION:
	 
	object for containg details about constants throughout the program

***************************************************************
"""
class Constant:
  
  """
  Function Name:
  
  	__init__

	Description:
  
  	Constructor for Constant
    
  Variables:
  
  	String  _dataType  type of the constant
    String  _name  name of the constant
    String  _description  description of the constant
    Functions[]  _usage  functions the variable is used in
    String  _value  the value of the constant
  """
  def __init__(self):
    self._dataType = ""
    self._name = ""
    self._description = ""
    self._usage = []
    self._value = ""

  def setDataType(self, dataType):
     self._dataType = dataType
    
  def setName(self, name):
    self._name = name
    
  def setDescription(self, description):
  	self._description = description
      
  def setValue(self, value):
    self._value = value
      
  def getDataType(self):
    return self._dataType
    
  def getName(self):
    return self._name
    
  def getDescription(self):
     return self._description

  def getValue(self):
     return self._value
    
  dataType = property(getDataType, setDataType)
  name = property(getName, setName)
  description = property(getDescription, setDescription)
  value = property(getValue, setValue)
      
   
"""
***************************************************************
CLASS NAME:
	
  Function
  
DESCRIPTION:
	 
	object for containg details about functions throughout the program

***************************************************************
"""
class Function:
  
  """
  Function Name:
  
  	__init__

	Description:
  
  	Constructor for Function
    
  Variables:
  
  	String  name  name of the function
    String  description  description of the function usage
    Variable[]  parameters  parameters of the function
    Variable  returnValue  return value of the function
  """
  def __init__(self):
    self._name = ""
    self._description = ""
    self._parameters = []
    self._returnValue = Variable()
  
  def setName(self, name):
    self._name = name
    
  def setDescription(self, description):
     self._desription = description
      
  def appendParameter(self, parameter):
    self._parameters.append(parameter)
        
  def setReturnValue(self, returnValue):
    self._returnValue = returnValue
    
  def getName(self):
    return self._name
    
  def getDescription(self):
     return self._description
    
  def getParameters(self):
    return self._parameters
  
  def getReturnValue(self):
    return self._returnValue
  
  
  name = property(getName, setName)
  description = property(getDescription, setDescription)
  parameters = property(getParameters)
  returnValue = property(getReturnValue, setReturnValue)

"""
  Function Name:
  
  	exitMessage

	Description:
  
  	Prints specified message then exits program with specified exit code.
    
  Parameters:
  
  	String  message  the message to print out
    int  code  the exit code
"""
def exitMessage(message, code):
  print(message)
  sys.exit(code)
  
"""
  Function Name:
  
  	unformedSyntaxHandler

    Description:
  
  	Wrapper for exitMessage with repeatedly used unformed syntax message
"""
def unformedSyntaxHandler():
    exitMessage("Unformed syntax, please check line " + str(currentLineIndex), 1)
    
  
"""
  Function Name:
  
  	findN

	Description:
  
  	Returns the index of the nth substring of input.
    
  Parameters:
  
  	String  message  the message to print out
    int  code  the exit code
"""
def findN(s, substr, n):
    if n <= s.count(substr) and n > -1:
        if n == 1:
            return s.find(substr)
        else:
            return s.find(substr, findN(s, substr, n-1)+1)
    else:
        return -1
  
"""
  Function Name:
  
  	isVariableDeclaration

	Description:
  
  	Checks if the given line is a variable declaration
    
  Parameters:
  
  	String  line  the line to check
    
  Returns:
  
  	boolean  isVariable  returns True if line contains variable declaration, returns False otherwise
"""
def isVariableDeclaration(line):
    for datatype in variableDeclarationTypes:
        if line.startswith(datatype):
            commentIndex = line.find("//")
            semicolonIndex = line.find(';')
            if semicolonIndex != -1 and (semicolonIndex < commentIndex or commentIndex == -1):
                return True
            break
    return False

"""
  Function Name:
  
  	isConstantDeclaration

	Description:
  
  	Checks if the given line is a constant declaration
    
  Parameters:
      
      
  
  	String  line  the line to check
    
  Returns:
  
  	boolean  isConstant  returns True if line contains constant declaration, returns False otherwise
"""
def isConstantDeclaration(line):
    if currentLine.startswith("#define"):
        return True
    return False

"""
  Function Name:
      
    printConstant
    
  Description:
  
  	Prints out an instance of a Constant object to the command line for debugging.
    
  Parameters:
  
  	Constant  c  the constant to print out
"""
def printConstant(c):
    print("Name: " + c.name)
    print("Value: " + c.value)
    print("Type: " + c.dataType)
    print("Description: " + c.description) 
    
"""
  Function Name:
      
    printVariable
    
  Description:
  
  	Prints out an instance of a Constant object to the command line for debugging.
    
  Parameters:
  
  	Variable  v  the variable to print out
"""
def printVariable(v):
    print("Name: " + v.name)
    print("Inital Value: " + v.inital_value)
    print("Type: " + v.dataType)
    print("Description: " + v.description) 
    print("Pointer depth: " + str(v.pointer_depth))
    print()

  
"""
    Function Name:
        
        searchForChar
        
    Description:
        
        Searches left or right in a given String from a given index character by character 
        to find a character or the absence of a character, returning the index the feature is found at
        
    Parameters:
        
        String  s  the string to search for given character
        char  char  the char to search for the presence or absence of
        int  increment  the increment to change each time (1 to search left by 1, -1 to search right by 1)
        int  startIndex  the index to start from while searching
        bool  presence  if True the presence of the character will be searched for, if False the absence of the character will be searched for
    
    Returns:
        
        int  index  the index the request is found at in the given String, if there is an error or the character is not found -1
"""
def searchForChar(s, char, increment, startIndex, presence):
    if startIndex < 0 or startIndex >= len(s):
        return -1
    i = 0
    while startIndex+(i*increment) >= 0 and startIndex+(i*increment) < len(s):
        if presence:
            if s[startIndex+(i*increment)] == char:
                return startIndex+(i*increment)
        else:
            if s[startIndex+(i*increment)] != char:
                return startIndex+(i*increment)
        i += 1
    return -1
    
"""
  Function Name:
  
  	harvestConstant

  Description:
  
  	Harvests constant declaration into Variable object form then appends to global list of constants
    
  Parameters:
  
  	String  line  the line with the constant declaration to harvest
"""
def harvestConstant(line):
  #create new instance of Constant object
  new_constant = Constant()
  
  #collect indexes
  first_space_index = findN(line, " ", 1)
  second_space_index = findN(line, " ", 2)
  comment_index = findN(line, "//", 1)
  #check for an unformed file, this check should be expanded for more context then single space delimiters for arguments
  if first_space_index == -1 or second_space_index == -1 or (comment_index != -1 and comment_index < second_space_index):
      unformedSyntaxHandler()
  
  #harvest value by searching from left of comment to first character, then searching for whitespace
  value_right_index = -1
  if comment_index != -1:
      value_right_index = searchForChar(line, " ", -1, comment_index-1, False)
  else:
      value_right_index = searchForChar(line, " ", -1, len(line)-2, False)
      
  value_left_index = searchForChar(line, " ", -1, value_right_index, True)
  new_constant.value = line[value_left_index+1:value_right_index+1]
  
  name_right_index = searchForChar(line, " ", -1, value_left_index-1, False)
  name_left_index = searchForChar(line, " ", -1, name_right_index, True)
  new_constant.name = line[name_left_index+1:name_right_index+1]
  #harvest description
  if comment_index != -1:
      if line.endswith("\n"):
          new_constant.description = line[comment_index+2:len(line)-1]
      else:
          new_constant.description = line[comment_index+2:len(line)]
      
  #determine datatype

  #check for int   
  intFlag = False
    
  try:
      temp = int(new_constant.value)
      intFlag = True
  except ValueError:
      pass

  #check for float, 1 period and able to be removed and then check if digit
  floatFlag = False
  
  if new_constant.value.count(".") == 1:
      floatFlag = new_constant.value.replace('.','',1).isdigit()
   
  #quotes indicate it being a string
  stringFlag = False
  
  if (new_constant.value[-1] == "\"" and new_constant.value[0] == "\"") or (new_constant.value[-1] == "\'" and new_constant.value[0] == "\'"): 
      stringFlag = True
  
  booleanFlag = False
  if new_constant.value == "true" or new_constant.value == "false":
      booleanFlag = True

  #check statement where String>float>int
  if booleanFlag:
      new_constant.dataType = "bool"
  elif stringFlag:
      new_constant.dataType = "String"
  elif floatFlag:
      new_constant.dataType = "float"
  elif intFlag:
      new_constant.dataType = "int"
  else:
      new_constant.dataType = "keyword"
      

  documentedConstants.append(new_constant)

      
"""
  Function Name:
  
  	harvestVariable

	Description:
  
  	Harvests variable declaration into Variable object form then appends to global list of variables
    
  Parameters:
  
  	String  line  the line with the variable declaration to harvest
"""
def harvestVariable(line):
  #create new instance of Constant object
  new_variable = Variable()
  
  #collect indexes
  semicolon_index = findN(line, ";", 1)
  comment_index = findN(line, "//", 1)
  equals_index = findN(line, "=", 1)
  

  #check for an unformed file
  if semicolon_index == -1 or comment_index == -1 or comment_index < semicolon_index:
      unformedSyntaxHandler()
  
  #harvest description
  if comment_index != -1:
      if line.endswith("\n"):
          new_variable.description = line[comment_index+2:len(line)-1]
      else:
          new_variable.description = line[comment_index+2:len(line)]  
          
  asteriskCount = 0
  name_right_index = -1
  
  if equals_index != -1 and equals_index < semicolon_index:
      name_right_index = searchForChar(line, " ", -1, equals_index-1, False)
  else:
      name_right_index = searchForChar(line, " ", -1, semicolon_index-1, False)
      
  name_left_index = searchForChar(line, " ", -1, name_right_index, True)
  tempName = line[name_left_index+1:name_right_index+1]
  
  #function pointer check
  if ")" not in tempName:
      asteriskCount += tempName.count("*")
      new_variable.name = tempName.replace("*", "").replace(" ", "")
      dataType_right_index = searchForChar(line, " ", -1, name_left_index-1, False)
      dataType_left_index = searchForChar(line, " ", 1, 0, False)
      tempDataType = line[dataType_left_index:dataType_right_index+1]
      asteriskCount += tempDataType.count("*")
      new_variable.dataType = tempDataType.replace("*", "").replace(" ", "")
  else:
      parameter_right_index = searchForChar(line, ")", -1, semicolon_index-1, True)
      parameter_left_index = searchForChar(line, "(", -1, parameter_right_index-1, True)
      body_right_index = searchForChar(line, ")", -1, parameter_left_index-1, True)
      body_left_index = searchForChar(line, "(", -1, body_right_index-1, True)
      pointer_left_index = searchForChar(line, " ", 1, 0, False)
      pointerAsteriskLine = line[0:body_right_index+1]
      asteriskCount += pointerAsteriskLine.count("*")
      bodyLine = pointerAsteriskLine.replace("*", "")
      new_variable.name = bodyLine[findN(bodyLine, "(", 1)+1:findN(bodyLine, ")", 1)].replace(" ", "")
      new_variable.dataType = line[pointer_left_index:parameter_right_index+1].replace(" ", "").replace(new_variable.name, "")
  
  new_variable._pointer_depth = asteriskCount
    
  #collect inital value
  if equals_index != -1 and equals_index < semicolon_index:
      inital_value_left_index = searchForChar(line, " ", 1, equals_index+1, False)
      inital_value_right_index = searchForChar(line, " ", -1, semicolon_index-1, False)
      new_variable.inital_value = line[inital_value_left_index:inital_value_right_index+1]
  else:
      new_variable.inital_value = "null"
  
  documentedVariables.append(new_variable)

"""
***************************************************************

									 		START OF PROGRAM

***************************************************************  
"""       
#check if there are enough arguments
if len(sys.argv) < 2:
  #if not enough arguments print usage message and exit
  #exit with code 2, Missing keyword or command
  exitMessage("Usage: python snakedoc.py path", 2)

#checking and cleaning of filename
path = str(sys.argv[1])

extensionValid = False

for extension in validExtensions:
  if path.endswith(extension):
    extensionValid = True
    break

if not extensionValid:
  #exit with code 2, Missing keyword or command
	exitMessage("Invalid file extension", 2)

#open file for reading
try:
	file = open(path, "r")
except OSError:
  exitMessage("File not found\nDouble check your path was spelled correctly", 1)

#go through the file line by line
	#identify patterns that are indicative of documentation (function header being present) <- arrayofstrings = ["funcheader"]
  	#pass to a pattern handler and read line by line until end of the pattern (if a function header is present, we keep getting information from it until we hit the */ or end of the header)
    	#record any data in variables setup before loop
    	#return back to looking for patterns
while True:
    currentLineIndex += 1
    currentLine = file.readline()
    if currentLine == "":
        break
    elif "/*" in currentLine:
        harvestHeader()
    elif isVariableDeclaration(currentLine):
        harvestVariable(currentLine)
    elif isConstantDeclaration(currentLine):
        harvestConstant(currentLine)
        
for var in documentedVariables:
    printVariable(var)
    

#create a list of html indexs (www.google.com/home/funcname, www.google.com/home/2, www.google.com/home/3)

#create a html file using the data in objects
	#generate basic template for documentation file
  #crawl through function objects and create files based on them
  
