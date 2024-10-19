#!/usr/bin/env python3

import time
import random
import string
import sys 
import csv

def find_combination(target, coins, capacity):
    for start_coin in coins:
        combinations = [[start_coin]]
        visited = set()
        while combinations:
            current_combination = combinations.pop(0)
            current_sum = sum(current_combination)
            if current_sum == target:
                return current_combination 
            if current_sum > target:
                continue
            for coin in coins:
                new_combination = current_combination + [coin]
                new_sum = sum(new_combination)
                if new_sum not in visited:
                    visited.add(new_sum) 
                    if len(new_combination) <= capacity:
                        combinations.append(new_combination)  
    return None 

def get_data():
    data=[]
    iteration=0
    for line in sys.stdin.readlines():
        start=time.time()
        line=line.strip().split(', ')
        point={}
        target= int(line[1])
        capacity = int(line[2])
        coins = sorted(list(map(int,line[3:])))
        point["Size"] = line[0]
        point["Target"] = target
        point["Capacity"] = capacity
        point["Coins"] = coins
        point["Number of Coins"] = len(coins)
        reversed_coins = list(reversed(coins))
        combination = find_combination(target,reversed_coins,capacity)
        coins=list(reversed(coins))
        if combination is None:
            point["Combination"] = "None"
        else:
            point["Combination"] = list(sorted(combination))
        end=time.time()
        elapsed=int((end-start)*1e6)
        point["Time Elapsed"] = elapsed
        data.append(point)
        iteration+=1
    return data
            
def main():
    data=sorted(get_data(), key = lambda point:(point["Target"],point["Number of Coins"],point["Time Elapsed"]))
    fieldnames = ['Size','Target', "Capacity", 'Number of Coins', 'Time Elapsed', 'Coins', 'Combination']
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
    
    
if __name__ == "__main__":
    main()