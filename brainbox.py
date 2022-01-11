import sys
import time

class SyntaxException(Exception):
    pass

class Interpreter:
    # Simple interpreter for Brainfuck code
    mem = []
    ptr = 0
    def __init__(self):
        self.reset()
        
    def reset(self):
        # Empty memory
        self.mem = [0,0,0]
        
    def handle_loops(self, chars):
        # Find loops
        loops, loopsd = [], {}
        for n, c in enumerate(chars):
            if c == "[":
                # Add in the location of the starting bracket
                loops.append(n)
            if c == "]":
                # Remove last item from the list, and append the starting point and ending point
                s = loops.pop()
                loopsd[n] = s
                loopsd[s] = n
        return loopsd
    
    def execute(self, string):
        # Interpreter
        start_time = time.time()
        if (string.count('[') != string.count(']')):
            raise SyntaxException("Program contains unclosed loops")
            return
        self.ptr = 0
        chars = list(string)
        loops = self.handle_loops(chars)
        idx = 0
        while idx < len(chars):
            c = chars[idx]
            # Increment and decrement the pointer
            if c == ">":
                self.ptr = self.ptr + 1
                # Memory is just-in-time
                if (self.ptr >= len(self.mem)):
                    self.mem.append(0)
            elif c == "<":
                self.ptr = self.ptr - 1 if self.ptr > 0 else len(self.mem)-1
            # Increment and decrement values
            elif c == "+":
                inc = self.mem[self.ptr] + 1
                self.mem[self.ptr] = inc if self.mem[self.ptr] < 255 else 0     
            elif c == "-":
                dec = self.mem[self.ptr] - 1
                self.mem[self.ptr] = dec if self.mem[self.ptr] > 0 else 255
            # Accept and return input
            elif c == ".":
                sys.stdout.write(chr(self.mem[self.ptr]))
            elif c == ",":
                self.mem[self.ptr] = ord(input(">")[0])
            # Loops
            elif c == "[" and self.mem[self.ptr] == 0:
                idx = loops[idx]
            elif c == "]" and self.mem[self.ptr] != 0:
                idx = loops[idx]
            idx += 1
        print("\nProgram used %s bits of memory, and finished evaluation in %s seconds."%(len(self.mem),str(time.time()-start_time)))
                
