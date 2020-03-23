#work on security

#Import Statements
import sys

path = ""
validExtensions = ["ino", "cpp", "INO", "CPP"]
variableDeclarationTypes = ["double", "int", "String", "bool", "float", "char", "Integer", "long", "unsigned", "Integer", "void"]
documentedConstants = []
documentedVariables = []
documentedFunctions = []

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
    self.name = ""
    self.description = ""
    
  def setName(self, name):
    self.name = name
    
  def setDescription(self, description):
     self.desription = description
      
  def getName(self):
    return self.name
    
  def getDescription(self):
     return self.description
    
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
  
  	String  dataType  type of the variable
    String  name  name of the variable
    String  description  description of the variable
    Functions[]  usage  functions the variable is used in
  """
  def __init__(self):
    self.dataType = ""
    self.name = ""
    self.description = ""
    self.usage = []

  def setDataType(self, dataType):
     self.dataType = dataType
    
  def setName(self, name):
    self.name = name
    
  def setDescription(self, description):
  	self.desription = description
      
  def getDataType(self):
    return self.getDataType
    
  def getName(self):
    return self.name
    
  def getDescription(self):
     return self.description
    
  dataType = property(getDataType, setDataType)
  name = property(getName, setName)
  description = property(getDescription, setDescription)
      
      
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
    self.name = ""
    self.description = ""
    self.parameters = []
    self.returnValue = Variable()
  
  def setName(self, name):
    self.name = name
    
  def setDescription(self, description):
     self.desription = description
      
  def appendParameter(self, parameter):
    self.parameters.append(parameter)
        
  def setReturnValue(self, returnValue):
    self.returnValue = returnValue
    
  def getName(self):
    return self.name
    
  def getDescription(self):
     return self.description
    
  def getParameters(self):
    return self.parameters
  
  def getReturnValue(self):
    return self.returnValue
  
  
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
  
  	isVariableDeclaration

	Description:
  
  	Checks if the given line is a variable declaration
    
  Parameters:
  
  	String  line  the line to check
    
  Returns:
  
  	boolean  isVariable  returns True if line contains variable declaration, returns False otherwise
"""
def isVariableDeclaration(line):
    line.replace("*", "")
    for datatype in variableDeclarationTypes:
        if line.startswith(datatype):
            commentIndex = line.find("//")
            semicolonIndex = line.find(';')
            if semicolonIndex > -1 and (semicolonIndex < commentIndex or commentIndex == -1):
                return True
            break
    return False
  
"""
  Function Name:
  
  	harvestConstant

	Description:
  
  	Harvests constant declaration into Variable object form then appends to global list of constants
    
  Parameters:
  
  	String  line  the line with the constant declaration to harvest
"""
def harvestConstant(line):
  pass

      
"""
  Function Name:
  
  	harvestVariable

	Description:
  
  	Harvests variable declaration into Variable object form then appends to global list of variables
    
  Parameters:
  
  	String  line  the line with the variable declaration to harvest
"""
def harvestVariable(line):
  noAsteriskLine = line
  noAsteriskLine.replace("*", "")
	#look from right to left and equals sign
  

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
	currentLine = file.readline()
  if currentLine == "":
    break
  elif "/*" in currentLine:
  	harvestHeader()
	elif isVariableDeclaration(currentLine):
    harvestVariable(currentLine)
  elif currentLine.startswith("#define")
  	harvestConstant(currentLine)
  

#create a list of html indexs (www.google.com/home/funcname, www.google.com/home/2, www.google.com/home/3)

#create a html file using the data in objects
	#generate basic template for documentation file
  #crawl through function objects and create files based on them
  
