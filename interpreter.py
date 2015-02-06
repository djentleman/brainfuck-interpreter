
import random

def checkBrackets(tape):
    # parse tape
    stack = []
    state = 0
    for char in tape:
        if not char in "[]":
            continue
        # it's a bracket
        if state == 0:
            if char == "[":
                state = 1
                stack.append("A")
            if char == "]":
                return 0
        elif state == 1:
            if char == "[":
                state = 1
                stack.append("A")
            if char == "]":
                stack = stack[:-1]
                if stack == []:
                    state = 0
                else:
                    state = 1
    if state == 0:
        return 1
    else:
        return 0
            
def check(tape):
    # bit nasty
    status = checkBrackets(tape)
    if "[]" in tape:
        status = 0
    return status

def generateTape(k):
    tape = ""
    for i in range(k):
        r = random.randint(0,8)
        if r == 1:
            tape += "+"
        elif r == 2:
            tape += "-"
        elif r == 3:
            tape += ">"
        elif r == 4:
            tape += "<"
        elif r == 5:
            tape += "."
        elif r == 6:
            tape += "["
        elif r == 7:
            tape += "]"
        else:# r == 0:
            tape += "," # will be ","
    return tape

def dumpTape(tape, p):
    s = ""
    for i in range(len(tape)):
        c = tape[i]
        if p == i:
            s += "(" + str(c) + ")"
        else:
            s += " " + str(c) + " "
    return s     

def run(tape, intape, debug=False):
    memory = [0]
    ptr = 0
    idx = 0
    inidx = 0
    if debug:
            #print "---"
            #print "---"
            #print "Tape"
            print "Tape: " + dumpTape(tape, -1)
            #print "Memory:"
            print "Memory: " + dumpTape(memory, ptr)
            print "Input: " + dumpTape(intape, inidx)
            print ""
            #print "---"
    while True:
        if idx == len(tape):
            break
        
        

            
        char = tape[idx]
        if char == ".":
            print memory[ptr]
        if char == "+":
            memory[ptr]+=1
            if memory[ptr] == 256:
                memory[ptr] = 0 # overflow
        if char == "-":
            memory[ptr]-=1
            if memory[ptr] == -1:
                memory[ptr] = 255 # underflow
        if char == ">":
            ptr+=1
            # if the ptr is outside memory, extend memory
            if len(memory) == ptr:
                memory += [0]
        if char == "<":
            ptr-=1
            if ptr == -1:
                memory = [0] + memory
                ptr = 0
        if char == "[":
            idx += 1
            continue

        if char == ",":
            if inidx < len(intape):
                memory[ptr] = intape[inidx]
                inidx+=1
            # ekse do nothing

        if char == "]":
            if memory[ptr] == 0:
                idx += 1
                continue # exit loop
            # keep looping
            nested = 0
            tmp = idx - 1
            while 1:
                if tape[tmp] == "[":
                    nested -= 1
                    if nested == -1:
                        idx = tmp+1
                        break
                if tape[tmp] == "]":
                    nested += 1
                tmp -= 1
            continue
            
        if debug:
            #print "---"
            #print "---"
            #print "Tape"
            print "Tape: " + dumpTape(tape, idx)
            #print "Memory:"
            #print "Memory: " + dumpTape(memory, ptr)
            #print "Input: " + dumpTape(intape, inidx)
            #print ""
            #print "---"
        
        idx += 1

        
        
            
        
            

def main():
    while 1:
        tape = generateTape(30)
        if check(tape):
            break
    tape = "+++[>++++<-]>+[>+++++<-]>."
    #tape = ",>,<[>+<-]>."
    print tape
    run(tape, [5, 10], 1)
        
    

if __name__ == "__main__":
  main()
