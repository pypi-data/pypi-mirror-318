#!/usr/bin/env python3  
  
import sys  
from lexer import Lexer  
from parser import Parser  
from interpreter import Interpreter  
  
def main():  
    if len(sys.argv) != 2:  
        print("Usage: muji <filename.muji>")  
        sys.exit(1)  
  
    filename = sys.argv[1]  
    if not filename.endswith('.muji'):  
        print("Error: File must have a .muji extension")  
        sys.exit(1)  
  
    try:  
        with open(filename, 'r') as file:  
            text = file.read()  
    except FileNotFoundError:  
        print(f"Error: File '{filename}' not found")  
        sys.exit(1)  
  
    lexer = Lexer(text)  
    parser = Parser(lexer)  
    interpreter = Interpreter(parser)  
  
    try:  
        interpreter.interpret()  
    except Exception as e:  
        print(e)  
  
if __name__ == '__main__':  
    main()  