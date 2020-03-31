#Import Statements
import sys
import re
import os

#Global Variables
path = ""
validExtensions = ["ino", "cpp", "INO", "CPP", "h", "H", "hpp", "HPP", "hxx", "HXX", "cxx", "CXX", "cc", "CC"]
variableDeclarationTypes = ["double", "int", "bool", "float", "char", "long", "unsigned", "void", "string", "File", "short", "SdVolume", "Sd2Card", "SdFile"]
documentedConstants = []
documentedVariables = []
documentedFunctions = []
documentedLibraries = []
global currentLineIndex
currentLineIndex = 0
noExtensionFileName = ""

#CSS Stylesheet
stylesheetCSS = """body {
    background-color:#ffffff;
    color:#353833;
    font-family:'DejaVu Sans', Arial, Helvetica, sans-serif;
    font-size:14px;
    margin:0;
    padding:0;
    height:100%;
    width:100%;
}

a:link, a:visited {
    text-decoration:none;
    color:#4A6782;
}
a[href]:hover, a[href]:focus {
    text-decoration:none;
    color:#bb7a2a;
}
a[name] {
    color:#353833;
}
a[name]:before, a[name]:target, a[id]:before, a[id]:target {
    content:"";
    display:inline-block;
    position:relative;
    padding-top:129px;
    margin-top:-129px;
}
pre {
    font-family:'DejaVu Sans Mono', monospace;
    font-size:14px;
}
h1 {
    font-size:20px;
}
h2 {
    font-size:18px;
}
h3 {
    font-size:16px;
    font-style:italic;
}
h4 {
    font-size:13px;
}
h5 {
    font-size:12px;
}
h6 {
    font-size:11px;
}
ul {
    list-style-type:disc;
}
code, tt {
    font-family:'DejaVu Sans Mono', monospace;
    font-size:14px;
    padding-top:4px;
    margin-top:8px;
    line-height:1.4em;
}
dt code {
    font-family:'DejaVu Sans Mono', monospace;
    font-size:14px;
    padding-top:4px;
}
table tr td dt code {
    font-family:'DejaVu Sans Mono', monospace;
    font-size:14px;
    vertical-align:top;
    padding-top:4px;
}



.bar a, .bar a:link, .bar a:visited, .bar a:active {
    color:#FFFFFF;
    text-decoration:none;
}
.bar a:hover, .bar a:focus {
    color:#bb7a2a;
}

.navPadding {
    padding-top: 107px;
}
.fixedNav {
    position:fixed;
    width:100%;
    z-index:999;
    background-color:#ffffff;
}
.topNav {
    background-color:#4D7A97;
    color:#FFFFFF;
    float:left;
    padding:0;
    width:100%;
    clear:right;
    height:2.8em;
    padding-top:10px;
    overflow:hidden;
    font-size:12px;
}


ul.navList, ul.subNavList {
    float:left;
    margin:0 25px 0 0;
    padding:0;
}
ul.navList li{
    list-style:none;
    float:left;
    padding: 5px 6px;
    text-transform:uppercase;
}


.topNav a:link, .topNav a:active, .topNav a:visited, .bottomNav a:link, .bottomNav a:active, .bottomNav a:visited {
    color:#FFFFFF;
    text-decoration:none;
    text-transform:uppercase;
}
.topNav a:hover, .bottomNav a:hover {
    text-decoration:none;
    color:#bb7a2a;
    text-transform:uppercase;
}
.navBarCell1Rev {
    background-color:#F8981D;
    color:#253441;
    margin: auto 5px;
}

.header {
    clear:both;
    margin:0 20px;
    padding:5px 0 0 0;
}

.title {
    color:#2c4557;
    margin:10px 0;
}
.subTitle {
    margin:5px 0 0 0;
}
.header ul {
    margin:0 0 15px 0;
    padding:0;
}

.header ul li {
    list-style:none;
    font-size:13px;
}

div.details ul.blockList ul.blockList ul.blockList li.blockList h4, div.details ul.blockList ul.blockList ul.blockListLast li.blockList h4 {
    background-color:#dee3e9;
    border:1px solid #d0d9e0;
    margin:0 0 6px -8px;
    padding:7px 5px;
}
ul.blockList ul.blockList ul.blockList li.blockList h3 {
    background-color:#dee3e9;
    border:1px solid #d0d9e0;
    margin:0 0 6px -8px;
    padding:7px 5px;
}
ul.blockList ul.blockList li.blockList h3 {
    padding:0;
    margin:15px 0;
}
ul.blockList li.blockList h2 {
    padding:0px 0 20px 0;
}

.contentContainer {
    clear:both;
    padding:10px 20px;
    position:relative;
}

.contentContainer .description dl dt, .contentContainer .details dl dt, .serializedFormContainer dl dt {
    font-size:12px;
    font-weight:bold;
    margin:10px 0 0 0;
    color:#4E4E4E;
}
.contentContainer .description dl dd, .contentContainer .details dl dd, .serializedFormContainer dl dd {
    margin:5px 0 10px 0px;
    font-size:14px;
    font-family:'DejaVu Serif', Georgia, "Times New Roman", Times, serif;
}




ul.blockList, ul.blockListLast {
    margin:10px 0 10px 0;
    padding:0;
}
ul.blockList li.blockList, ul.blockListLast li.blockList {
    list-style:none;
    margin-bottom:15px;
    line-height:1.4;
}
ul.blockList ul.blockList li.blockList, ul.blockList ul.blockListLast li.blockList {
    padding:0px 20px 5px 10px;
    border:1px solid #ededed;
    background-color:#f8f8f8;
}
ul.blockList ul.blockList ul.blockList li.blockList, ul.blockList ul.blockList ul.blockListLast li.blockList {
    padding:0 0 5px 8px;
    background-color:#ffffff;
    border:none;
}
ul.blockList ul.blockList ul.blockList ul.blockList li.blockList {
    margin-left:0;
    padding-left:0;
    padding-bottom:15px;
    border:none;
}
ul.blockList ul.blockList ul.blockList ul.blockList li.blockListLast {
    list-style:none;
    border-bottom:none;
    padding-bottom:0;
}
table tr td dl, table tr td dl dt, table tr td dl dd {
    margin-top:0;
    margin-bottom:1px;
}

.memberSummary {
    width:100%;
    border-spacing:0;
    border-left:1px solid #EEE;
    border-right:1px solid #EEE;
    border-bottom:1px solid #EEE;
}
.memberSummary {
    padding:0px;
}
.memberSummary caption {
    position:relative;
    text-align:left;
    background-repeat:no-repeat;
    color:#253441;
    font-weight:bold;
    clear:none;
    overflow:hidden;
    padding:0px;
    padding-top:10px;
    padding-left:1px;
    margin:0px;
    white-space:pre;
}
.overviewSummary caption a:link, .memberSummary caption a:link, .typeSummary caption a:link,
.constantsSummary caption a:link, .deprecatedSummary caption a:link,
.requiresSummary caption a:link, .packagesSummary caption a:link, .providesSummary caption a:link,
.usesSummary caption a:link,
.overviewSummary caption a:hover, .memberSummary caption a:hover, .typeSummary caption a:hover,
.constantsSummary caption a:hover, .deprecatedSummary caption a:hover,
.requiresSummary caption a:hover, .packagesSummary caption a:hover, .providesSummary caption a:hover,
.usesSummary caption a:hover,
.overviewSummary caption a:active, .memberSummary caption a:active, .typeSummary caption a:active,
.constantsSummary caption a:active, .deprecatedSummary caption a:active,
.requiresSummary caption a:active, .packagesSummary caption a:active, .providesSummary caption a:active,
.usesSummary caption a:active,
.overviewSummary caption a:visited, .memberSummary caption a:visited, .typeSummary caption a:visited,
.constantsSummary caption a:visited, .deprecatedSummary caption a:visited,
.requiresSummary caption a:visited, .packagesSummary caption a:visited, .providesSummary caption a:visited,
.usesSummary caption a:visited {
    color:#FFFFFF;
}
.useSummary caption a:link, .useSummary caption a:hover, .useSummary caption a:active,
.useSummary caption a:visited {
    color:#1f389c;
}
.overviewSummary caption span, .memberSummary caption span, .typeSummary caption span,
.useSummary caption span, .constantsSummary caption span, .deprecatedSummary caption span,
.requiresSummary caption span, .packagesSummary caption span, .providesSummary caption span,
.usesSummary caption span {
    white-space:nowrap;
    padding-top:5px;
    padding-left:12px;
    padding-right:12px;
    padding-bottom:7px;
    display:inline-block;
    float:left;
    background-color:#F8981D;
    border: none;
    height:16px;
}
.memberSummary caption span.activeTableTab span, .packagesSummary caption span.activeTableTab span,
.overviewSummary caption span.activeTableTab span, .typeSummary caption span.activeTableTab span {
    white-space:nowrap;
    padding-top:5px;
    padding-left:12px;
    padding-right:12px;
    margin-right:3px;
    display:inline-block;
    float:left;
    background-color:#F8981D;
    height:16px;
}
.memberSummary caption span.tableTab span, .packagesSummary caption span.tableTab span,
.overviewSummary caption span.tableTab span, .typeSummary caption span.tableTab span {
    white-space:nowrap;
    padding-top:5px;
    padding-left:12px;
    padding-right:12px;
    margin-right:3px;
    display:inline-block;
    float:left;
    background-color:#4D7A97;
    height:16px;
}
.memberSummary caption span.tableTab, .memberSummary caption span.activeTableTab,
.packagesSummary caption span.tableTab, .packagesSummary caption span.activeTableTab,
.overviewSummary caption span.tableTab, .overviewSummary caption span.activeTableTab,
.typeSummary caption span.tableTab, .typeSummary caption span.activeTableTab {
    padding-top:0px;
    padding-left:0px;
    padding-right:0px;
    background-image:none;
    float:none;
    display:inline;
}
.overviewSummary .tabEnd, .memberSummary .tabEnd, .typeSummary .tabEnd,
.useSummary .tabEnd, .constantsSummary .tabEnd, .deprecatedSummary .tabEnd,
.requiresSummary .tabEnd, .packagesSummary .tabEnd, .providesSummary .tabEnd, .usesSummary .tabEnd {
    display:none;
    width:5px;
    position:relative;
    float:left;
    background-color:#F8981D;
}
.memberSummary .activeTableTab .tabEnd, .packagesSummary .activeTableTab .tabEnd,
.overviewSummary .activeTableTab .tabEnd, .typeSummary .activeTableTab .tabEnd {
    display:none;
    width:5px;
    margin-right:3px;
    position:relative;
    float:left;
    background-color:#F8981D;
}
.memberSummary .tableTab .tabEnd, .packagesSummary .tableTab .tabEnd,
.overviewSummary .tableTab .tabEnd, .typeSummary .tableTab .tabEnd {
    display:none;
    width:5px;
    margin-right:3px;
    position:relative;
    background-color:#4D7A97;
    float:left;
}
.rowColor th, .altColor th {
    font-weight:normal;
}
.overviewSummary td, .memberSummary td, .typeSummary td,
.useSummary td, .constantsSummary td, .deprecatedSummary td,
.requiresSummary td, .packagesSummary td, .providesSummary td, .usesSummary td {
    text-align:left;
    padding:0px 0px 12px 10px;
}
th.colFirst, th.colSecond, th.colLast, th.colConstructorName, th.colDeprecatedItemName, .useSummary th,
.constantsSummary th, .packagesSummary th, td.colFirst, td.colSecond, td.colLast, .useSummary td,
.constantsSummary td {
    vertical-align:top;
    padding-right:0px;
    padding-top:8px;
    padding-bottom:3px;
}
th.colFirst, th.colSecond, th.colLast, th.colConstructorName, th.colDeprecatedItemName, .constantsSummary th,
.packagesSummary th {
    background:#dee3e9;
    text-align:left;
    padding:8px 3px 3px 7px;
}
td.colFirst, th.colFirst {
    font-size:13px;
}
td.colSecond, th.colSecond, td.colLast, th.colConstructorName, th.colDeprecatedItemName, th.colLast {
    font-size:13px;
}

.providesSummary th.colFirst, .providesSummary th.colLast, .providesSummary td.colFirst,
.providesSummary td.colLast {
    white-space:normal;
    font-size:13px;
}
.overviewSummary td.colFirst, .overviewSummary th.colFirst,
.requiresSummary td.colFirst, .requiresSummary th.colFirst,
.packagesSummary td.colFirst, .packagesSummary td.colSecond, .packagesSummary th.colFirst, .packagesSummary th,
.usesSummary td.colFirst, .usesSummary th.colFirst,
.providesSummary td.colFirst, .providesSummary th.colFirst,
.memberSummary td.colFirst, .memberSummary th.colFirst,
.memberSummary td.colSecond, .memberSummary th.colSecond, .memberSummary th.colConstructorName,
.typeSummary td.colFirst, .typeSummary th.colFirst {
    vertical-align:top;
}
.packagesSummary th.colLast, .packagesSummary td.colLast {
    white-space:normal;
}
td.colFirst a:link, td.colFirst a:visited,
td.colSecond a:link, td.colSecond a:visited,
th.colFirst a:link, th.colFirst a:visited,
th.colSecond a:link, th.colSecond a:visited,
th.colConstructorName a:link, th.colConstructorName a:visited,
th.colDeprecatedItemName a:link, th.colDeprecatedItemName a:visited,
.constantValuesContainer td a:link, .constantValuesContainer td a:visited,
.allClassesContainer td a:link, .allClassesContainer td a:visited,
.allPackagesContainer td a:link, .allPackagesContainer td a:visited {
    font-weight:bold;
}
.tableSubHeadingColor {
    background-color:#EEEEFF;
}
.altColor, .altColor th {
    background-color:#FFFFFF;
}

ul.blockList ul.blockList ul.blockList li.blockList h3 {
    font-style:normal;
}
div.block {
    font-size:14px;
    font-family:'DejaVu Serif', Georgia, "Times New Roman", Times, serif;
}
td.colLast div {
    padding-top:0px;
}
td.colLast a {
    padding-bottom:3px;
}

h1.hidden {
    visibility:hidden;
    overflow:hidden;
    font-size:10px;
}
.block {
    display:block;
    margin:3px 10px 2px 0px;
    color:#474747;
}


div.block div.deprecationComment, div.block div.block span.emphasizedPhrase,
div.block div.block span.interfaceName {
    font-style:normal;
}
div.contentContainer ul.blockList li.blockList h2 {
    padding-bottom:0px;
}


main, nav, header, footer, section {
    display:block;
}




.methodSignature {
    white-space:normal;
}

table.borderless,
table.plain,
table.striped {
    margin-top: 10px;
    margin-bottom: 10px;
}
table.borderless > caption,
table.plain > caption,
table.striped > caption {
    font-weight: bold;
    font-size: smaller;
}
table.borderless th, table.borderless td,
table.plain th, table.plain td,
table.striped th, table.striped td {
    padding: 2px 5px;
}
table.borderless,
table.borderless > thead > tr > th, table.borderless > tbody > tr > th, table.borderless > tr > th,
table.borderless > thead > tr > td, table.borderless > tbody > tr > td, table.borderless > tr > td {
    border: none;
}
table.borderless > thead > tr, table.borderless > tbody > tr, table.borderless > tr {
    background-color: transparent;
}
table.plain {
    border-collapse: collapse;
    border: 1px solid black;
}
table.plain > thead > tr, table.plain > tbody tr, table.plain > tr {
    background-color: transparent;
}
table.plain > thead > tr > th, table.plain > tbody > tr > th, table.plain > tr > th,
table.plain > thead > tr > td, table.plain > tbody > tr > td, table.plain > tr > td {
    border: 1px solid black;
}
table.striped {
    border-collapse: collapse;
    border: 1px solid black;
}
table.striped > thead {
    background-color: #E3E3E3;
}
table.striped > thead > tr > th, table.striped > thead > tr > td {
    border: 1px solid black;
}
table.striped > tbody > tr:nth-child(even) {
    background-color: #EEE
}
table.striped > tbody > tr:nth-child(odd) {
    background-color: #FFF
}
table.striped > tbody > tr > th, table.striped > tbody > tr > td {
    border-left: 1px solid black;
    border-right: 1px solid black;
}
table.striped > tbody > tr > th {
    font-weight: normal;
}"""

"""
***************************************************************
CLASS NAME:

    Library

DESCRIPTION:

    Object that repersents a library import statement
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
    String  description  description of the usage of the library in the program
    String  code  the plain text code of the library import statement
  """
  def __init__(self):
    self._name = ""
    self._description = ""
    self._code = ""

  def setName(self, name):
    self._name = name

  def setDescription(self, description):
     self._description = description

  def setCode(self, code):
      self._code = code

  def getName(self):
    return self._name

  def getDescription(self):
     return self._description

  def getCode(self):
      return self._code

  """
  Function Name:

    toString

  Description:

    Prints out the Library object to the command line
  """
  def toString(self):
      print("Name: " + self._name)
      print("Description: " + self._description)
      print("Code: " + self._code)
      print()

  #Property Calls
  name = property(getName, setName)
  description = property(getDescription, setDescription)
  code = property(getCode, setCode)

"""
***************************************************************
CLASS NAME:

  Variable

DESCRIPTION:

  Object that repersents a global variable declaration in the program
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
    String  inital_value  the inital value set to the variable
    Functions[]  usage  functions the variable is used in
    int  pointer_depth  the pointer depth of the variable
    String  code  the plain text code of the variable declaration
  """
  def __init__(self):
    self._dataType = ""
    self._name = ""
    self._description = ""
    self._usage = []
    self._inital_value = "null"
    self._pointer_depth = 0
    self._code = ""

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

  def setCode(self, code):
      self._code = code

  def appendUsage(self, function):
      self._usage.append(function)

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

  def getCode(self):
      return self._code

  """
  Function Name:

    toString

  Description:

  	Prints out the current instance of a Variable object to the command line
  """
  def toString(self):
      print("Name: " + self._name)
      print("Inital Value: " + self._inital_value)
      print("Type: " + self._dataType)
      print("Description: " + self._description)
      print("Pointer depth: " + str(self._pointer_depth))
      print("Used in:")
      for function in self._usage:
          print(function.name)
      print()

  #Property Calls
  dataType = property(getDataType, setDataType)
  name = property(getName, setName)
  description = property(getDescription, setDescription)
  usage = property(getUsage)
  inital_value = property(getInitalValue, setInitalValue)
  pointer_depth = property(getPointerDepth, setPointerDepth)
  code = property(getCode, setCode)

"""
***************************************************************
CLASS NAME:

  Constant

DESCRIPTION:

	Object that repersents a constant declaration in the program
***************************************************************
"""
class Constant:
  """
  Function Name:

  	__init__

  Description:

  	Constructor for Constant

  Variables:

  	String  dataType  predicted data type of the constant
    String  name  name of the constant
    String  description  description of the constant
    Functions[]  usage  functions the constant is used in
    String  value  the value of the constant
    String  code  the plain text code of the constant declaration
  """
  def __init__(self):
    self._dataType = ""
    self._name = ""
    self._description = ""
    self._usage = []
    self._value = ""
    self._code = ""

  def setDataType(self, dataType):
     self._dataType = dataType

  def setName(self, name):
    self._name = name

  def setDescription(self, description):
  	self._description = description

  def setValue(self, value):
    self._value = value

  def setCode(self, code):
    self._code = code

  def appendUsage(self, function):
    self._usage.append(function)

  def getDataType(self):
    return self._dataType

  def getName(self):
    return self._name

  def getDescription(self):
     return self._description

  def getValue(self):
     return self._value

  def getCode(self):
      return self._code

  def getUsage(self):
      return self._usage

  """
  Function Name:

    toString

  Description:

  	Prints out the Constant object to the command line
  """
  def toString(self):
    print("Name: " + self._name)
    print("Value: " + self._value)
    print("Type: " + self._dataType)
    print("Description: " + self._description)
    print("Usage: ")
    for function in self._usage:
        print(function.name)
    print()

  #Property Calls
  dataType = property(getDataType, setDataType)
  name = property(getName, setName)
  description = property(getDescription, setDescription)
  value = property(getValue, setValue)
  code = property(getCode, setCode)
  usage = property(getUsage)

"""
***************************************************************
CLASS NAME:

  Function

DESCRIPTION:

	Object repersenting a Function in the program
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
    String  description  description of the function
    Variable[]  parameters  parameters of the function
    Variable  returnValue  return value of the function
	Variable[]  variables  the global variables manipulated by the function
    Constant[] constants  the global constants referenced by the fucntion
	Functions[]  functionCalls  functions called by the function
	String  code  the plain text code of the function
  """
  def __init__(self):
      self._description = ""
      self._parameters = []
      self._return_value = None
      self._variables = []
      self._function_calls = []
      self._constants = []
      self._code = ""
      self._name = ""

  def setName(self, name):
      self._name = name

  def setCode(self, code):
      self._code = code

  def setDescription(self, description):
      self._description = description

  def appendParameter(self, parameter):
      self._parameters.append(parameter)

  def setReturnValue(self, returnValue):
      self._return_value = returnValue

  def appendFunctionCall(self, function):
      self._function_calls.append(function)

  def appendVariable(self, variable):
      self._variables.append(variable)

  def appendConstant(self, constant):
      self._constants.append(constant)

  def getName(self):
      return self._name

  def getDescription(self):
      return self._description

  def getParameters(self):
      return self._parameters

  def getReturnValue(self):
      return self._return_value

  def getCode(self):
      return self._code

  def getFunctionCalls(self):
      return self._function_calls

  def getVariables(self):
      return self._variables

  def getConstants(self):
      return self._constants

  """
  Function Name:

    toString

  Description:

  	Prints out the current instance of the Function object to the command line for debugging.
  """
  def toString(self):
      print("========================================")
      print("Name: " + str(self._name) + "\n")
      print("Description:")
      print(self._description + "\n")
      print("Parameters:")
      for parameter in self._parameters:
          parameter.toString()
          print()
          print("\nReturn value:")
      if self._return_value != None:
	         self._return_value.toString()
      print("Code:")
      print(self._code)
      print("Variables used:")
      for variable in self._variables:
          print(variable.name)
      print("Functions called:")
      for function in self._function_calls:
          print(function.name)
      print("========================================")

  #Property Calls
  name = property(getName, setName)
  description = property(getDescription, setDescription)
  parameters = property(getParameters)
  returnValue = property(getReturnValue, setReturnValue)
  code = property(getCode, setCode)
  functionCalls = property(getFunctionCalls)
  variables = property(getVariables)
  constants = property(getConstants)

"""
  Function Name:

  	exitMessage

  Description:

  	Prints specified message then exits program with specified exit code

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

  	Wrapper for exitMessage with an unformed syntax message including the offending line, exiting with code 1
"""
def unformedSyntaxHandler():
    exitMessage("Unformed syntax, please check line " + str(currentLineIndex), 1)

"""
  Function Name:

  	findN

  Description:

  	Returns the index of the nth substring of input

  Parameters:

  	String  s  the string to search
    String  substr  the substring to search for
    int  n  the nth occurrence to search for
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
    for dataType in variableDeclarationTypes:
        if re.search(" *" + dataType, line):
            if re.search("//", line) and re.search(";", line):
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
    if re.search("^.*#define", line):
        return True
    return False

"""
    Function Name:

      searchForChar

    Description:

      Searches left or right in a given String from a given index character by character
      to find a character or the absence of a character, returning the index the feature is found at

    Parameters:

      String  string  the string to search for given character
      char  char  the char to search for the presence or absence of
      int  increment  the increment to change each time (1 to search left by 1, -1 to search right by 1)
      int  startIndex  the index to start from while searching
      bool  presence  if True the presence of the character will be searched for, if False the absence of the character will be searched for

    Returns:

      int  index  the index the request is found at in the given String, if there is an error or the character is not found -1
"""
def searchForChar(string, char, increment, startIndex, presence):
    if startIndex < 0 or startIndex >= len(string):
        return -1
    i = 0
    if presence:
        while startIndex+(i*increment) >= 0 and startIndex+(i*increment) < len(string):
            if string[startIndex+(i*increment)] == char:
                return startIndex+(i*increment)
            i += 1
    else:
    	while startIndex+(i*increment) >= 0 and startIndex+(i*increment) < len(string):
            if string[startIndex+(i*increment)] != char:
                return startIndex+(i*increment)
            i += 1
    return -1

"""
  Function Name:

  	isFunctionHeader

  Description:

  	Checks if the given line is the start of a function header

  Parameters:

  	String  line  the line to check

  Returns:

  	boolean  isFunctionHeader  returns True if line contains the start of a function header, returns False otherwise
"""
def isFunctionHeader(line):
    if re.search("^.*Function Name: *\n", line):
        return True
    return False

"""
  Function Name:

  	isLibraryImport

  Description:

  	Checks if the given line is a library import statement

  Parameters:

  	String  line  the line to check

  Returns:

  	boolean  isLibraryImport  returns True if line contains a library import statement, returns False otherwise
"""
def isLibraryImport(line):
    if re.search("^.*#include", line):
        return True
    return False

"""
    Function Name:

  	  skipBlankLine

    Description:

      Skips lines until it encounters a line that doens't contain solely asterisks, spaces, and new line characters or is the end of a group comment (*/)
"""
def skipBlankLine():
    global currentLineIndex
    while True:
        line = file.readline()
        currentLineIndex += 1
        if not re.search("(\w)", line) and not re.search("(\*\/)", line):
            continue
        else:
            return line

"""
    Function Name:

  	  descriptionScraper

    Description:

  	  Scrapes the description section of a function header and sets fields of a Function object to harvested values

    Parameters:

	  Function  new_function  takes in a  function to set the harvested description to

    Returns:

	  String  line  return the last line read as it triggered an exit
"""
def descriptionScraper(new_function):
    description = ""
    line = skipBlankLine()
    while True:
        if re.search(".*Parameters: *\n", line) or re.search(".*Returns: *\n", line) or re.search("(\*\/)", line):
            break
        elif re.search("^.*Description: *\n", line) or re.search("^.*Function Name: *\n", line):
            unformedSyntaxHandler()
        else:
            description += re.search("([ *]*)([\w\[.!?\\\\-\]`~\{\}\"\'\;\:,\/=+@#$%^&*() <>]*[\w\[.!?\\-\]`~\{\}\"\'\;\:,\/=+@#$%^&*()<>])( *\n)",  line, re.I | re.U).group(2) + "\n"
        line = skipBlankLine()

    #Remove last end of line character if present
    if description.endswith("\n"):
        description = description[:-1]
    new_function.description = description
    return line

"""
    Function Name:

  	  parameterScraper

    Description:

      Scrapes the parameters section of a function header and sets fields of a Function object to harvested values

    Parameters:

      Function  new_function  takes in a  function to store the harvested parameters in

    Returns:

      String  line  return the last return the last line read as it triggered an exit
"""
def parameterScraper(new_function):
	line = skipBlankLine()
	while True:
		if  re.search(".*Returns: *\n", line) or re.search("(\*\/)", line) or re.search("([ *]*)(N\/A) *\n", line):
			break
		else:
			new_variable = Variable()
			groups  = re.search("([ *]*)([\w*\[\]]*)([ ]*)([\w]*)([ ]*)([\w\[.!?\\-\]`~\{\}\"\'\;\:,\/=+@#$%^&*() <>]*[\w\[.!?\\-\]`~\{\}\"\'\;\:,\/=+@#$%^&*()<>])( *\n)",  line, re.I | re.U)

			new_variable.description = groups.group(6)
			new_variable.name = groups.group(4)
			new_variable.dataType = groups.group(2)
			new_variable.pointer_depth = new_variable.dataType.count("*")
			new_variable.dataType = new_variable.dataType.replace("*", "")
			new_function.appendParameter(new_variable)
		line = skipBlankLine()
	return line

"""
Function Name:

  	returnScraper

Description:

  	Scrapes the return section of a function header and sets fields of a Function object to harvested values

Parameters:

	Function  new_function  takes in a  function to store the harvested return information in

Returns:

      String  line  return the last return the last line read as it triggered an exit
"""
def returnScraper(new_function):
	line = skipBlankLine()
	while True:
		if  re.search(".*Parameters: *\n", line) or re.search("(\*\/)", line) or re.search("([ *]*)(N\/A) *\n", line):
			break
		else:
			new_variable = Variable()
			groups  = re.search("([ *]*)([\w*]*)([ ]*)([\w]*)([ ]*)([\w\[.!?\\-\]`~\{\}\"\'\;\:,\/=+@#$%^&*() ]*[\w\[.!?\\-\]`~\{\}\"\'\;\:,\/=+@#$%^&*()])( *\n)",  line, re.I | re.U)
			new_variable.description = groups.group(6)
			new_variable.name = groups.group(4)
			new_variable.dataType = groups.group(2)
			new_variable.pointer_depth = new_variable.dataType.count("*")
			new_variable.dataType = new_variable.dataType.replace("*", "")
			new_function.returnValue = new_variable
		line = skipBlankLine()
	return line

"""
  Function Name:

  	harvestFunction

  Description:

  	Harvests function declaration and its header into a function object then appended the created object to the global list of functions documentedFunctions
"""
def harvestFunction():
	global currentLineIndex
	new_function = Function()
	#Keep going until we find a non-blank line (has the function name)
	line = skipBlankLine()

	if re.search("^.*Description: *\n", line):
		unformedSyntaxHandler()

	#Harvest function name from line
	new_function.name = re.sub("(\W)", "",  line)
	#Keep going until we encounter another field, (description field)
	line = skipBlankLine()


	#Check if field is description field
	if re.search("^.*Description: *\n", line):
		line = descriptionScraper(new_function)
	else:
		#Couldn't find description header
		unformedSyntaxHandler()

	headingsHarvestedCount = 0

	while headingsHarvestedCount < 2:
		if re.search(".*Parameters: *\n", line):
			line = parameterScraper(new_function)
		elif re.search(".*Returns: *\n", line):
			line = returnScraper(new_function)
		elif re.search("([ *]*)(N\/A) *\n", line):
			line = skipBlankLine()
			headingsHarvestedCount -= 1
		elif re.search("(\*\/)", line):
			#Done harvesting the function header
			break
		headingsHarvestedCount += 1

    #Confirm end of header was found
	if not re.search("(\*\/)", line):
		line = skipBlankLine()
		if not re.search("(\*\/)", line):
			unformedSyntaxHandler()

	line = skipBlankLine()

	code = ""

    #Harvest plain-text code
	opening_curly_count = line.count("{")
	closing_curly_count = line.count("}")
	code = line

	while opening_curly_count >= 1 and opening_curly_count != closing_curly_count:
		line = file.readline()
		currentLineIndex += 1
		opening_curly_count += line.count("{")
		closing_curly_count += line.count("}")
		code += line

	new_function.code = code

    #Append the created Function object
	documentedFunctions.append(new_function)

"""
  Function Name:

  	harvestLibraryImport

  Description:

  	Harvests a library import statement then appends the newly created object to documentedLibraries

  Parameters:

  	String  line  the line with the library import to harvest
"""
def harvestLibraryImport(line):
    new_library = Library()
    groups = re.search("( *)(#include)( *)([<\"\'][\w.\"\']*[\"\'>])( *)(\/\/)([\w ]*[\w ])( *\n)",  line, re.I | re.U)
    new_library.name = groups.group(4)
    new_library.description = groups.group(7)
    new_library.code = groups.group(1) + groups.group(2) + groups.group(3) + groups.group(4)
    documentedLibraries.append(new_library)

"""
  Function Name:

  	analyzeFunctionBody

  Description:

  	Analyzes the plain text code of the body of a function and creates links within objects

  Parameters:

  	Function  function_to_analyze  the function to analyze the code of
"""
def analyzeFunctionBody(function_to_analyze):
    code_to_analyze = function_to_analyze.code
    for function in documentedFunctions:
        if function.name != function_to_analyze.name:
            if re.search(function.name + "(\(.*\))",  code_to_analyze, re.I | re.U):
                function_to_analyze.appendFunctionCall(function)


    for variable in documentedVariables:
        if variable.name in code_to_analyze:
            function_to_analyze.appendVariable(variable)
            variable.appendUsage(function_to_analyze)

    for constant in documentedConstants:
        if constant.name in code_to_analyze:
            function_to_analyze.appendConstant(constant)
            constant.appendUsage(function_to_analyze)

"""
  Function Name:

  	harvestConstant

  Description:

  	Harvests constant declaration into Constant object form then appends the newly created object to the documentedConstants list

  Parameters:

  	String  line  the line with the constant declaration to harvest
"""
def harvestConstant(line):
  #Create a new instance of a Constant object
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

  #now that we know the indexs we can harvest the value
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
      floatFlag = new_constant.value.replace(".", "", 1).replace("-", "", 1).isdigit()

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

  new_constant.code = line[0:value_right_index+1]

  documentedConstants.append(new_constant)


"""
  Function Name:

  	harvestVariable

	Description:

  	Harvests variable declaration into Variable object form then appends to the object to documentedVariables

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

  #void (*foo)(int);     //wow

  #function pointer check
  if ")" not in tempName:
      asteriskCount += tempName.count("*")
      tempName = tempName.replace("*", "").replace(" ", "")
      arrayTag = False
      if "[" in tempName and "]" in tempName:
          sqaure_left_index = findN(tempName, "[", 1)
          sqaure_right_index = findN(tempName, "]", 1)
          tempName = tempName[0: sqaure_left_index:] + tempName[sqaure_right_index + 1::]
          arrayTag = True
      new_variable.name = tempName
      dataType_right_index = searchForChar(line, " ", -1, name_left_index-1, False)
      dataType_left_index = searchForChar(line, " ", 1, 0, False)
      tempDataType = line[dataType_left_index:dataType_right_index+1]
      asteriskCount += tempDataType.count("*")
      if arrayTag:
          new_variable.dataType = tempDataType.replace("*", "").replace(" ", "") + "[]"
      else:
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

  new_variable.code = line[0:semicolon_index+1]

  documentedVariables.append(new_variable)

"""
    Function Name:

        htmlHead

    Description:

  	    Returns a String contaning the start of a HTML file

    Parameter:

        String  title  title to put in the header
        String  path  the path to relate the stylesheet to

    Returns:

        String  htmlString  the html file string
"""
def htmlHead(title, path):
    htmlString = ""
    htmlString += "<!DOCTYPE HTML>"
    htmlString += "\n<html lang=\"en\">"
    htmlString += "\n<head>"
    htmlString += "\n<title>" + title + "</title>"
    htmlString += "\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">"
    htmlString += "\n<link rel=\"stylesheet\" type=\"text/css\" href=\"" + path + "\\stylesheets\stylesheet.css\" title=\"Style\">"
    htmlString += "\n<head>"
    return htmlString


"""
    Function Name:

        htmlNavBar

    Description:

  	    Returns a String contaning the navigation bar portion of the HTML file

    Parameter:

        String  highlighted_link  the link to highlight

    Returns:

        String  htmlString  the html file string
"""
def htmlNavBar(highlighted_link):
    htmlString = ""
    htmlString += "\n<header>"
    htmlString += "\n<nav>"
    htmlString += "<div class=\"topNav\">"
    htmlString += "<a id=\"navbar.top\"></a>"
    htmlString += "\n<ul class=\"navList\" title=\"Navigation\">"

    if highlighted_link != "Home":
        htmlString += "\n<li><a href=\"../home.html\">Home</a></li>"
    else:
        htmlString += "\n<li><a href=\"../home.html\" class=\"navBarCell1Rev\">Home</a></li>"

    if highlighted_link != "Functions":
        htmlString += "\n<li><a href=\"../indexes/functionsIndex.html\">Functions</a></li>"
    else:
        htmlString += "\n<li class=\"navBarCell1Rev\">Functions</li>"

    if highlighted_link != "Variables":
        htmlString += "\n<li><a href=\"../indexes/variablesIndex.html\">Variables</a></li>"
    else:
        htmlString += "\n<li class=\"navBarCell1Rev\">Variables</li>"

    if highlighted_link != "Constants":
        htmlString += "\n<li><a href=\"../indexes/constantsIndex.html\">Constants</a></li>"
    else:
        htmlString += "\n<li class=\"navBarCell1Rev\">Constants</li>"

    if highlighted_link != "Libraries":
        htmlString += "\n<li><a href=\"../indexes/librariesIndex.html\">Libraries</a></li>"
    else:
        htmlString += "\n<li class=\"navBarCell1Rev\">Libraries</li>"

    htmlString += "\n</header>"

    return htmlString

"""
    Function Name:

        htmlFunctionSummary

    Description:

  	    Returns a String contaning a function summary in HTML

    Parameter:

        Function  in_function  the function to turn into a HTML function summary

    Returns:

        String  htmlString  the html file string
"""
def htmlFunctionSummary(in_function):

    htmlString = ""

    if in_function.description != "" or len(in_function.parameters) >= 1 or in_function.returnValue != None:
        htmlString += "\n<div class=\"details\">"
        htmlString += "\n<ul class=\"blockList\">"
        htmlString += "\n<section>"
        htmlString += "\n<ul class=\"blockList\">"
        htmlString += "\n<li class=\"blockList\">"
        htmlString += "\n<a id=\"whitespace\"></a>"
        htmlString += "\n<h3>Function Summary</h3>"
        htmlString += "\n<a id=\"whitespace\"></a>"

        if in_function.description != "":
            htmlString += "\n<ul class=\"blockList\">"
            htmlString += "\n<li class=\"blockList\">"
            htmlString += "\n<h4>Description</h4>"
            htmlString += "\n<div class=\"block\">" + in_function.description.replace("\n", "<br \/>") + "</div>"

        htmlString += "\n</li>"

        if len(in_function.parameters) >= 1:
            htmlString += "\n<table class=\"memberSummary\">"
            htmlString += "\n<caption><span>Parameters</span><span class=\"tabEnd\">&nbsp;</span></caption>"
            htmlString += "\n<tr>"
            htmlString += "\n<th class=\"colFirst\" scope=\"col\">Data Type</th>"
            htmlString += "\n<th class=\"colSecond\" scope=\"col\">Name</th>"
            htmlString += "\n<th class=\"colLast\" scope=\"col\">Description</th>"
            htmlString += "</tr>"
            htmlString += "<tr id=\"i0\" class=\"altColor\">"


            for parameter in in_function.parameters:
                htmlString += "\n<tr id=\"i0\" class=\"altColor\">"
                htmlString += "\n<td class=\"colFirst\"><code>" + "*" * parameter.pointer_depth + parameter.dataType + "</code></td>"
                htmlString += "\n<th class=\"colSecond\" scope=\"row\"><code>" + parameter.name + "</code></th>"
                htmlString += "\n<td class=\"colLast\">"
                htmlString += "\n<div class=\"block\">" + parameter.description.replace("\n", " ") + "</div>"
                htmlString += "\n</td>"
                htmlString += "\n</tr>"

            htmlString += "\n</table>"

        if in_function.returnValue != None:
            htmlString += "\n<a id=\"whitespace\"></a>"
            htmlString += "\n<table class=\"memberSummary\">"
            htmlString += "<caption><span>Returns</span><span class=\"tabEnd\"> &nbsp;</span></caption>"
            htmlString += "\n<tr>"
            htmlString += "\n<th class=\"colFirst\" scope=\"col\">Data Type</th>"
            htmlString += "\n<th class=\"colSecond\" scope=\"col\">Name</th>"
            htmlString += "\n<th class=\"colLast\" scope=\"col\">Description</th>"
            htmlString += "\n</tr>"
            htmlString += "\n<tr id=\"i0\" class=\"altColor\">"
            htmlString += "\n<td class=\"colFirst\"><code>" + "*" * in_function.returnValue.pointer_depth + in_function.returnValue.dataType + "</code></td>"
            htmlString += "\n<th class=\"colSecond\" scope=\"row\"><code>" + in_function.returnValue.name + "</code></th>"
            htmlString += "\n<td class=\"colLast\">"
            htmlString += "\n<div class=\"block\">" + in_function.returnValue.description + "</div>"
            htmlString += "\n</td>"
            htmlString += "\n</tr>"
            htmlString += "\n</table>"

        htmlString += "\n</section>"
        htmlString += "\n</li>"
        htmlString += "\n</ul>"
        htmlString += "\n</li>"
        htmlString += "\n</ul>"
        htmlString += "\n</ul>"
        htmlString += "\n</div>"

    return htmlString


"""
    Function Name:

        htmlVariableSummary

    Description:

  	    Returns a String contaning the variable summary of a variable page in HTML

    Parameter:

        Variable  in_variable  the variable to turn into a HTML variable summary

    Returns:

        String  htmlString  the html file string
"""
def htmlVariableSummary(in_variable):

    htmlString = ""

    htmlString += "\n<div class=\"details\">"
    htmlString += "\n<ul class=\"blockList\">"
    htmlString += "\n<section>"
    htmlString += "\n<ul class=\"blockList\">"
    htmlString += "\n<li class=\"blockList\">"
    htmlString += "\n<a id=\"whitespace\"></a>"
    htmlString += "\n<h3>Variable Summary</h3>"
    htmlString += "\n<a id=\"whitespace\"></a>"

    htmlString += "\n<ul v class=\"blockList\">"
    htmlString += "\n<li class=\"blockList\">"
    htmlString += "\n<h4>Description</h4>"
    htmlString += "\n<div class=\"block\">" + in_variable.description.replace("\n", "<br \/>") + "</div>"
    htmlString += "\n</li>"

    htmlString += "\n<a id=\"whitespace\"></a>"
    htmlString += "\n<table class=\"memberSummary\">"
    htmlString += "<caption><span>Fields</span><span class=\"tabEnd\"> &nbsp;</span></caption>"
    htmlString += "\n<tr>"
    htmlString += "\n<th class=\"colFirst\" scope=\"col\">Data Type</th>"
    htmlString += "\n<th class=\"colSecond\" scope=\"col\">Name</th>"
    htmlString += "\n<th class=\"colLast\" scope=\"col\">Inital Value</th>"
    htmlString += "\n</tr>"
    htmlString += "\n<tr id=\"i0\" class=\"altColor\">"
    htmlString += "\n<td class=\"colFirst\"><code>" + "*" * in_variable.pointer_depth + in_variable.dataType + "</code></td>"
    htmlString += "\n<th class=\"colSecond\" scope=\"row\"><code>" + in_variable.name + "</code></th>"
    htmlString += "\n<td class=\"colLast\">"
    htmlString += "\n<div class=\"block\">" + in_variable.inital_value + "</div>"
    htmlString += "\n</td>"
    htmlString += "\n</tr>"
    htmlString += "\n</table>"

    htmlString += "\n</section>"
    htmlString += "\n</li>"
    htmlString += "\n</ul>"
    htmlString += "\n</li>"
    htmlString += "\n</ul>"
    htmlString += "\n</ul>"
    htmlString += "\n</div>"

    return htmlString

"""
    Function Name:

        htmlConstantSummary

    Description:

  	    Returns a String contaning the constant summary of a constant page in HTML

    Parameter:

        Constant  in_constant  the constant to turn into a HTML constat summary

    Returns:

        String  htmlString  the html file string
"""
def htmlConstantSummary(in_constant):

    htmlString = ""

    htmlString += "\n<div class=\"details\">"
    htmlString += "\n<ul class=\"blockList\">"
    htmlString += "\n<section>"
    htmlString += "\n<ul class=\"blockList\">"
    htmlString += "\n<li class=\"blockList\">"
    htmlString += "\n<a id=\"whitespace\"></a>"
    htmlString += "\n<h3>Constant Summary</h3>"
    htmlString += "\n<a id=\"whitespace\"></a>"

    htmlString += "\n<ul v class=\"blockList\">"
    htmlString += "\n<li class=\"blockList\">"
    htmlString += "\n<h4>Description</h4>"
    htmlString += "\n<div class=\"block\">" + in_constant.description.replace("\n", "<br \/>") + "</div>"
    htmlString += "\n</li>"

    htmlString += "\n<a id=\"whitespace\"></a>"
    htmlString += "\n<table class=\"memberSummary\">"
    htmlString += "<caption><span>Fields</span><span class=\"tabEnd\"> &nbsp;</span></caption>"
    htmlString += "\n<tr>"
    htmlString += "\n<th class=\"colFirst\" scope=\"col\">Data Type</th>"
    htmlString += "\n<th class=\"colSecond\" scope=\"col\">Name</th>"
    htmlString += "\n<th class=\"colLast\" scope=\"col\">Value</th>"
    htmlString += "\n</tr>"
    htmlString += "\n<tr id=\"i0\" class=\"altColor\">"
    htmlString += "\n<td class=\"colFirst\"><code>" + in_constant.dataType + "</code></td>"
    htmlString += "\n<th class=\"colSecond\" scope=\"row\"><code>" + in_constant.name + "</code></th>"
    htmlString += "\n<td class=\"colLast\">"
    htmlString += "\n<div class=\"block\">" + in_constant.value + "</div>"
    htmlString += "\n</td>"
    htmlString += "\n</tr>"
    htmlString += "\n</table>"

    htmlString += "\n</section>"
    htmlString += "\n</li>"
    htmlString += "\n</ul>"
    htmlString += "\n</li>"
    htmlString += "\n</ul>"
    htmlString += "\n</ul>"
    htmlString += "\n</div>"

    return htmlString

"""
    Function Name:

        htmlLibrarySummary

    Description:

  	    Returns a String contaning a HTML library summary

    Parameter:

        Library  in_library  the library to turn into a HTML library summary

    Returns:

        String  htmlString  the html file string
"""
def htmlLibrarySummary(in_library):

    htmlString = ""

    htmlString += "\n<div class=\"details\">"
    htmlString += "\n<ul class=\"blockList\">"
    htmlString += "\n<section>"
    htmlString += "\n<ul class=\"blockList\">"
    htmlString += "\n<li class=\"blockList\">"
    htmlString += "\n<a id=\"whitespace\"></a>"
    htmlString += "\n<h3>Library Summary</h3>"
    htmlString += "\n<a id=\"whitespace\"></a>"

    htmlString += "\n<ul v class=\"blockList\">"
    htmlString += "\n<li class=\"blockList\">"
    htmlString += "\n<h4>Description</h4>"
    htmlString += "\n<div class=\"block\">" + in_library.description.replace("\n", "<br \/>") + "</div>"
    htmlString += "\n</li>"

    htmlString += "\n</section>"
    htmlString += "\n</li>"
    htmlString += "\n</ul>"
    htmlString += "\n</li>"
    htmlString += "\n</ul>"
    htmlString += "\n</ul>"
    htmlString += "\n</div>"

    return htmlString

"""
    Function Name:

        htmlFunctionReferences

    Description:

  	    Returns a String contaning the references of a function file in HTML

    Parameter:

        Function  in_function  the function to create the HTML references section for

    Returns:

        String  htmlString  the html file string
"""
def htmlFunctionReferences(in_function):
    htmlString = ""

    if len(in_function.functionCalls) >= 1 or len(in_function.variables) >= 1 or len(in_function.constants) >= 1:
        htmlString += "\n<div class=\"details\">"
        htmlString += "\n<ul class=\"blockList\">"
        htmlString += "\n<section>"
        htmlString += "\n<ul class=\"blockList\">"
        htmlString += "\n<li class=\"blockList\">"
        htmlString += "\n<a id=\"whitespace\"></a>"
        htmlString += "\n<h3>References</h3>"
        htmlString += "\n<a id=\"whitespace\"></a>"
        htmlString += "\n<ul class=\"blockList\">"
        if len(in_function.functionCalls) >= 1:
            htmlString += "\n<li class=\"blockList\">"
            htmlString += "\n<h4>Referenced Functions</h4>"

            buildString = ""

            firstFlag = True

            for function in in_function.functionCalls:
                if firstFlag:
                    buildString += "<a href=\"../functions/" + function.name + ".html\">" + function.name + "</a>"
                    firstFlag = False
                else:
                    buildString += ", <a href=\"../functions/" + function.name + ".html\">" + function.name + "</a>"

            htmlString += "\n<code>" + buildString + "</code>"

            htmlString += "\n</li>"

        if len(in_function.variables) >= 1:
            htmlString += "\n<li class=\"blockList\">"
            htmlString += "\n<h4>Referenced Variables</h4>"

            buildString = ""

            firstFlag = True

            for variable in in_function.variables:
                if firstFlag:
                    buildString += "<a href=\"../variables/" + variable.name + ".html\">" + variable.name + "</a>"
                    firstFlag = False
                else:
                    buildString += ", <a href=\"../variables/" + variable.name + ".html\">" + variable.name + "</a>"


            htmlString += "\n<code>" + buildString +  "</code>"

            htmlString += "\n</li>"

        if len(in_function.constants) >= 1:
            htmlString += "\n<li class=\"blockList\">"
            htmlString += "\n<h4>Referenced Constants</h4>"

            buildString = ""

            firstFlag = True

            for constant in in_function.constants:
                if firstFlag:
                    buildString += "<a href=\"../constants/" + constant.name + ".html\">" + constant.name + "</a>"
                    firstFlag = False
                else:
                    buildString += ", <a href=\"../constants/" + constant.name + ".html\">" + constant.name + "</a>"


            htmlString += "\n<code>" + buildString +  "</code>"
            htmlString += "\n</li>"

        htmlString += "\n</section>"

        htmlString += "\n</li>"
        htmlString += "\n</ul>"
        htmlString += "\n</ul>"
        htmlString += "\n</ul>"

        htmlString += "\n</div>"

    return htmlString


"""
    Function Name:

        htmlVariableReferences

    Description:

  	    Returns a String contaning the references of a variable file in HTML

    Parameter:

        Variable  in_variable  the variable to create the HTML references section for

    Returns:

        String  htmlString  the html file string
"""
def htmlVariableReferences(in_variable):
    htmlString = ""

    if len(in_variable.usage) >= 1:
        htmlString += "\n<div class=\"details\">"
        htmlString += "\n<ul class=\"blockList\">"
        htmlString += "\n<section>"
        htmlString += "\n<ul class=\"blockList\">"
        htmlString += "\n<li class=\"blockList\">"
        htmlString += "\n<a id=\"whitespace\"></a>"
        htmlString += "\n<h3>Usage</h3>"
        htmlString += "\n<a id=\"whitespace\"></a>"
        htmlString += "\n<ul class=\"blockList\">"

        htmlString += "\n<li class=\"blockList\">"
        htmlString += "\n<h4>Usage in Functions</h4>"

        buildString = ""

        firstFlag = True

        for function in in_variable.usage:
            if firstFlag:
                buildString += "<a href=\"../functions/" + function.name + ".html\">" + function.name + "</a>"
                firstFlag = False
            else:
                buildString += ", <a href=\"../functions/" + function.name + ".html\">" + function.name + "</a>"

        htmlString += "\n<code>" + buildString + "</code>"

        htmlString += "\n</li>"

        htmlString += "\n</section>"

        htmlString += "\n</li>"
        htmlString += "\n</ul>"
        htmlString += "\n</ul>"
        htmlString += "\n</ul>"

        htmlString += "\n</div>"

    return htmlString

"""
    Function Name:

        htmlConstantReferences

    Description:

  	    Returns a String contaning the references of a constant file in HTML

    Parameter:

        Constant  in_constant  the constant to create the HTML references section for

    Returns:

        String  htmlString  the html file string
"""
def htmlConstantReferences(in_constant):
    htmlString = ""

    if len(in_constant.usage) >= 1:
        htmlString += "\n<div class=\"details\">"
        htmlString += "\n<ul class=\"blockList\">"
        htmlString += "\n<section>"
        htmlString += "\n<ul class=\"blockList\">"
        htmlString += "\n<li class=\"blockList\">"
        htmlString += "\n<a id=\"whitespace\"></a>"
        htmlString += "\n<h3>Usage</h3>"
        htmlString += "\n<a id=\"whitespace\"></a>"
        htmlString += "\n<ul class=\"blockList\">"

        htmlString += "\n<li class=\"blockList\">"
        htmlString += "\n<h4>Usage in Functions</h4>"

        buildString = ""

        firstFlag = True

        for function in in_constant.usage:
            if firstFlag:
                buildString += "<a href=\"../functions/" + function.name + ".html\">" + function.name + "</a>"
                firstFlag = False
            else:
                buildString += ", <a href=\"../functions/" + function.name + ".html\">" + function.name + "</a>"

        htmlString += "\n<code>" + buildString + "</code>"

        htmlString += "\n</li>"

        htmlString += "\n</section>"

        htmlString += "\n</li>"
        htmlString += "\n</ul>"
        htmlString += "\n</ul>"
        htmlString += "\n</ul>"

        htmlString += "\n</div>"

    return htmlString

"""
    Function Name:

        htmlFunctionBody

    Description:

  	    Returns a String contaning the the function body portion of the function page in HTML

    Parameter:

        Function  in_function  the function to create the function body in HTML for

    Returns:

        String  htmlString  the html file string
"""
def htmlFunctionBody(in_function):
    htmlString = ""
    htmlString += "\n<div class=\"details\">"
    htmlString += "\n<ul class=\"blockList\">"
    htmlString += "\n<li class=\"blockList\">"
    htmlString += "\n<section>"
    htmlString += "\n<ul class=\"blockList\">"
    htmlString += "\n<li class=\"blockList\">"
    htmlString += "\n<a id=\"whitespace\"></a>"
    htmlString += "\n<h3>Function Body</h3>"
    htmlString += "\n<a id=\"whitespace\"></a>"
    htmlString += "\n<ul class=\"blockListLast\">"
    htmlString += "\n<li class=\"blockList\">"
    htmlString += "\n<h4>" + in_function.name + "</h4>"
    codeString = in_function.code
    newLineFlag = False
    buildCodeString = ""
    for letter in codeString:
        if letter == "\n":
            newLineFlag = True
            buildCodeString += "<br \/>"
        elif letter == " " and newLineFlag:
            buildCodeString += "&nbsp;&nbsp;"
        else:
            newLineFlag = False
            buildCodeString += letter

    htmlString += "\n<pre class=\"methodSignature\">" + buildCodeString + "</pre>"
    htmlString += "\n</li>"
    htmlString += "\n</ul>"
    htmlString += "\n</li>"
    htmlString += "\n</ul>"
    htmlString += "\n</section>"
    htmlString += "\n</li>"
    htmlString += "\n</ul>"
    htmlString += "\n</div>"

    return htmlString

"""
    Function Name:

        htmlVariableBody

    Description:

  	    Returns a String contaning the the variable body portion of the variable page in HTML

    Parameter:

        Variable  in_variable  the variable to create the variable body in HTML for

    Returns:

        String  htmlString  the html file string
"""
def htmlVariableBody(in_variable):
    htmlString = ""
    htmlString += "\n<div class=\"details\">"
    htmlString += "\n<ul class=\"blockList\">"
    htmlString += "\n<li class=\"blockList\">"
    htmlString += "\n<section>"
    htmlString += "\n<ul class=\"blockList\">"
    htmlString += "\n<li class=\"blockList\">"
    htmlString += "\n<a id=\"whitespace\"></a>"
    htmlString += "\n<h3>Variable Declaration</h3>"
    htmlString += "\n<a id=\"whitespace\"></a>"
    htmlString += "\n<ul class=\"blockListLast\">"
    htmlString += "\n<li class=\"blockList\">"
    htmlString += "\n<h4>" + in_variable.name + "</h4>"
    codeString = in_variable.code
    newLineFlag = False
    buildCodeString = ""
    for letter in codeString:
        if letter == "\n":
            newLineFlag = True
            buildCodeString += "<br \/>"
        elif letter == " " and newLineFlag:
            buildCodeString += "&nbsp;&nbsp;"
        else:
            newLineFlag = False
            buildCodeString += letter

    htmlString += "\n<pre class=\"methodSignature\">" + buildCodeString + "</pre>"
    htmlString += "\n</li>"
    htmlString += "\n</ul>"
    htmlString += "\n</li>"
    htmlString += "\n</ul>"
    htmlString += "\n</section>"
    htmlString += "\n</li>"
    htmlString += "\n</ul>"
    htmlString += "\n</div>"

    return htmlString

"""
    Function Name:

        htmlConstantBody

    Description:

  	    Returns a String contaning the the constant body portion of the constant page in HTML

    Parameter:

        Constant  in_constant  the constant to create the constant body in HTML for

    Returns:

        String  htmlString  the html file string
"""
def htmlConstantBody(in_constant):
    htmlString = ""
    htmlString += "\n<div class=\"details\">"
    htmlString += "\n<ul class=\"blockList\">"
    htmlString += "\n<li class=\"blockList\">"
    htmlString += "\n<section>"
    htmlString += "\n<ul class=\"blockList\">"
    htmlString += "\n<li class=\"blockList\">"
    htmlString += "\n<a id=\"whitespace\"></a>"
    htmlString += "\n<h3>Constant Declaration</h3>"
    htmlString += "\n<a id=\"whitespace\"></a>"
    htmlString += "\n<ul class=\"blockListLast\">"
    htmlString += "\n<li class=\"blockList\">"
    htmlString += "\n<h4>" + in_constant.name + "</h4>"
    codeString = in_constant.code
    newLineFlag = False
    buildCodeString = ""
    for letter in codeString:
        if letter == "\n":
            newLineFlag = True
            buildCodeString += "<br \/>"
        elif letter == " " and newLineFlag:
            buildCodeString += "&nbsp;&nbsp;"
        else:
            newLineFlag = False
            buildCodeString += letter

    htmlString += "\n<pre class=\"methodSignature\">" + buildCodeString + "</pre>"
    htmlString += "\n</li>"
    htmlString += "\n</ul>"
    htmlString += "\n</li>"
    htmlString += "\n</ul>"
    htmlString += "\n</section>"
    htmlString += "\n</li>"
    htmlString += "\n</ul>"
    htmlString += "\n</div>"

    return htmlString

"""
    Function Name:

        htmlLibraryBody

    Description:

  	    Returns a String contaning the the library body portion of the library page in HTML

    Parameter:

        Library  in_library  the library to create the library body in HTML for

    Returns:

        String  htmlString  the html file string
"""
def htmlLibraryBody(in_library):
    htmlString = ""
    htmlString += "\n<div class=\"details\">"
    htmlString += "\n<ul class=\"blockList\">"
    htmlString += "\n<li class=\"blockList\">"
    htmlString += "\n<section>"
    htmlString += "\n<ul class=\"blockList\">"
    htmlString += "\n<li class=\"blockList\">"
    htmlString += "\n<a id=\"whitespace\"></a>"
    htmlString += "\n<h3>Library Import Statement</h3>"
    htmlString += "\n<a id=\"whitespace\"></a>"
    htmlString += "\n<ul class=\"blockListLast\">"
    htmlString += "\n<li class=\"blockList\">"
    htmlString += "\n<h4>" + in_library.name + "</h4>"
    codeString = in_library.code
    newLineFlag = False
    buildCodeString = ""
    for letter in codeString:
        if letter == "\n":
            newLineFlag = True
            buildCodeString += "<br \/>"
        elif letter == " " and newLineFlag:
            buildCodeString += "&nbsp;&nbsp;"
        else:
            newLineFlag = False
            buildCodeString += letter

    htmlString += "\n<pre class=\"methodSignature\">" + buildCodeString.replace(">", "&gt;").replace("<", "&lt;") + "</pre>"
    htmlString += "\n</li>"
    htmlString += "\n</ul>"
    htmlString += "\n</li>"
    htmlString += "\n</ul>"
    htmlString += "\n</section>"
    htmlString += "\n</li>"
    htmlString += "\n</ul>"
    htmlString += "\n</div>"

    return htmlString


"""
Function Name:

    functionToHTML

Description:

  	Converts a function object into a HTML file

Parameters:

    Function  function  the function to turn into a HTML file

"""
def functionToHTML(function):
    fileHTML = htmlHead(function.name, "..")
    fileHTML += "\n<body>"
    fileHTML += htmlNavBar("")
    fileHTML += "\n<main>"
    fileHTML += "\n<div class=\"header\">"
    fileHTML += "\n<a id=\"whitespace\"></a>"
    fileHTML += "\n<h2 title=\"Function Name\" class=\"title\">" + function.name + "</h2>"
    fileHTML += "\n</div>"
    fileHTML += "\n<div class=\"contentContainer\">"
    fileHTML += "\n<div class=\"description\">"
    fileHTML += "\n</ul>"
    fileHTML += "\n</div>"
    fileHTML += htmlFunctionSummary(function)
    fileHTML += htmlFunctionReferences(function)
    fileHTML += htmlFunctionBody(function)
    fileHTML += "\n</div>"
    fileHTML += "\n</main>"
    fileHTML += "\n</body>"
    fileHTML += "\n</html>"

    htmlFile = open("./" + noExtensionFileName + "/functions/" + function.name + ".html", "w")
    htmlFile.write(fileHTML)
    htmlFile.close()

"""
Function Name:

    variableToHTML

Description:

  	Converts a variable object into a HTML file

Parameters:

    Variable  variable  the variable to turn into a HTML file

"""
def variableToHTML(variable):
    fileHTML = htmlHead(variable.name, "..")
    fileHTML += "\n<body>"
    fileHTML += htmlNavBar("")
    fileHTML += "\n<main>"
    fileHTML += "\n<div class=\"header\">"
    fileHTML += "\n<a id=\"whitespace\"></a>"
    fileHTML += "\n<h2 title=\"Variable Name\" class=\"title\">" + variable.name + "</h2>"
    fileHTML += "\n</div>"
    fileHTML += "\n<div class=\"contentContainer\">"
    fileHTML += "\n<div class=\"description\">"
    fileHTML += "\n</ul>"
    fileHTML += "\n</div>"
    fileHTML += htmlVariableSummary(variable)
    fileHTML += htmlVariableReferences(variable)
    fileHTML += htmlVariableBody(variable)
    fileHTML += "\n</div>"
    fileHTML += "\n</main>"
    fileHTML += "\n</body>"
    fileHTML += "\n</html>"

    htmlFile = open("./" + noExtensionFileName + "/variables/" + variable.name + ".html", "w")
    htmlFile.write(fileHTML)
    htmlFile.close()

"""
Function Name:

    constantToHTML

Description:

  	Converts a Constant object into a HTML file

Parameters:

    Constant  constant  the constant to turn into a HTML file

"""
def constantToHTML(constant):
    fileHTML = htmlHead(constant.name, "..")
    fileHTML += "\n<body>"
    fileHTML += htmlNavBar("")
    fileHTML += "\n<main>"
    fileHTML += "\n<div class=\"header\">"
    fileHTML += "\n<a id=\"whitespace\"></a>"
    fileHTML += "\n<h2 title=\"Constant Name\" class=\"title\">" + constant.name + "</h2>"
    fileHTML += "\n</div>"
    fileHTML += "\n<div class=\"contentContainer\">"
    fileHTML += "\n<div class=\"description\">"
    fileHTML += "\n</ul>"
    fileHTML += "\n</div>"
    fileHTML += htmlConstantSummary(constant)
    fileHTML += htmlConstantReferences(constant)
    fileHTML += htmlConstantBody(constant)
    fileHTML += "\n</div>"
    fileHTML += "\n</main>"
    fileHTML += "\n</body>"
    fileHTML += "\n</html>"

    htmlFile = open("./" + noExtensionFileName + "/constants/" + constant.name + ".html", "w")
    htmlFile.write(fileHTML)
    htmlFile.close()

"""
Function Name:

    libraryToHTML

Description:

  	Converts a Library object into a HTML file

Parameters:

    Library  library  the library to turn into a HTML file

"""
def libraryToHTML(library):
    fileHTML = htmlHead(library.name, "..")
    fileHTML += "\n<body>"
    fileHTML += htmlNavBar("")
    fileHTML += "\n<main>"
    fileHTML += "\n<div class=\"header\">"
    fileHTML += "\n<a id=\"whitespace\"></a>"
    fileHTML += "\n<h2 title=\"Library Name\" class=\"title\">" + library.name.replace(">", "&gt;").replace("<", "&lt;") + "</h2>"
    fileHTML += "\n</div>"
    fileHTML += "\n<div class=\"contentContainer\">"
    fileHTML += "\n<div class=\"description\">"
    fileHTML += "\n</ul>"
    fileHTML += "\n</div>"
    fileHTML += htmlLibrarySummary(library)
    fileHTML += htmlLibraryBody(library)
    fileHTML += "\n</div>"
    fileHTML += "\n</main>"
    fileHTML += "\n</body>"
    fileHTML += "\n</html>"

    htmlFile = open("./" + noExtensionFileName + "/libraries/" + library.name.replace(">", "").replace("<", "") + ".html", "w")
    htmlFile.write(fileHTML)
    htmlFile.close()


"""
Function Name:

    checkDirectoryAvailability

Description:

  	Checks if the directory for the documentation is available, exits if it is not
"""
def checkDirectoryAvailability():
    path = os.getcwd()
    path += "./" + noExtensionFileName
    if os.path.exists(path):
        exitMessage("Directory " + path + " is already in use, delete it and retry", 1)


"""
Function Name:

    createDirectories

Description:

  	Creates the neccesary directories for the documentation
"""
def createDirectories():
    path = os.getcwd()
    path += "./" + noExtensionFileName
    os.mkdir(path)
    os.mkdir(path + "\\functions")
    os.mkdir(path + "\\variables")
    os.mkdir(path + "\\constants")
    os.mkdir(path + "\\libraries")
    os.mkdir(path + "\\indexes")
    os.mkdir(path + "\\stylesheets")
    # Maybe in the future...
    #os.mkdir(path + "\\TypeDefs")
    #os.mkdir(path + "\\Objects")

"""
Function Name:

    writeCSS

Description:

  	Writes CSS stylesheet to the top level directory of the documentation for reference from HTML files

"""
def writeCSS():
    cssFile = open("./" + noExtensionFileName + "/stylesheets/stylesheet.css", "w")
    cssFile.write(stylesheetCSS)
    cssFile.close()

"""
Function Name:

    dataToHTML

Description:

    Writes data present in objects to HTML files within respective files along with writing index files

"""
def dataToHTML():
    for function in documentedFunctions:
        functionToHTML(function)

    for variable in documentedVariables:
        variableToHTML(variable)

    for constant in documentedConstants:
        constantToHTML(constant)

    for library in documentedLibraries:
        libraryToHTML(library)



"""
Function Name:

    writeIndexHTML

Description:

    Writes out the HTML for creating indexs under the indexes directory of generated documentation

"""
def writeIndexHTML():
    functionsIndexHTML()
    variablesIndexHTML()
    constantsIndexHTML()
    librariesIndexHTML()

"""
Function Name:

    functionsIndexHTML

Description:

  	Creates the HTML for the function index page
"""
def functionsIndexHTML():
    fileHTML = htmlHead("Function Index", "..")
    fileHTML += "\n<body>"
    fileHTML += htmlNavBar("Functions")
    fileHTML += "\n<main>"
    fileHTML += "\n<div class=\"header\">"
    fileHTML += "\n<a id=\"whitespace\"></a>"
    fileHTML += "\n<h2 title=\"Function Index Header\" class=\"title\">Function Index</h2>"
    fileHTML += "\n</div>"
    fileHTML += "\n<div class=\"contentContainer\">"
    fileHTML += "\n<div class=\"description\">"
    fileHTML += "\n</ul>"
    fileHTML += "\n</div>"
    fileHTML += "\n<div class=\"details\">"
    fileHTML += "\n<ul class=\"blockList\">"
    fileHTML += "\n<section>"
    fileHTML += "\n<ul class=\"blockList\">"
    fileHTML += "\n<li class=\"blockList\">"
    fileHTML += "\n<a id=\"whitespace\"></a>"
    fileHTML += "\n<h3>Functions</h3>"
    fileHTML += "\n<a id=\"whitespace\"></a>"

    if len(documentedFunctions) >= 1:
        fileHTML += "\n<table class=\"memberSummary\">"
        fileHTML += "\n<caption><span>Index</span><span class=\"tabEnd\">&nbsp;</span></caption>"
        fileHTML += "\n<tr>"
        fileHTML += "\n<th class=\"colFirst\" scope=\"col\">Name</th>"
        fileHTML += "\n<th class=\"colSecond\" scope=\"col\">Parameter Count</th>"
        fileHTML += "\n<th class=\"colSecond\" scope=\"col\">Return Type</th>"
        fileHTML += "\n<th class=\"colSecond\" scope=\"col\">Functions Called</th>"
        fileHTML += "\n<th class=\"colSecond\" scope=\"col\">Global Variables Manipulated</th>"
        fileHTML += "\n<th class=\"colLast\" scope=\"col\">Constants Referenced</th>"
        fileHTML += "</tr>"
        fileHTML += "<tr id=\"i0\" class=\"altColor\">"


        for function in documentedFunctions:
            fileHTML += "\n<tr id=\"i0\" class=\"altColor\">"
            fileHTML += "\n<td class=\"colFirst\"><code><a href=\"../functions/" + function.name + ".html\">" + function.name + "</a></code></td>"
            fileHTML += "\n<td class=\"colSecond\"><div class=\"block\"><code>" + str(len(function.parameters)) + "</code></div></td>"
            if function.returnValue != None:
                fileHTML += "\n<th class=\"colSecond\" scope=\"row\"><code>" + function.returnValue.pointer_depth * "*" + function.returnValue.dataType + "</code></th>"
            else:
                fileHTML += "\n<th class=\"colSecond\" scope=\"row\"><code>void</code></th>"
            fileHTML += "\n<td class=\"colSecond\"><div class=\"block\"><code>" + str(len(function.functionCalls)) + "</code></div></td>"
            fileHTML += "\n<td class=\"colSecond\"><div class=\"block\"><code>" + str(len(function.variables)) + "</code></div></td>"
            fileHTML += "\n<td class=\"colLast\"><div class=\"block\"><code>" + str(len(function.constants)) + "</code></div></td>"
            fileHTML += "\n</tr>"

        fileHTML += "\n</table>"

    fileHTML += "\n</section>"
    fileHTML += "\n</li>"
    fileHTML += "\n</ul>"
    fileHTML += "\n</li>"
    fileHTML += "\n</ul>"
    fileHTML += "\n</ul>"
    fileHTML += "\n</div>"

    fileHTML += "\n</div>"
    fileHTML += "\n</main>"
    fileHTML += "\n</body>"
    fileHTML += "\n</html>"

    htmlFile = open("./" + noExtensionFileName + "/indexes/functionsIndex.html", "w")
    htmlFile.write(fileHTML)
    htmlFile.close()

"""
Function Name:

    variablesIndexHTML

Description:

  	Creates the HTML for the variable index page
"""
def variablesIndexHTML():
    fileHTML = htmlHead("Variable Index", "..")
    fileHTML += "\n<body>"
    fileHTML += htmlNavBar("Variables")
    fileHTML += "\n<main>"
    fileHTML += "\n<div class=\"header\">"
    fileHTML += "\n<a id=\"whitespace\"></a>"
    fileHTML += "\n<h2 title=\"Variable Index Header\" class=\"title\">Variable Index</h2>"
    fileHTML += "\n</div>"
    fileHTML += "\n<div class=\"contentContainer\">"
    fileHTML += "\n<div class=\"description\">"
    fileHTML += "\n</ul>"
    fileHTML += "\n</div>"
    fileHTML += "\n<div class=\"details\">"
    fileHTML += "\n<ul class=\"blockList\">"
    fileHTML += "\n<section>"
    fileHTML += "\n<ul class=\"blockList\">"
    fileHTML += "\n<li class=\"blockList\">"
    fileHTML += "\n<a id=\"whitespace\"></a>"
    fileHTML += "\n<h3>Variables</h3>"
    fileHTML += "\n<a id=\"whitespace\"></a>"

    if len(documentedVariables) >= 1:
        fileHTML += "\n<table class=\"memberSummary\">"
        fileHTML += "\n<caption><span>Index</span><span class=\"tabEnd\">&nbsp;</span></caption>"
        fileHTML += "\n<tr>"
        fileHTML += "\n<th class=\"colFirst\" scope=\"col\">Name</th>"
        fileHTML += "\n<th class=\"colSecond\" scope=\"col\">Data Type</th>"
        fileHTML += "\n<th class=\"colSecond\" scope=\"col\">Inital Value</th>"
        fileHTML += "\n<th class=\"colLast\" scope=\"col\">Function Usage Count</th>"
        fileHTML += "</tr>"
        fileHTML += "<tr id=\"i0\" class=\"altColor\">"


        for variable in documentedVariables:
            fileHTML += "\n<tr id=\"i0\" class=\"altColor\">"
            fileHTML += "\n<td class=\"colFirst\"><code><a href=\"../variables/" + variable.name + ".html\">" + variable.name + "</a></code></td>"
            fileHTML += "\n<th class=\"colSecond\" scope=\"row\"><code>" + variable.pointer_depth * "*" + variable.dataType + "</code></th>"
            fileHTML += "\n<th class=\"colSecond\" scope=\"row\"><code>" + variable.inital_value + "</code></th>"
            fileHTML += "\n<td class=\"colLast\">"
            fileHTML += "\n<div class=\"block\"><code>" + str(len(variable.usage)) + "</code></div>"
            fileHTML += "\n</td>"
            fileHTML += "\n</tr>"

        fileHTML += "\n</table>"

    fileHTML += "\n</section>"
    fileHTML += "\n</li>"
    fileHTML += "\n</ul>"
    fileHTML += "\n</li>"
    fileHTML += "\n</ul>"
    fileHTML += "\n</ul>"
    fileHTML += "\n</div>"

    fileHTML += "\n</div>"
    fileHTML += "\n</main>"
    fileHTML += "\n</body>"
    fileHTML += "\n</html>"

    htmlFile = open("./" + noExtensionFileName + "/indexes/variablesIndex.html", "w")
    htmlFile.write(fileHTML)
    htmlFile.close()

"""
Function Name:

    constantsIndexHTML

Description:

  	Creates the HTML for the constants index page
"""
def constantsIndexHTML():
    fileHTML = htmlHead("Constant Index", "..")
    fileHTML += "\n<body>"
    fileHTML += htmlNavBar("Constants")
    fileHTML += "\n<main>"
    fileHTML += "\n<div class=\"header\">"
    fileHTML += "\n<a id=\"whitespace\"></a>"
    fileHTML += "\n<h2 title=\"Constant Index Header\" class=\"title\">Constant Index</h2>"
    fileHTML += "\n</div>"
    fileHTML += "\n<div class=\"contentContainer\">"
    fileHTML += "\n<div class=\"description\">"
    fileHTML += "\n</ul>"
    fileHTML += "\n</div>"
    fileHTML += "\n<div class=\"details\">"
    fileHTML += "\n<ul class=\"blockList\">"
    fileHTML += "\n<section>"
    fileHTML += "\n<ul class=\"blockList\">"
    fileHTML += "\n<li class=\"blockList\">"
    fileHTML += "\n<a id=\"whitespace\"></a>"
    fileHTML += "\n<h3>Constants</h3>"
    fileHTML += "\n<a id=\"whitespace\"></a>"

    if len(documentedConstants) >= 1:
        fileHTML += "\n<table class=\"memberSummary\">"
        fileHTML += "\n<caption><span>Index</span><span class=\"tabEnd\">&nbsp;</span></caption>"
        fileHTML += "\n<tr>"
        fileHTML += "\n<th class=\"colFirst\" scope=\"col\">Name</th>"
        fileHTML += "\n<th class=\"colSecond\" scope=\"col\">Value</th>"
        fileHTML += "\n<th class=\"colLast\" scope=\"col\">Function Usage Count</th>"
        fileHTML += "\n<th class=\"colLast\" scope=\"col\">Assumed Data Type</th>"
        fileHTML += "</tr>"
        fileHTML += "<tr id=\"i0\" class=\"altColor\">"


        for constant in documentedConstants:
            fileHTML += "\n<tr id=\"i0\" class=\"altColor\">"
            fileHTML += "\n<td class=\"colFirst\"><code><a href=\"../constants/" + constant.name + ".html\">" + constant.name + "</a></code></td>"
            fileHTML += "\n<th class=\"colSecond\" scope=\"row\"><code>" + constant.value + "</code></th>"
            fileHTML += "\n<th class=\"colSecond\" scope=\"row\"><code>" + str(len(constant.usage)) + "</code></th>"
            fileHTML += "\n<td class=\"colLast\">"
            fileHTML += "\n<div class=\"block\">" + constant.dataType + "</div>"
            fileHTML += "\n</td>"
            fileHTML += "\n</tr>"

        fileHTML += "\n</table>"

    fileHTML += "\n</section>"
    fileHTML += "\n</li>"
    fileHTML += "\n</ul>"
    fileHTML += "\n</li>"
    fileHTML += "\n</ul>"
    fileHTML += "\n</ul>"
    fileHTML += "\n</div>"

    fileHTML += "\n</div>"
    fileHTML += "\n</main>"
    fileHTML += "\n</body>"
    fileHTML += "\n</html>"

    htmlFile = open("./" + noExtensionFileName + "/indexes/constantsIndex.html", "w")
    htmlFile.write(fileHTML)
    htmlFile.close()

"""
Function Name:

    librariesIndexHTML

Description:

  	Creates the HTML for the libraries index page
"""
def librariesIndexHTML():
    fileHTML = htmlHead("Libraries Index", "..")
    fileHTML += "\n<body>"
    fileHTML += htmlNavBar("Libraries")
    fileHTML += "\n<main>"
    fileHTML += "\n<div class=\"header\">"
    fileHTML += "\n<a id=\"whitespace\"></a>"
    fileHTML += "\n<h2 title=\"Library Index Header\" class=\"title\">Library Index</h2>"
    fileHTML += "\n</div>"
    fileHTML += "\n<div class=\"contentContainer\">"
    fileHTML += "\n<div class=\"description\">"
    fileHTML += "\n</ul>"
    fileHTML += "\n</div>"
    fileHTML += "\n<div class=\"details\">"
    fileHTML += "\n<ul class=\"blockList\">"
    fileHTML += "\n<section>"
    fileHTML += "\n<ul class=\"blockList\">"
    fileHTML += "\n<li class=\"blockList\">"
    fileHTML += "\n<a id=\"whitespace\"></a>"
    fileHTML += "\n<h3>Libraries</h3>"
    fileHTML += "\n<a id=\"whitespace\"></a>"

    if len(documentedLibraries) >= 1:
        fileHTML += "\n<table class=\"memberSummary\">"
        fileHTML += "\n<caption><span>Index</span><span class=\"tabEnd\">&nbsp;</span></caption>"
        fileHTML += "\n<tr>"
        fileHTML += "\n<th class=\"colFirst\" scope=\"col\">Name</th>"
        fileHTML += "\n<th class=\"colLast\" scope=\"col\">Description</th>"
        fileHTML += "</tr>"
        fileHTML += "<tr id=\"i0\" class=\"altColor\">"


        for library in documentedLibraries:
            fileHTML += "\n<tr id=\"i0\" class=\"altColor\">"
            fileHTML += "\n<td class=\"colFirst\"><code><a href=\"../libraries/" + library.name.replace(">", "").replace("<", "") + ".html\">" + library.name.replace(">", "").replace("<", "") + "</a></code></td>"
            fileHTML += "\n<td class=\"colLast\">"
            fileHTML += "\n<div class=\"block\">" + library.description.replace("\n", "<br \/>") + "</div>"
            fileHTML += "\n</td>"
            fileHTML += "\n</tr>"

        fileHTML += "\n</table>"

    fileHTML += "\n</section>"
    fileHTML += "\n</li>"
    fileHTML += "\n</ul>"
    fileHTML += "\n</li>"
    fileHTML += "\n</ul>"
    fileHTML += "\n</ul>"
    fileHTML += "\n</div>"

    fileHTML += "\n</div>"
    fileHTML += "\n</main>"
    fileHTML += "\n</body>"
    fileHTML += "\n</html>"

    htmlFile = open("./" + noExtensionFileName + "/indexes/librariesIndex.html", "w")
    htmlFile.write(fileHTML)
    htmlFile.close()

def writeHomeHTML():
    global currentLineIndex
    fileHTML = htmlHead("Home", ".")
    fileHTML += "\n<body>"
    fileHTML += "\n<body>"
    fileHTML += "\n<header>"
    fileHTML += "\n<nav>"
    fileHTML += "<div class=\"topNav\">"
    fileHTML += "<a id=\"navbar.top\"></a>"
    fileHTML += "\n<ul class=\"navList\" title=\"Navigation\">"

    fileHTML += "\n<li class=\"navBarCell1Rev\">Home</li>"
    fileHTML += "\n<li><a href=\"./indexes/functionsIndex.html\">Functions</a></li>"
    fileHTML += "\n<li><a href=\"./indexes/variablesIndex.html\">Variables</a></li>"
    fileHTML += "\n<li><a href=\"./indexes/constantsIndex.html\">Constants</a></li>"
    fileHTML += "\n<li><a href=\"./indexes/librariesIndex.html\">Libraries</a></li>"
    fileHTML += "\n</header>"

    fileHTML += "\n<main>"
    fileHTML += "\n<div class=\"header\">"
    fileHTML += "\n<a id=\"whitespace\"></a>"
    fileHTML += "\n<h2 title=\"Homepage Header\" class=\"title\">" + path + "</h2>"
    fileHTML += "\n</div>"
    fileHTML += "\n<div class=\"contentContainer\">"
    fileHTML += "\n<div class=\"description\">"
    fileHTML += "\n</ul>"
    fileHTML += "\n</div>"

    fileHTML += "\n<div class=\"details\">"
    fileHTML += "\n<ul class=\"blockList\">"
    fileHTML += "\n<section>"
    fileHTML += "\n<ul class=\"blockList\">"
    fileHTML += "\n<li class=\"blockList\">"
    fileHTML += "\n<a id=\"whitespace\"></a>"
    fileHTML += "\n<h3>Program Overview</h3>"
    fileHTML += "\n<a id=\"whitespace\"></a>"



    fileHTML += "\n<table class=\"memberSummary\">"
    fileHTML += "\n<caption><span>Size</span><span class=\"tabEnd\">&nbsp;</span></caption>"
    fileHTML += "\n<tr>"
    fileHTML += "\n<th class=\"colFirst\" scope=\"col\">Functions</th>"
    fileHTML += "\n<th class=\"colSecond\" scope=\"col\">Variables</th>"
    fileHTML += "\n<th class=\"colSecond\" scope=\"col\">Constants</th>"
    fileHTML += "\n<th class=\"colSecond\" scope=\"col\">Libraries</th>"
    fileHTML += "\n<th class=\"colLast\" scope=\"col\">Lines</th>"
    fileHTML += "</tr>"
    fileHTML += "<tr id=\"i0\" class=\"altColor\">"

    fileHTML += "\n<tr id=\"i0\" class=\"altColor\">"
    fileHTML += "\n<td class=\"colFirst\"><code>" + str(len(documentedFunctions)) + "</code></td>"
    fileHTML += "\n<td class=\"colSecond\"><code>" + str(len(documentedVariables)) + "</code></td>"
    fileHTML += "\n<td class=\"colSecond\"><code>" + str(len(documentedConstants)) + "</code></td>"
    fileHTML += "\n<td class=\"colSecond\"><code>" + str(len(documentedLibraries)) + "</code></td>"
    fileHTML += "\n<td class=\"colLast\">"
    fileHTML += "\n<code>" + str(currentLineIndex) + "</code>"
    fileHTML += "\n</td>"
    fileHTML += "\n</tr>"

    fileHTML += "\n</table>"

    fileHTML += "\n</section>"
    fileHTML += "\n</li>"
    fileHTML += "\n</ul>"
    fileHTML += "\n</li>"
    fileHTML += "\n</ul>"
    fileHTML += "\n</ul>"
    fileHTML += "\n</div>"

    fileHTML += "\n</div>"
    fileHTML += "\n</main>"
    fileHTML += "\n</body>"
    fileHTML += "\n</html>"

    htmlFile = open("./" + noExtensionFileName + "/home.html", "w")
    htmlFile.write(fileHTML)
    htmlFile.close()


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
    noExtensionFileName = path.replace(extension, "")
    break

checkDirectoryAvailability()

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
	elif isFunctionHeader(currentLine):
		harvestFunction()
	elif isVariableDeclaration(currentLine):
		harvestVariable(currentLine)
	elif isConstantDeclaration(currentLine):
		harvestConstant(currentLine)
	elif isLibraryImport(currentLine):
		harvestLibraryImport(currentLine)

for function in documentedFunctions:
    analyzeFunctionBody(function)

createDirectories()
writeCSS()
dataToHTML()
writeIndexHTML()
writeHomeHTML()
