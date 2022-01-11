# brainbox
 A lightweight, simple Python-based interpreter for Brainfuck.

# Intro

 Brainfuck is an esoteric language &mdash; esolang &mdash; invented by Swiss physics student Urban M&Luml;ller in 1993 for the Amiga operating system, with the intent of designing a programming language with the smallest possible compiler.

 Brainfuck isn't designed for actual use, but to be confusing &amp; difficult to understand. Brainfuck has no variables, functions, or other high-level things. Brainfuck is Turing complete, but not 

# Tutorial:
 
 Brainfuck has 8 commands, and movable data and instruction pointers with a finite amount of memory. Most implementations have only 30,000 bits available, but this implementation has just-in-time memory which expands as it is needed.

## The Pointers
###### Instruction Pointer
This pointer points to the instruction in the program for the interpreter to follow.

###### Data Pointer
This pointer points to a given byte in memory, and can be used to change or read memory.

## Brainfuck's 8 commands:
###### > (Greater Than)
This command moves the data pointer right. In this implementation, if the pointer position exceeds the memory size, more space is added just-in-time. 

###### < (Less Than)
This command moves the data pointer left. In this implementation, the pointer wraps back to the end of memory if it attempts to go below position 0 in memory.

###### + (Plus)
This command increments the value in the memory location the pointer points at by 1. If it goes above 255, it wraps back to 0.

###### - (Minus)
This command decrements the value in the memory location the pointer points at by 1. If it tries to go below 0, it wraps back to 255.

###### . (Period)
This command prints the ASCII value of the current memory location.

###### , (Comma)
This command takes 1 byte of user input (using python input() in this implementation) and writes it to the current memory location.

###### \[ (Opening Bracket)
If the byte at the data pointer is zero, it skips the instruction pointer to the next closing bracket. If not, it skips the instruction pointer to the next instruction.

###### \] (Closing Bracket) 
If the byte at the data pointer is nonzero, it moves the instruction pointer to the last opening bracket. If not, it skips the instruction pointer to the next instruction to its right.

 Anything else, even whitespace, is a comment.


 # Some Examples
 ## Hi!
 This Brainfuck program prints the text Hi! to the console. 
 ```
 +[----->+++<]>+. print the character "h"
 +. print the character "i"
 <++++++++++[>-------<-]>--. print the exclamation mark
 ```
 ###### How does it work?
 (pointer being the data pointer)
 First, the character H is printed. Byte 0x00 is set to 1, then subtracted by 5.
 Byte 0x01 is then incremented by 3, and the pointer is moved back to byte 0x00.
 This is looped until the value reaches 0.
 The pointer is then advanced to byte 0x01, and the value incremented by 1 for a value of 104 (lowercase h in ASCII), which is printed.

 Second, the value of byte 0x01 is incremented by 1, giving 105, the ASCII value for I, which is printed.

 Third, the pointer is moved to byte 0x00. Byte 0x00's value is then incremented by 10.
 The pointer is then moved to Byte 0x01, which is decremented by 7, then the pointer is moved back to byte 0x00. 
 At the end of the loop, the pointer is moved to Byte 0x01, which is then decremented by 2, giving the ASCII value 33, which is an exclamation point, which is printed.


 ## Adding 2 numbers
 This Brainfuck program adds 2 numbers (6 and 3). 
 ```
++++++ set byte 0x00 to 6
> +++ set byte 0x01 to 3

[<+>-] add byte 0x01 to byte 0x00
++++++[<++++++++>-]<. add 48 to it to print a number
```
###### How does it work?
(pointer, again, is the data pointer)
First, byte 0x00's value is incremented by 6. 
Second, the pointer is moved to byte 0x01, which is incremented by 3.
In a loop that repeats until byte 0x01 is zero, the pointer is moved to byte 0x00, which is incremented by one, then moved back to byte 0x01, which is decremented by one.
48 (the ASCII value for 0) is then added to byte 0x00, using a similar process, but instead of incrementing by one 3 times, it increments by eight six times. The pointer is them moved to byte 0x01, which is displayed. 


# The Brainbox library
Brainbox is an interpreter for Brainfuck, written entirely in Python. Just import the module, then create an instance of the class and use the "execute" method to run your code. Any of the provided programs, or others, can be used as tests.