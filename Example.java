package exa; 
  
import java.util.Scanner; 
  
/** 
* 
* @author Yash 
*/
public class Example { 
    /** 
* This is a program for adding two numbers in java. 
    * @param args 
*/
    public static void main(String[] args) 
    { 
        /** 
        * This is the main method  
        * which is very important for  
        * execution for a java program. 
        */
  
        int x, y; 
        Scanner sc = new Scanner(System.in); 
        /** 
        * Declared two variables x and y.  
        * And taking input from the user  
        * by using Scanner class.  
        * 
        */
  
        x = sc.nextInt(); 
        y = sc.nextInt(); 
        /** 
        * Storing the result in variable sum  
        * which is of the integer type. 
        */
        int sum = x + y; 
  
        /** 
        * Using standard output stream  
        * for giving the output. 
        * @return null 
        */
        System.out.println("Sum is: " + sum); 
    } 
} 
