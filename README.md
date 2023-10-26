# SnakeDoc: Automated Documentation Generator for .ino files 📜🐍

SnakeDoc is a tool designed to generate Java-doc style website documentation for Arduino/C++ code. if your code comments follow a standardized format, SnakeDoc will generate comprehensive documentation for you.
Features

## Prerequisites

    Arduino/C++ codebase with comments in the SnakeDoc standardized format.

## Usage 🛠

    Clone the repository.
    Run SnakeDoc on your Arduino/C++ project.
    Navigate to the generated documentation website.

## Standardized Format 📝

Here's a snapshot of the expected format, for an Arduino C SDCard reader function:

```
#define dataPointLimit 100 //the maximum amount of data points that can be analyzed at once

/*
* Function Name:
*   sdResponse
* Description:
*   Takes in a file object from an SD card and returns a string with all the data from that file
* Parameters:
*   File  file  the file to read the response from
* Returns:
*   String  response  characters from the SD card sent to the microcontroller
*/
String sdResponse(File file) {
  // ... function implementation ...
}```
