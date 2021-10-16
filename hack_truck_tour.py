# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 19:53:05 2021

@author: James Ang
"""

def truckTour(petrolpumps):
    # Write your code here
    tank = 0
    i = 0
    
    for amt,dist in petrolpumps:
        
        tank += amt
        tank -= dist
        
        if tank <0:
            print("failed")
            petrolpumps.append(petrolpumps.pop(0))
            break
        
    
    
    
    return truckTour(petrolpumps)


def truckTour2(petrolpumps):
    # Write your code here
    

    
    for j in range(len(petrolpumps)):
        tank = 0
        
        for i in range(len(petrolpumps)):
            print(i)
            tank += petrolpumps[i][0]
            tank -= petrolpumps[i][1]
            
            if tank <0:
                print("failed")
                petrolpumps.append(petrolpumps.pop(0))
                break
        
        if tank > 0:
            print(j)
            break

        
    
    return j


def truckTour3(petrolpumps):    # USE THIS FINAL ONE
    # Write your code here
    
    pump = 0
    tank = 0
        
    for i in range(len(petrolpumps)):
        # print(i)
        tank += petrolpumps[i][0] - petrolpumps[i][1]
        #tank -= 
        
        if tank <0:
            # print("failed")
            # petrolpumps.append(petrolpumps.pop(0))
            tank = 0
            pump = i + 1

    return pump

    


if __name__ == '__main__':
    n = 3
    petrolpumps = [[1, 5], [10, 3], [3, 4]]
    result = truckTour3(petrolpumps)
    print(result)