import argparse;
import random;
from datetime import datetime
import textwrap;

def main():
  # Handle arguments
  parser = argparse.ArgumentParser(
    prog='knapsackTestCaseGen',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='Creates a given number each of small, medium, and large test cases for the knapsack problem.',
    epilog=textwrap.dedent('''
        The range for total value, number of coins, and coin size can be configured within the code.
        The cases are in format "casetype, totalvalue, coin1value, coin2value, coin3value,...'''))
  
  parser.add_argument("--file", "-f", required=True, type=argparse.FileType('w'),
                      help="File to print test cases to (Will overwrite data).")
  parser.add_argument("--size", "-s", required=True, type=int,
                      help="Number of test cases to generate.")
  
  args = parser.parse_args()

  # If something went wrong and the file cannot be opened, exit with error
  if (not args.file):
    print("Error opening file.")
    return
  
  # Otherwise, print test cases to file

  # Set the total value range for the small, medium, and large test cases
  # Format: [[easy min val, easy max val], [med min, med max], [large min, large max]]
  testcaseTotalValueRange = [[100, 999], [1000, 9999], [10000, 30000]]
  # convert float values to ints

  
  # Set the maximum coin value for the small, medium, and large test cases
  # Default is [25, 25, 25] to make them all 25 cents, but could be changed
  testcaseMaxCoinValue = [50, 250, 500]
  
  # Set the case types and number of coins for each type
  testcaseTypes = {"Small":25, "Medium":50, "Large":75}
  testcaseCapacity = {"Small":100, "Medium":250, "Large":500}

  # Set randomization seed
  random.seed(datetime.now().timestamp())
  for testSize, vals in enumerate(testcaseTotalValueRange):
    for _testcase in range(args.size):
      Type = list(testcaseTypes.items())[testSize][0]
      args.file.write(f"{Type}")
      args.file.write(f", {random.randint(testcaseTotalValueRange[testSize][0], testcaseTotalValueRange[testSize][1])}")
      numCoins=list(testcaseTypes.items())[testSize][1]
      numCoins=random.randint(numCoins*3//5,numCoins*7//5)
      args.file.write(f", {numCoins}")
      capacity=list(testcaseCapacity.items())[testSize][1]
      args.file.write(f", {random.randint(3*capacity//5,7*capacity//5)}")
      
      
      coins = []
      while len(coins)<numCoins:
        coin=random.randint(2, testcaseMaxCoinValue[testSize])
        if coin not in coins:
          coins.append(coin)  
      coins=list(map(str,coins))
      args.file.write(f", {", ".join(coins)}")
      
      args.file.write("\n")

  # Close the file once we are done
  args.file.close()

if __name__ == '__main__':
  main()