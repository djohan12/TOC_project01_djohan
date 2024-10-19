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

def main():
    failed=0
    linenum=1
    for line in sys.stdin.readlines():
        inputs=line.strip().split(':')
        target=int(inputs[0])
        print(f"Test {linenum}\t...",end='\t')
        linenum+=1
        capacity=int(inputs[1])
        coins=list(map(int,(inputs[2].split(','))))
        combination=inputs[3]
        if combination!="None":
            combination = list(map(int,(inputs[3].split(','))))
        found = find_combination(target,coins,capacity)
        if(found is None and combination=="None") or sum(found)==target:
            print("Success")
        else:
            print("Failed")
            failed+=1
    if(failed):
        print(f'{failed} tests failed')
    else:
        print("All tests passed successfully")

if __name__ == "__main__":
    main()