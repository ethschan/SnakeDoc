#work on security

#Import Statements
import sys

path = ""
validExtensions = ["ino", "cpp", "INO", "CPP"]

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
***************************************************************

									 		START OF PROGRAM

***************************************************************  
""" 
#check if there are enough arguments
if len(sys.argv) < 2:
  #if not enough arguments print usage message and exit
  print("Usage: python snakedoc.py path")
  #exit with code 2, Missing keyword or command
  sys.exit(2)

#checking and cleaning of filename
path = str(sys.argv[1])

extensionValid = False

for extension in validExtensions:
  if path.endswith(extension):
    extensionValid = True

if not extensionValid:
    print("Invalid file extension")
    #exit with code 2, Missing keyword or command
    sys.exit(2)

#display compatible files

#prompt for filename

#open file for reading

#open file for writing

#create a function object to store data
	#function objects should reference eachother (for example a variable is used inside a function)
  


#Create function object

#Include statement object (fields: String  name, String  usage)
  
#go through the file line by line
	#identify patterns that are indicative of documentation (function header being present) <- arrayofstrings = ["funcheader"]
  	#pass to a pattern handler and read line by line until end of the pattern (if a function header is present, we keep getting information from it until we hit the */ or end of the header)
    	#record any data in variables setup before loop
    	#return back to looking for patterns
      
#create a list of html indexs (www.google.com/home/funcname, www.google.com/home/2, www.google.com/home/3)

#create a html file using the data in objects
	#generate basic template for documentation file
  #crawl through function objects and create files based on them
  
