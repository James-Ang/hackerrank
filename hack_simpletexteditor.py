# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 08:05:05 2021

@author: James Ang
"""

import sys

commands = []

if __name__ == "__main__":
    firstLine = False
    
    for line in sys.stdin:
        if not firstLine:
            firstLine = True
        else:
            line = line.rstrip()
            if line.startswith("1"):
                if len(commands) == 0:
                    commands.append(line[2:])
                else:
                    commands.append(commands[-1] + line[2:])
            elif line.startswith("2"):
                point = len(commands[-1]) - int(line[2:])
                commands.append(commands[-1][:point])
            elif line.startswith("3"):
                print(commands[-1][int(line[2:]) - 1])
            elif line.startswith("4"):
                commands.pop()