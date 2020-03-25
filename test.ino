#define   selectPin 25 //the input pin for the select button
#define   enterPin    27    //enterPin  the input pin for the enter button
#define   chipSelectPin 4 //chipSelectPin  the chip select pin for the SD card module
#define adcPin    A1    //adcPin  the input pin for adc reading


#define   NULL 0    //0/none type defintion
#define    true   1    //true boolean type definition
#define   false 0    //false boolean type definition
double voltInit = 1023; //the voltage threshold to start recording sample data at
double voltMin = 1018; //the volage threshold to stop recording sample data at
double *** * ** ** ** * * maxProx; //maxProx  maximum proximity to thresholds to count as being at the thresholds
#define dataPointLimit 100 //the maximum amount of data points that can be analyzed at once
#define    voltageMaxNum    1240    //the numeric upper limit of the voltage readings
#define  voltageMax 1.5 //the voltage upper limit of the voltage readings in volts
#define  xSmoothing 5   //the number of points that are averaged together when processing the signal
#define   maxConsec   50 //the number of times the average signal value must be at voltMin to indicate full activation
void *(*foo)(int *); //wow



/*
* Function Name:
*
*   testHeader
*
* Description:
*
*   testy testy, pleasd work so I can resty
*
* Parameters:
*
*   N/A
*
* Returns:
*
*   N/A
*/
