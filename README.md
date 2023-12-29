# SnakeDoc: Automated Java-Doc Style Documentation Generator for Arduino C

SnakeDoc is a tool designed to generate Java-doc style website documentation for Arduino C code. if your code comments follow a standardized format, SnakeDoc will generate comprehensive documentation for you.

## Features

    Automated Generation: SnakeDoc will automatically generate documentation for yuour Arduion C code provided it is properly commented.
    Java-doc Style: Familiar Java-doc style documentation for developers acquainted with Java's documentation style.

## Prerequisites

    Arduino C codebase with comments in the SnakeDoc standardized format.

## Usage

    1. Clone the repository.
    2. Run SnakeDoc on your Arduino C project.
    3. Navigate to the generated documentation website.

## Example Format

Here's a snapshot of the expected format, for an Arduino SDCard reader function:

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
