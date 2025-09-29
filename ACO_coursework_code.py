##############
# How to run code:
# Do the three steps.
##############
# STEP 1: Change file path to where the file for the bags is stored
##############

import re
import random

# This opens the file and saves it to a variable named data
with open('/Users/lewishall/Desktop/Evo Algorithms Yr4/Knapsack problem code/BankProblemDataSet1.tex', 'r') as file:
    data = file.read()
    
##############
# STEP 2: Adjust values to what you like
##############

a = 1 # alpha value
b = 2 # beta value
rho = 0.5 # The pheremone evaporation rate

# value m determines the amount of pheromone deposited relative to the fitness of the solution.
m = 4000 

# Number of ants that find a solution, referred to as p (population) in my report.
Number_of_Ants = 50

# How many times do you want to repeat this process of running the ants through
# and calculating different solutions. This is referred to as x in my report.
# e.g. For 10,000 evaluations, using 50 ants, 10,000/50 = 200, x = 200.

Number_Of_Solution_Calculations = 200

############
# STEP 3: Run all the code, the results are printed out
############

# this takes the data from the text file and creates two lists 
# with the weight and value for each bag
# I then convert the string values in the lists to 
# floats so I can use them for calculations

weights = re.findall(r'weight:\s*([\d.]+)', data)
weights = [float(weight) for weight in weights]
values = re.findall(r'value:\s*([\d.]+)', data)
values = [float(value) for value in values]

# This uses both the lists to create a list with the value/weight
# ratio for each bag

R = [value / weight for value, weight in zip(values, weights)]
# this rounds all the values to 4 d.p
R = [round(num, 4) for num in R] 


# These are 10 the sets of heuristic matrixes, each containing the 
# vale/weight ratios of 10 of the bags. R[x] is a number in the 
# list of the ratios of the 100 bags where x is the bag number. 
# The matrixes have a line of zeros on the left as that signifies 
# the start node, so that the probability of the ant moving back to the 
# start node is always zero

H_0 = [[0, R[0], R[1], R[2], R[3], R[4], R[5], R[6], R[7], R[8], R[9]],
      [0, 0, R[1], R[2], R[3], R[4], R[5], R[6], R[7], R[8], R[9]],
      [0, R[0], 0, R[2], R[3], R[4], R[5], R[6], R[7], R[8], R[9]],
      [0, R[0], R[1], 0, R[3], R[4], R[5], R[6], R[7], R[8], R[9]],
      [0, R[0], R[1], R[2], 0, R[4], R[5], R[6], R[7], R[8], R[9]],
      [0, R[0], R[1], R[2], R[3], 0, R[5], R[6], R[7], R[8], R[9]],
      [0, R[0], R[1], R[2], R[3], R[4], 0, R[6], R[7], R[8], R[9]],
      [0, R[0], R[1], R[2], R[3], R[4], R[5], 0, R[7], R[8], R[9]],
      [0, R[0], R[1], R[2], R[3], R[4], R[5], R[6], 0, R[8], R[9]],
      [0, R[0], R[1], R[2], R[3], R[4], R[5], R[6], R[7], 0, R[9]],
      [0, R[0], R[1], R[2], R[3], R[4], R[5], R[6], R[7], R[8], 0]]

H_1 = [[0, R[10], R[11], R[12], R[13], R[14], R[15], R[16], R[17], R[18], R[19]],
       [0, 0, R[11], R[12], R[13], R[14], R[15], R[16], R[17], R[18], R[19]],
       [0, R[10], 0, R[12], R[13], R[14], R[15], R[16], R[17], R[18], R[19]],
       [0, R[10], R[11], 0, R[13], R[14], R[15], R[16], R[17], R[18], R[19]],
       [0, R[10], R[11], R[12], 0, R[14], R[15], R[16], R[17], R[18], R[19]],
       [0, R[10], R[11], R[12], R[13], 0, R[15], R[16], R[17], R[18], R[19]],
       [0, R[10], R[11], R[12], R[13], R[14], 0, R[16], R[17], R[18], R[19]],
       [0, R[10], R[11], R[12], R[13], R[14], R[15], 0, R[17], R[18], R[19]],
       [0, R[10], R[11], R[12], R[13], R[14], R[15], R[16], 0, R[18], R[19]],
       [0, R[10], R[11], R[12], R[13], R[14], R[15], R[16], R[17], 0, R[19]],
       [0, R[10], R[11], R[12], R[13], R[14], R[15], R[16], R[17], R[18], 0]]

H_2 = [[0, R[20], R[21], R[22], R[23], R[24], R[25], R[26], R[27], R[28], R[29]],
       [0, 0, R[21], R[22], R[23], R[24], R[25], R[26], R[27], R[28], R[29]],
       [0, R[20], 0, R[22], R[23], R[24], R[25], R[26], R[27], R[28], R[29]],
       [0, R[20], R[21], 0, R[23], R[24], R[25], R[26], R[27], R[28], R[29]],
       [0, R[20], R[21], R[22], 0, R[24], R[25], R[26], R[27], R[28], R[29]],
       [0, R[20], R[21], R[22], R[23], 0, R[25], R[26], R[27], R[28], R[29]],
       [0, R[20], R[21], R[22], R[23], R[24], 0, R[26], R[27], R[28], R[29]],
       [0, R[20], R[21], R[22], R[23], R[24], R[25], 0, R[27], R[28], R[29]],
       [0, R[20], R[21], R[22], R[23], R[24], R[25], R[26], 0, R[28], R[29]],
       [0, R[20], R[21], R[22], R[23], R[24], R[25], R[26], R[27], 0, R[29]],
       [0, R[20], R[21], R[22], R[23], R[24], R[25], R[26], R[27], R[28], 0]]

H_3 = [[0, R[30], R[31], R[32], R[33], R[34], R[35], R[36], R[37], R[38], R[39]],
    [0, 0, R[31], R[32], R[33], R[34], R[35], R[36], R[37], R[38], R[39]],
    [0, R[30], 0, R[32], R[33], R[34], R[35], R[36], R[37], R[38], R[39]],
    [0, R[30], R[31], 0, R[33], R[34], R[35], R[36], R[37], R[38], R[39]],
    [0, R[30], R[31], R[32], 0, R[34], R[35], R[36], R[37], R[38], R[39]],
    [0, R[30], R[31], R[32], R[33], 0, R[35], R[36], R[37], R[38], R[39]],
    [0, R[30], R[31], R[32], R[33], R[34], 0, R[36], R[37], R[38], R[39]],
    [0, R[30], R[31], R[32], R[33], R[34], R[35], 0, R[37], R[38], R[39]],
    [0, R[30], R[31], R[32], R[33], R[34], R[35], R[36], 0, R[38], R[39]],
    [0, R[30], R[31], R[32], R[33], R[34], R[35], R[36], R[37], 0, R[39]],
    [0, R[30], R[31], R[32], R[33], R[34], R[35], R[36], R[37], R[38], 0]]

H_4 = [[0, R[40], R[41], R[42], R[43], R[44], R[45], R[46], R[47], R[48], R[49]],
    [0, 0, R[41], R[42], R[43], R[44], R[45], R[46], R[47], R[48], R[49]],
    [0, R[40], 0, R[42], R[43], R[44], R[45], R[46], R[47], R[48], R[49]],
    [0, R[40], R[41], 0, R[43], R[44], R[45], R[46], R[47], R[48], R[49]],
    [0, R[40], R[41], R[42], 0, R[44], R[45], R[46], R[47], R[48], R[49]],
    [0, R[40], R[41], R[42], R[43], 0, R[45], R[46], R[47], R[48], R[49]],
    [0, R[40], R[41], R[42], R[43], R[44], 0, R[46], R[47], R[48], R[49]],
    [0, R[40], R[41], R[42], R[43], R[44], R[45], 0, R[47], R[48], R[49]],
    [0, R[40], R[41], R[42], R[43], R[44], R[45], R[46], 0, R[48], R[49]],
    [0, R[40], R[41], R[42], R[43], R[44], R[45], R[46], R[47], 0, R[49]],
    [0, R[40], R[41], R[42], R[43], R[44], R[45], R[46], R[47], R[48], 0]]

H_5 = [[0, R[50], R[51], R[52], R[53], R[54], R[55], R[56], R[57], R[58], R[59]],
    [0, 0, R[51], R[52], R[53], R[54], R[55], R[56], R[57], R[58], R[59]],
    [0, R[50], 0, R[52], R[53], R[54], R[55], R[56], R[57], R[58], R[59]],
    [0, R[50], R[51], 0, R[53], R[54], R[55], R[56], R[57], R[58], R[59]],
    [0, R[50], R[51], R[52], 0, R[54], R[55], R[56], R[57], R[58], R[59]],
    [0, R[50], R[51], R[52], R[53], 0, R[55], R[56], R[57], R[58], R[59]],
    [0, R[50], R[51], R[52], R[53], R[54], 0, R[56], R[57], R[58], R[59]],
    [0, R[50], R[51], R[52], R[53], R[54], R[55], 0, R[57], R[58], R[59]],
    [0, R[50], R[51], R[52], R[53], R[54], R[55], R[56], 0, R[58], R[59]],
    [0, R[50], R[51], R[52], R[53], R[54], R[55], R[56], R[57], 0, R[59]],
    [0, R[50], R[51], R[52], R[53], R[54], R[55], R[56], R[57], R[58], 0]]

H_6 = [[0, R[60], R[61], R[62], R[63], R[64], R[65], R[66], R[67], R[68], R[69]],
    [0, 0, R[61], R[62], R[63], R[64], R[65], R[66], R[67], R[68], R[69]],
    [0, R[60], 0, R[62], R[63], R[64], R[65], R[66], R[67], R[68], R[69]],
    [0, R[60], R[61], 0, R[63], R[64], R[65], R[66], R[67], R[68], R[69]],
    [0, R[60], R[61], R[62], 0, R[64], R[65], R[66], R[67], R[68], R[69]],
    [0, R[60], R[61], R[62], R[63], 0, R[65], R[66], R[67], R[68], R[69]],
    [0, R[60], R[61], R[62], R[63], R[64], 0, R[66], R[67], R[68], R[69]],
    [0, R[60], R[61], R[62], R[63], R[64], R[65], 0, R[67], R[68], R[69]],
    [0, R[60], R[61], R[62], R[63], R[64], R[65], R[66], 0, R[68], R[69]],
    [0, R[60], R[61], R[62], R[63], R[64], R[65], R[66], R[67], 0, R[69]],
    [0, R[60], R[61], R[62], R[63], R[64], R[65], R[66], R[67], R[68], 0]]

H_7 = [[0, R[70], R[71], R[72], R[73], R[74], R[75], R[76], R[77], R[78], R[79]],
    [0, 0, R[71], R[72], R[73], R[74], R[75], R[76], R[77], R[78], R[79]],
    [0, R[70], 0, R[72], R[73], R[74], R[75], R[76], R[77], R[78], R[79]],
    [0, R[70], R[71], 0, R[73], R[74], R[75], R[76], R[77], R[78], R[79]],
    [0, R[70], R[71], R[72], 0, R[74], R[75], R[76], R[77], R[78], R[79]],
    [0, R[70], R[71], R[72], R[73], 0, R[75], R[76], R[77], R[78], R[79]],
    [0, R[70], R[71], R[72], R[73], R[74], 0, R[76], R[77], R[78], R[79]],
    [0, R[70], R[71], R[72], R[73], R[74], R[75], 0, R[77], R[78], R[79]],
    [0, R[70], R[71], R[72], R[73], R[74], R[75], R[76], 0, R[78], R[79]],
    [0, R[70], R[71], R[72], R[73], R[74], R[75], R[76], R[77], 0, R[79]],
    [0, R[70], R[71], R[72], R[73], R[74], R[75], R[76], R[77], R[78], 0]]

H_8 = [[0, R[80], R[81], R[82], R[83], R[84], R[85], R[86], R[87], R[88], R[89]],
    [0, 0, R[81], R[82], R[83], R[84], R[85], R[86], R[87], R[88], R[89]],
    [0, R[80], 0, R[82], R[83], R[84], R[85], R[86], R[87], R[88], R[89]],
    [0, R[80], R[81], 0, R[83], R[84], R[85], R[86], R[87], R[88], R[89]],
    [0, R[80], R[81], R[82], 0, R[84], R[85], R[86], R[87], R[88], R[89]],
    [0, R[80], R[81], R[82], R[83], 0, R[85], R[86], R[87], R[88], R[89]],
    [0, R[80], R[81], R[82], R[83], R[84], 0, R[86], R[87], R[88], R[89]],
    [0, R[80], R[81], R[82], R[83], R[84], R[85], 0, R[87], R[88], R[89]],
    [0, R[80], R[81], R[82], R[83], R[84], R[85], R[86], 0, R[88], R[89]],
    [0, R[80], R[81], R[82], R[83], R[84], R[85], R[86], R[87], 0, R[89]],
    [0, R[80], R[81], R[82], R[83], R[84], R[85], R[86], R[87], R[88], 0]]

H_9 = [[0, R[90], R[91], R[92], R[93], R[94], R[95], R[96], R[97], R[98], R[99]],
    [0, 0, R[91], R[92], R[93], R[94], R[95], R[96], R[97], R[98], R[99]],
    [0, R[90], 0, R[92], R[93], R[94], R[95], R[96], R[97], R[98], R[99]],
    [0, R[90], R[91], 0, R[93], R[94], R[95], R[96], R[97], R[98], R[99]],
    [0, R[90], R[91], R[92], 0, R[94], R[95], R[96], R[97], R[98], R[99]],
    [0, R[90], R[91], R[92], R[93], 0, R[95], R[96], R[97], R[98], R[99]],
    [0, R[90], R[91], R[92], R[93], R[94], 0, R[96], R[97], R[98], R[99]],
    [0, R[90], R[91], R[92], R[93], R[94], R[95], 0, R[97], R[98], R[99]],
    [0, R[90], R[91], R[92], R[93], R[94], R[95], R[96], 0, R[98], R[99]],
    [0, R[90], R[91], R[92], R[93], R[94], R[95], R[96], R[97], 0, R[99]],
    [0, R[90], R[91], R[92], R[93], R[94], R[95], R[96], R[97], R[98], 0]]

# These are the pheremone matrixes T, for all the different heuristic matrixes
# all values are initialised as a random number between 0 and 1. The range is 
# 11 since there are 10 bags and the start node.

T_0 = [[ random.random() for j in range(11)] for i in range(11)]
T_1 = [[ random.random() for j in range(11)] for i in range(11)]
T_2 = [[ random.random() for j in range(11)] for i in range(11)]
T_3 = [[ random.random() for j in range(11)] for i in range(11)]
T_4 = [[ random.random() for j in range(11)] for i in range(11)]
T_5 = [[ random.random() for j in range(11)] for i in range(11)]
T_6 = [[ random.random() for j in range(11)] for i in range(11)]
T_7 = [[ random.random() for j in range(11)] for i in range(11)]
T_8 = [[ random.random() for j in range(11)] for i in range(11)]
T_9 = [[ random.random() for j in range(11)] for i in range(11)]

# List containing all the pheremone matrixes
T_All = [T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9]

# This is a list of the 10 sets of heuristic matrixes
All_Sets_Of_Bags = [H_0, H_1, H_2, H_3, H_4, H_5, H_6, H_7, H_8, H_9]
# Initialising the weight in the van as zero before the code is run.
Current_Van_Weight = 0


# Function to update the pheremones matrixes
def Update_Pheremones(Bag_1, Bag_2, Bag_3, Bag_4, Bag_5, Bag_6, Bag_7, T, Total_Value_In_Van):
    Tx = T
    
    # Amount of pheremone added, deltal1, is the total value that 
    # the ant managed to get in the van, divided by m, the variable
    # we change in the experiment
    delta1 = Total_Value_In_Van/m
    
    # The function called ant collect 7 bags always checks if the weight of the 
    # van is at its max before adding a new bag to the list of bags, if the van 
    # cannot fit another bag and the function has only selected Bag_1,2,3 then 
    # the varibles named Bag_4,5,6,7 will be given the result -1. This function 
    # checks to see if the variable is not -1 before updating the path between 
    # the two bags that the ant visited.
    if Bag_1 > 0: Tx[0][Bag_1] += delta1 
    if Bag_2 > 0: Tx[Bag_1][Bag_2] += delta1 
    if Bag_3 > 0: Tx[Bag_2][Bag_3] += delta1 
    if Bag_4 > 0: Tx[Bag_3][Bag_4] += delta1 
    if Bag_5 > 0: Tx[Bag_4][Bag_5] += delta1
    if Bag_6 > 0: Tx[Bag_5][Bag_6] += delta1 
    if Bag_7 > 0: Tx[Bag_6][Bag_7] += delta1
        
    # This evaporates the pheremones in the matrix by multiplying all the 
    # pheremone values in the matrix by (1-rho).
    Tx = [[ (1-rho)*T[i][j] for j in range(11)] for i in range(11)]
    
    return Tx

    # this function is called if the ant has already collected 7 bags from each set
    # of 10 bags, if this is the case and the ant collects another bag from a set of bags 
    # then you do not want to evaporate the matrix of pheremones from that bag a 
    # second time, you just want to deposit pheremone where the ant went to next.
    # hence why this function is the same as the last one but without the pheremone 
    # evaporation equation.
    
def Update_Pheremones_V2(Bag_1, Bag_2, Bag_3, Bag_4, Bag_5, Bag_6, Bag_7, T, Total_Value_In_Van):
    Tx = T
    
    delta1 = Total_Value_In_Van/m
    
    if Bag_1 > 0: Tx[0][Bag_1] += delta1 
    if Bag_2 > 0: Tx[Bag_1][Bag_2] += delta1 
    if Bag_3 > 0: Tx[Bag_2][Bag_3] += delta1 
    if Bag_4 > 0: Tx[Bag_3][Bag_4] += delta1
    if Bag_5 > 0: Tx[Bag_4][Bag_5] += delta1
    if Bag_6 > 0: Tx[Bag_5][Bag_6] += delta1 
    if Bag_7 > 0: Tx[Bag_6][Bag_7] += delta1 
        
    return Tx


# This function takes the current bag the ant is on and calculates 
# what bag to choose next

def Find_Next_Bag(Current_Node, H, T):
    
    # Probability of a ant moving to a bag, pheremone value 
    # between the two bags multiplied by the heuristic value 
    N0 = T[Current_Node][0]**a * H[Current_Node][0]**b
    N1 = T[Current_Node][1]**a * H[Current_Node][1]**b
    N2 = T[Current_Node][2]**a * H[Current_Node][2]**b
    N3 = T[Current_Node][3]**a * H[Current_Node][3]**b
    N4 = T[Current_Node][4]**a * H[Current_Node][4]**b
    N5 = T[Current_Node][5]**a * H[Current_Node][5]**b
    N6 = T[Current_Node][6]**a * H[Current_Node][6]**b
    N7 = T[Current_Node][7]**a * H[Current_Node][7]**b
    N8 = T[Current_Node][8]**a * H[Current_Node][8]**b
    N9 = T[Current_Node][9]**a * H[Current_Node][9]**b
    N10 = T[Current_Node][10]**a * H[Current_Node][10]**b
    
    Sum_N = N0+N1+N2+N3+N4+N5+N6+N7+N8+N9+N10
    
    # Probability of a ant moving to a bag, pheremone value 
    # between the two bags multiplied by the heuristic value, 
    # divided by the sum of that but for every possible bag 
    # the ant could move to
    P0 = N0/Sum_N
    P1 = N1/Sum_N
    P2 = N2/Sum_N
    P3 = N3/Sum_N
    P4 = N4/Sum_N
    P5 = N5/Sum_N
    P6 = N6/Sum_N
    P7 = N7/Sum_N
    P8 = N8/Sum_N
    P9 = N9/Sum_N
    P10 = N10/Sum_N

    # cumulative probability, allows you to use a random number between
    # 0 and 1 to decide which bag to move to.
    Cp0 = P0
    Cp1 = Cp0 + P1
    Cp2 = Cp1 + P2
    Cp3 = Cp2 + P3
    Cp4 = Cp3 + P4
    Cp5 = Cp4 + P5
    Cp6 = Cp5 + P6
    Cp7 = Cp6 + P7
    Cp8 = Cp7 + P8
    Cp9 = Cp8 + P9
    Cp10 = Cp9 + P10
    
    # Node List, Probability list, Cumulative probability list
    N_L = [N0, N1, N2, N3, N4, N5, N6, N7, N8, N9, N10]
    P_L = [P0, P1, P2, P3, P4, P5, P6, P7, P8, P9, P10]
    Cp_L = [Cp0, Cp1, Cp2, Cp3, Cp4, Cp5, Cp6, Cp7, Cp8, Cp9, Cp10]
    
    # same lists but rounded, these were used to print out to check the
    # function was working properly
    N_L_rounded = [round(num, 2) for num in N_L] 
    P_L_rounded = [round(num, 2) for num in P_L]
    Cp_L_rounded = [round(num, 2) for num in Cp_L]

    # Generate a random number between 0 and 1
    random_number = random.random()

    # Find the first Cp value greater than the random number
    for i, value in enumerate(Cp_L):

        if value > random_number:
            # returns the number i to indicate which bag the ant
            # chose to move to
            return i

    return None


# Function for the ant to collect 7 bags from a batch of 10 bags
def Ant_collect_7_bags(Current_Node, Chosen_Batch_of_10_bags, Current_Van_Weight, Current_Van_Value, x, T, Second_Cycle_Of_Bag_Collecting):
    Van_Full = False
    H = Chosen_Batch_of_10_bags
    
    # Calls the functio to find the first bag
    Bag_1 = Find_Next_Bag(0, H, T) 
   
    # Updated the van's total weight and amount of money in the van
    Bag_1_Weight = weights[Bag_1 -1 + x]
    Current_Van_Weight = Current_Van_Weight + Bag_1_Weight
    
    Bag_1_Value = values[Bag_1 -1 + x]
    Current_Van_Value = Current_Van_Value + Bag_1_Value
    
    # If the weight in the van exceeds the vans total weight limit then
    # remove the weight and money from the last bag, remove the 
    # weight and money from the preious bag, and only return the bag numbers 
    # out of the 7 bags that were selected, for the bags that were not selected
    # return their value as -1 to indicate this. In this part, all of the seven 
    # are returned as -1.
    if Current_Van_Weight > 295:
        # this lets us know outside this function that the van is full 
        Van_Full = True
        Current_Van_Weight = Current_Van_Weight - Bag_1_Weight
        Current_Van_Value = Current_Van_Value - Bag_1_Value
        return Current_Van_Weight, Current_Van_Value, -1, -1, -1, -1, -1, -1, -1, H, Van_Full

    # This takes the number from the node that the ant arrived at and 
    # then makes that whole column 0 so that the probability of an ant 
    # arriving there again is 0, this means the ant cannot choose the same bag twice
    H = [[ H[i][j] if i != j and j != 0 and j != Bag_1 else 0 for j in range(11)] for i in range(11)]
    
    # If the ant has taken 7 bags from every set of bags and is now collecting 
    # one more bag from each set of bags then the variable named
    # second cycle of bag collecting is set as true, and so the ant only takes one 
    # more bag from this set of bags
    if Second_Cycle_Of_Bag_Collecting == True:
        return Current_Van_Weight, Current_Van_Value, Bag_1, -1, -1, -1, -1, -1, -1, H, Van_Full
    
    Bag_2 = Find_Next_Bag(Bag_1, H, T)
    
    
    Bag_2_Weight = weights[Bag_2 -1 + x]
    Current_Van_Weight = Current_Van_Weight + Bag_2_Weight
    
    Bag_2_Value = values[Bag_2 -1 + x]
    Current_Van_Value = Current_Van_Value + Bag_2_Value
    

    if Current_Van_Weight > 295:
        Van_Full = True
        Current_Van_Weight = Current_Van_Weight - Bag_2_Weight
        Current_Van_Value = Current_Van_Value - Bag_2_Value
        return Current_Van_Weight, Current_Van_Value, Bag_1, -1, -1, -1, -1, -1, -1, H, Van_Full

    H = [[ H[i][j] if i != j and j != 0 and j != Bag_2 else 0 for j in range(11)] for i in range(11)]


    Bag_3 = Find_Next_Bag(Bag_2, H, T)
    
    Bag_3_Weight = weights[Bag_3 -1 + x]
    Current_Van_Weight = Current_Van_Weight + Bag_3_Weight
    
    Bag_3_Value = values[Bag_3 -1 + x]
    Current_Van_Value = Current_Van_Value + Bag_3_Value
    

    if Current_Van_Weight > 295:
        Van_Full = True
        Current_Van_Weight = Current_Van_Weight - Bag_3_Weight
        Current_Van_Value = Current_Van_Value - Bag_3_Value
        return Current_Van_Weight, Current_Van_Value, Bag_1, Bag_2, -1, -1, -1, -1, -1, H, Van_Full

    H = [[ H[i][j] if i != j and j != 0 and j != Bag_3 else 0 for j in range(11)] for i in range(11)]



    Bag_4 = Find_Next_Bag(Bag_3, H, T)
    
    
    Bag_4_Weight = weights[Bag_4 -1 + x]
    Current_Van_Weight = Current_Van_Weight + Bag_4_Weight
    
    Bag_4_Value = values[Bag_4 -1 + x]
    Current_Van_Value = Current_Van_Value + Bag_4_Value
    

    if Current_Van_Weight > 295:
        Van_Full = True
        Current_Van_Weight = Current_Van_Weight - Bag_4_Weight
        Current_Van_Value = Current_Van_Value - Bag_4_Value
        return Current_Van_Weight, Current_Van_Value, Bag_1, Bag_2, Bag_3, -1, -1, -1, -1, H, Van_Full 

    H = [[ H[i][j] if i != j and j != 0 and j != Bag_4 else 0 for j in range(11)] for i in range(11)]
    
    
    
    Bag_5 = Find_Next_Bag(Bag_4, H, T)
    
    
    Bag_5_Weight = weights[Bag_5 -1 + x]
    Current_Van_Weight = Current_Van_Weight + Bag_5_Weight
    
    Bag_5_Value = values[Bag_5 -1 + x]
    Current_Van_Value = Current_Van_Value + Bag_5_Value
    
   
    
    if Current_Van_Weight > 295:
        Van_Full = True
        Current_Van_Weight = Current_Van_Weight - Bag_5_Weight
        Current_Van_Value = Current_Van_Value - Bag_5_Value
        return Current_Van_Weight, Current_Van_Value, Bag_1, Bag_2, Bag_3, Bag_4, -1, -1, -1, H, Van_Full

    H = [[ H[i][j] if i != j and j != 0 and j != Bag_5 else 0 for j in range(11)] for i in range(11)]
    
    
    Bag_6 = Find_Next_Bag(Bag_5, H, T)
    
    
    Bag_6_Weight = weights[Bag_6 -1 + x]
    Current_Van_Weight = Current_Van_Weight + Bag_6_Weight
    
    Bag_6_Value = values[Bag_6 -1 + x]
    Current_Van_Value = Current_Van_Value + Bag_6_Value
    
    
    if Current_Van_Weight > 295:
        Van_Full = True
        Current_Van_Weight = Current_Van_Weight - Bag_6_Weight
        Current_Van_Value = Current_Van_Value - Bag_6_Value
        return Current_Van_Weight, Current_Van_Value, Bag_1, Bag_2, Bag_3, Bag_4, Bag_5, -1, -1, H, Van_Full 

    H = [[ H[i][j] if i != j and j != 0 and j != Bag_6 else 0 for j in range(11)] for i in range(11)]
    
    Bag_7 = Find_Next_Bag(Bag_6, H, T)
    
    
    Bag_7_Weight = weights[Bag_7 -1 + x]
    Current_Van_Weight = Current_Van_Weight + Bag_7_Weight
    
    Bag_7_Value = values[Bag_7 -1 + x]
    Current_Van_Value = Current_Van_Value + Bag_7_Value
    
    
    if Current_Van_Weight > 295:
        Van_Full = True
        Current_Van_Weight = Current_Van_Weight - Bag_7_Weight
        Current_Van_Value = Current_Van_Value - Bag_7_Value
        return Current_Van_Weight, Current_Van_Value, Bag_1, Bag_2, Bag_3, Bag_4, Bag_5, Bag_6, -1, H, Van_Full 

    H = [[ H[i][j] if i != j and j != 0 and j != Bag_7 else 0 for j in range(11)] for i in range(11)]

    return Current_Van_Weight, Current_Van_Value, Bag_1, Bag_2, Bag_3, Bag_4, Bag_5, Bag_6, Bag_7, H, Van_Full



# Function to make an ant fill the van with bags and thereby create a solution
# Take the heuristic and pheremone matrixes as input arguments

def Ant_fill_van(All_Sets_Of_Bags, T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9):
    Van_Full = False
    Current_Van_Weight = 0
    Current_Van_Value = 0 
    All_Sets_Of_Bags = [H_0, H_1, H_2, H_3, H_4, H_5, H_6, H_7, H_8, H_9]
    Second_Cycle_Of_Bag_Collecting = False
    
    # Define a function that can be called to update all the necessary pheremones
    def Complete_Pheremone_Update(T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9):
        T_0 = Update_Pheremones(Bag_0_1, Bag_0_2, Bag_0_3, Bag_0_4, Bag_0_5, Bag_0_6, Bag_0_7, T_0, Current_Van_Value)
        T_1 = Update_Pheremones(Bag_1_1, Bag_1_2, Bag_1_3, Bag_1_4, Bag_1_5, Bag_1_6, Bag_1_7, T_1, Current_Van_Value)
        T_2 = Update_Pheremones(Bag_2_1, Bag_2_2, Bag_2_3, Bag_2_4, Bag_2_5, Bag_2_6, Bag_2_7, T_2, Current_Van_Value)
        T_3 = Update_Pheremones(Bag_3_1, Bag_3_2, Bag_3_3, Bag_3_4, Bag_3_5, Bag_3_6, Bag_3_7, T_3, Current_Van_Value)
        T_4 = Update_Pheremones(Bag_4_1, Bag_4_2, Bag_4_3, Bag_4_4, Bag_4_5, Bag_4_6, Bag_4_7, T_4, Current_Van_Value)
        T_5 = Update_Pheremones(Bag_5_1, Bag_5_2, Bag_5_3, Bag_5_4, Bag_5_5, Bag_5_6, Bag_5_7, T_5, Current_Van_Value)
        T_6 = Update_Pheremones(Bag_6_1, Bag_6_2, Bag_6_3, Bag_6_4, Bag_6_5, Bag_6_6, Bag_6_7, T_6, Current_Van_Value)
        T_7 = Update_Pheremones(Bag_7_1, Bag_7_2, Bag_7_3, Bag_7_4, Bag_7_5, Bag_7_6, Bag_7_7, T_7, Current_Van_Value)
        
        # Run the following code if the arguments being put into the function have a vale
        # They will not have a value if the van was too heavy and could not get more bags
        # in the van without exceeding the weight limit
        try: 
            T_8 = Update_Pheremones(Bag_8_1, Bag_8_2, Bag_8_3, Bag_8_4, Bag_8_5, Bag_8_6, Bag_8_7, T_8, Current_Van_Value)
        except NameError:
            pass
        try: 
            T_9 = Update_Pheremones(Bag_9_1, Bag_9_2, Bag_9_3, Bag_9_4, Bag_9_5, Bag_9_6, Bag_9_7, T_9, Current_Van_Value)
        except NameError:
            pass
        try: 
            T_0 = Update_Pheremones_V2(Bag_2_0_1, Bag_2_0_2, Bag_2_0_3, Bag_2_0_4, Bag_2_0_5, Bag_2_0_6, Bag_2_0_7, T_0, Current_Van_Value)
        except NameError:
            pass
        try: 
            T_1 = Update_Pheremones_V2(Bag_2_1_1, Bag_2_1_2, Bag_2_1_3, Bag_2_1_4, Bag_2_1_5, Bag_2_1_6, Bag_2_1_7, T_1, Current_Van_Value)
        except NameError:
            pass
        try: 
            T_2 = Update_Pheremones_V2(Bag_2_2_1, Bag_2_2_2, Bag_2_2_3, Bag_2_2_4, Bag_2_2_5, Bag_2_2_6, Bag_2_2_7, T_2, Current_Van_Value)
        except NameError:
            pass
        try: 
            T_3 = Update_Pheremones_V2(Bag_2_3_1, Bag_2_3_2, Bag_2_3_3, Bag_2_3_4, Bag_2_3_5, Bag_2_3_6, Bag_2_3_7, T_3, Current_Van_Value)
        except NameError:
            pass
        try: 
            T_4 = Update_Pheremones_V2(Bag_2_4_1, Bag_2_4_2, Bag_2_4_3, Bag_2_4_4, Bag_2_4_5, Bag_2_4_6, Bag_2_4_7, T_4, Current_Van_Value)
        except NameError:
            pass
        try: 
            T_5 = Update_Pheremones_V2(Bag_2_5_1, Bag_2_5_2, Bag_2_5_3, Bag_2_5_4, Bag_2_5_5, Bag_2_5_6, Bag_2_5_7, T_5, Current_Van_Value)
        except NameError:
            pass
        try: 
            T_6 = Update_Pheremones_V2(Bag_2_6_1, Bag_2_6_2, Bag_2_6_3, Bag_2_6_4, Bag_2_6_5, Bag_2_6_6, Bag_2_6_7, T_6, Current_Van_Value)
        except NameError:
            pass
        try: 
            T_7 = Update_Pheremones_V2(Bag_2_7_1, Bag_2_7_2, Bag_2_7_3, Bag_2_7_4, Bag_2_7_5, Bag_2_7_6, Bag_2_7_7, T_7, Current_Van_Value)
        except NameError:
            pass
        try: 
            T_8 = Update_Pheremones_V2(Bag_2_8_1, Bag_2_8_2, Bag_2_8_3, Bag_2_8_4, Bag_2_8_5, Bag_2_8_6, Bag_2_8_7, T_8, Current_Van_Value)
        except NameError:
            pass
        try: 
            T_9 = Update_Pheremones_V2(Bag_2_9_1, Bag_2_9_2, Bag_2_9_3, Bag_2_9_4, Bag_2_9_5, Bag_2_9_6, Bag_2_9_7, T_9, Current_Van_Value)
        except NameError:
            pass
        return T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9

    
    # When we call the function we have it return the new heuristic matrix that 
    # has seven of the bags in that batch of 10 set as 0 as they've been put in the 
    # van, we save the new matrix as Hx_0 so it doesn't permanently set the values
    # in the heuristic matrix as zero, so when the next ant uses the heuristic matrix
    # it isn't filled with 0 values
    Current_Van_Weight, Current_Van_Value, Bag_0_1, Bag_0_2, Bag_0_3, Bag_0_4, Bag_0_5, Bag_0_6, Bag_0_7, Hx_0, Van_Full = Ant_collect_7_bags(0, H_0, Current_Van_Weight, Current_Van_Value, 0, T_0, Second_Cycle_Of_Bag_Collecting)
    
    Current_Van_Weight, Current_Van_Value, Bag_1_1, Bag_1_2, Bag_1_3, Bag_1_4, Bag_1_5, Bag_1_6, Bag_1_7, Hx_1, Van_Full = Ant_collect_7_bags(0, H_1, Current_Van_Weight, Current_Van_Value, 10, T_1, Second_Cycle_Of_Bag_Collecting)
   
    Current_Van_Weight, Current_Van_Value, Bag_2_1, Bag_2_2, Bag_2_3, Bag_2_4, Bag_2_5, Bag_2_6, Bag_2_7, Hx_2, Van_Full = Ant_collect_7_bags(0, H_2, Current_Van_Weight, Current_Van_Value, 20, T_2, Second_Cycle_Of_Bag_Collecting)
    
    Current_Van_Weight, Current_Van_Value, Bag_3_1, Bag_3_2, Bag_3_3, Bag_3_4, Bag_3_5, Bag_3_6, Bag_3_7, Hx_3, Van_Full = Ant_collect_7_bags(0, H_3, Current_Van_Weight, Current_Van_Value, 30, T_3, Second_Cycle_Of_Bag_Collecting)
    
    Current_Van_Weight, Current_Van_Value, Bag_4_1, Bag_4_2, Bag_4_3, Bag_4_4, Bag_4_5, Bag_4_6, Bag_4_7, Hx_4, Van_Full = Ant_collect_7_bags(0, H_4, Current_Van_Weight, Current_Van_Value, 40, T_4, Second_Cycle_Of_Bag_Collecting)
    
    Current_Van_Weight, Current_Van_Value, Bag_5_1, Bag_5_2, Bag_5_3, Bag_5_4, Bag_5_5, Bag_5_6, Bag_5_7, Hx_5, Van_Full = Ant_collect_7_bags(0, H_5, Current_Van_Weight, Current_Van_Value, 50, T_5, Second_Cycle_Of_Bag_Collecting)

    Current_Van_Weight, Current_Van_Value, Bag_6_1, Bag_6_2, Bag_6_3, Bag_6_4, Bag_6_5, Bag_6_6, Bag_6_7, Hx_6, Van_Full = Ant_collect_7_bags(0, H_6, Current_Van_Weight, Current_Van_Value, 60, T_6, Second_Cycle_Of_Bag_Collecting)
        
    Current_Van_Weight, Current_Van_Value, Bag_7_1, Bag_7_2, Bag_7_3, Bag_7_4, Bag_7_5, Bag_7_6, Bag_7_7, Hx_7, Van_Full = Ant_collect_7_bags(0, H_7, Current_Van_Weight, Current_Van_Value, 70, T_7, Second_Cycle_Of_Bag_Collecting)

    # The bag numbers are all 1-10 so for the second and third sets of the bags 
    # I add 10, and 20 to the bag number so that the bag numbers are between 1-100
    Ordered_List_of_Bags_In_Van = [Bag_0_1, Bag_0_2, Bag_0_3, Bag_0_4, Bag_0_5, Bag_0_6, Bag_0_7,
                                   Bag_1_1+10, Bag_1_2+10, Bag_1_3+10, Bag_1_4+10, Bag_1_5+10, Bag_1_6+10, Bag_1_7+10,  
                                   Bag_2_1+20, Bag_2_2+20, Bag_2_3+20, Bag_2_4+20, Bag_2_5+20, Bag_2_6+20, Bag_2_7+20, 
                                   Bag_3_1+30, Bag_3_2+30, Bag_3_3+30, Bag_3_4+30, Bag_3_5+30, Bag_3_6+30, Bag_3_7+30,
                                   Bag_4_1+40, Bag_4_2+40, Bag_4_3+40, Bag_4_4+40, Bag_4_5+40, Bag_4_6+40, Bag_4_7+40,
                                   Bag_5_1+50, Bag_5_2+50, Bag_5_3+50, Bag_5_4+50, Bag_5_5+50, Bag_5_6+50, Bag_5_7+50,
                                   Bag_6_1+60, Bag_6_2+60, Bag_6_3+60, Bag_6_4+60, Bag_6_5+60, Bag_6_6+60, Bag_6_7+60,
                                   Bag_7_1+70, Bag_7_2+70, Bag_7_3+70, Bag_7_4+70, Bag_7_5+70, Bag_7_6+70, Bag_7_7+70,]


    Current_Van_Weight, Current_Van_Value, Bag_8_1, Bag_8_2, Bag_8_3, Bag_8_4, Bag_8_5, Bag_8_6, Bag_8_7, Hx_8, Van_Full = Ant_collect_7_bags(0, H_8, Current_Van_Weight, Current_Van_Value, 80, T_8, Second_Cycle_Of_Bag_Collecting)
    
    # if the van exceeded the weight limit during the function that selects 7 bags
    # then the variables that are returned that don't contain a bag value
    # have been put as -1. This sorts through them so they're only added to the list 
    # of bags in the van if they aren't given the value -1
    if Bag_8_1 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_8_1+80]) 
    if Bag_8_2 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_8_2+80])
    if Bag_8_3 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_8_3+80])
    if Bag_8_4 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_8_4+80])
    if Bag_8_5 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_8_5+80])
    if Bag_8_6 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_8_6+80])
    if Bag_8_7 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_8_7+80]) 
     
    # If van exceeds weight limit, update pheremones and end the ants journey
    if Van_Full == True:
        T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9 = Complete_Pheremone_Update(T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9)
        return Ordered_List_of_Bags_In_Van, Current_Van_Weight, Current_Van_Value, T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9

    Current_Van_Weight, Current_Van_Value, Bag_9_1, Bag_9_2, Bag_9_3, Bag_9_4, Bag_9_5, Bag_9_6, Bag_9_7, Hx_9, Van_Full = Ant_collect_7_bags(0, H_9, Current_Van_Weight, Current_Van_Value, 90, T_9, Second_Cycle_Of_Bag_Collecting)
    
    if Bag_9_1 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_9_1+90]) 
    if Bag_9_2 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_9_2+90])
    if Bag_9_3 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_9_3+90])
    if Bag_9_4 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_9_4+90])
    if Bag_9_5 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_9_5+90]) 
    if Bag_9_6 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_9_6+90]) 
    if Bag_9_7 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_9_7+90])
    
    if Van_Full == True:
        T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9 = Complete_Pheremone_Update(T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9)
        return Ordered_List_of_Bags_In_Van, Current_Van_Weight, Current_Van_Value, T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9
    
    
    # Now we have 6 bags from each set of 10 bags, we will collect 1 more bag from each set 
    # of 10 bags until the van is full, setting the variable Second_Cycle_Of_Bag_Collecting
    # to true tells our bag collecting function to only collect one bag
    Second_Cycle_Of_Bag_Collecting = True
   
    Current_Van_Weight, Current_Van_Value, Bag_2_0_1, Bag_2_0_2, Bag_2_0_3, Bag_2_0_4, Bag_2_0_5, Bag_2_0_6, Bag_2_0_7, Hxx_0, Van_Full = Ant_collect_7_bags(0, Hx_0, Current_Van_Weight, Current_Van_Value, 0, T_0, Second_Cycle_Of_Bag_Collecting)
    
    if Bag_2_0_1 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_2_0_1])
    
    if Van_Full == True:
        T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9 = Complete_Pheremone_Update(T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9)
        return Ordered_List_of_Bags_In_Van, Current_Van_Weight, Current_Van_Value, T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9
    
    
    Current_Van_Weight, Current_Van_Value, Bag_2_1_1, Bag_2_1_2, Bag_2_1_3, Bag_2_1_4, Bag_2_1_5, Bag_2_1_6, Bag_2_1_7, Hxx_1, Van_Full = Ant_collect_7_bags(0, Hx_1, Current_Van_Weight, Current_Van_Value, 0, T_1, Second_Cycle_Of_Bag_Collecting)
    
    if Bag_2_1_1 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_2_1_1+10])
    
    if Van_Full == True:
        T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9 = Complete_Pheremone_Update(T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9)
        return Ordered_List_of_Bags_In_Van, Current_Van_Weight, Current_Van_Value, T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9
    
    
    Current_Van_Weight, Current_Van_Value, Bag_2_2_1, Bag_2_2_2, Bag_2_2_3, Bag_2_2_4, Bag_2_2_5, Bag_2_2_6, Bag_2_2_7, Hxx_2, Van_Full = Ant_collect_7_bags(0, Hx_2, Current_Van_Weight, Current_Van_Value, 0, T_2, Second_Cycle_Of_Bag_Collecting)
    
    if Bag_2_2_1 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_2_2_1+20])
    
    if Van_Full == True:
        T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9 = Complete_Pheremone_Update(T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9)
        return Ordered_List_of_Bags_In_Van, Current_Van_Weight, Current_Van_Value, T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9
    
    
    Current_Van_Weight, Current_Van_Value, Bag_2_3_1, Bag_2_3_2, Bag_2_3_3, Bag_2_3_4, Bag_2_3_5, Bag_2_3_6, Bag_2_3_7, Hxx_3, Van_Full = Ant_collect_7_bags(0, Hx_3, Current_Van_Weight, Current_Van_Value, 0, T_3, Second_Cycle_Of_Bag_Collecting)
    
    if Bag_2_3_1 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_2_3_1+30])
   
    
    if Van_Full == True:
        T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9 = Complete_Pheremone_Update(T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9)
        return Ordered_List_of_Bags_In_Van, Current_Van_Weight, Current_Van_Value, T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9
    
    
    Current_Van_Weight, Current_Van_Value, Bag_2_4_1, Bag_2_4_2, Bag_2_4_3, Bag_2_4_4, Bag_2_4_5, Bag_2_4_6, Bag_2_4_7, Hxx_4, Van_Full = Ant_collect_7_bags(0, Hx_4, Current_Van_Weight, Current_Van_Value, 0, T_4, Second_Cycle_Of_Bag_Collecting)
    
    if Bag_2_4_1 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_2_4_1+40])
   
    
    if Van_Full == True:
        T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9 = Complete_Pheremone_Update(T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9)
        return Ordered_List_of_Bags_In_Van, Current_Van_Weight, Current_Van_Value, T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9
    
 
    Current_Van_Weight, Current_Van_Value, Bag_2_5_1, Bag_2_5_2, Bag_2_5_3, Bag_2_5_4, Bag_2_5_5, Bag_2_5_6, Bag_2_5_7, Hxx_5, Van_Full = Ant_collect_7_bags(0, Hx_5, Current_Van_Weight, Current_Van_Value, 0, T_5, Second_Cycle_Of_Bag_Collecting)
    
    if Bag_2_5_1 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_2_5_1+50])
   
    
    if Van_Full == True:
        T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9 = Complete_Pheremone_Update(T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9)
        return Ordered_List_of_Bags_In_Van, Current_Van_Weight, Current_Van_Value, T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9
 

    Current_Van_Weight, Current_Van_Value, Bag_2_6_1, Bag_2_6_2, Bag_2_6_3, Bag_2_6_4, Bag_2_6_5, Bag_2_6_6, Bag_2_6_7, Hxx_6, Van_Full = Ant_collect_7_bags(0, Hx_6, Current_Van_Weight, Current_Van_Value, 0, T_6, Second_Cycle_Of_Bag_Collecting)
    
    if Bag_2_6_1 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_2_6_1+60])
   
    
    if Van_Full == True:
        T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9 = Complete_Pheremone_Update(T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9)
        return Ordered_List_of_Bags_In_Van, Current_Van_Weight, Current_Van_Value, T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9
    
    
    Current_Van_Weight, Current_Van_Value, Bag_2_7_1, Bag_2_7_2, Bag_2_7_3, Bag_2_7_4, Bag_2_7_5, Bag_2_7_6, Bag_2_7_7, Hxx_7, Van_Full = Ant_collect_7_bags(0, Hx_7, Current_Van_Weight, Current_Van_Value, 0, T_7, Second_Cycle_Of_Bag_Collecting)
    
    if Bag_2_7_1 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_2_7_1+70])
   
    
    if Van_Full == True:
        T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9 = Complete_Pheremone_Update(T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9)
        return Ordered_List_of_Bags_In_Van, Current_Van_Weight, Current_Van_Value, T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9
    

    Current_Van_Weight, Current_Van_Value, Bag_2_8_1, Bag_2_8_2, Bag_2_8_3, Bag_2_8_4, Bag_2_8_5, Bag_2_8_6, Bag_2_8_7, Hxx_8, Van_Full = Ant_collect_7_bags(0, Hx_8, Current_Van_Weight, Current_Van_Value, 0, T_8, Second_Cycle_Of_Bag_Collecting)
    
    if Bag_2_8_1 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_2_8_1+80])
   
    
    if Van_Full == True:
        T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9 = Complete_Pheremone_Update(T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9)
        return Ordered_List_of_Bags_In_Van, Current_Van_Weight, Current_Van_Value, T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9
    
    Current_Van_Weight, Current_Van_Value, Bag_2_9_1, Bag_2_9_2, Bag_2_9_3, Bag_2_9_4, Bag_2_9_5, Bag_2_9_6, Bag_2_9_7, Hxx_9, Van_Full = Ant_collect_7_bags(0, Hx_9, Current_Van_Weight, Current_Van_Value, 0, T_9, Second_Cycle_Of_Bag_Collecting)
    
    if Bag_2_9_1 > 0: Ordered_List_of_Bags_In_Van.extend([Bag_2_9_1+90])
   
    
    if Van_Full == True:
        T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9 = Complete_Pheremone_Update(T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9)
        return Ordered_List_of_Bags_In_Van, Current_Van_Weight, Current_Van_Value, T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9
    
    
    All_Sets_Of_Bags = [H_0, H_1, H_2, H_3, H_4, H_5, H_6, H_7, H_8, H_9]
    Hx = All_Sets_Of_Bags
    
    # If the van is not full then it prints a message so I that I should 
    # change the code to allow the ant to make the van as close to its
    # max weight as possible
    if Van_Full == False:
        
        print("XXXXXXXXX     VAN NOT FULL     XXXXXXXXX")
    
    return Ordered_List_of_Bags_In_Van, Current_Van_Weight, Current_Van_Value, T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9



# Function to send multiple ants through to fill the van

def Create_Multiple_Ant_Solutions(Number_of_Ants, All_Sets_Of_Bags, T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9):
    # Creating two empty lists containing the results and list
    # of lists of bags chosen
    All_solution_Values = [0] * Number_of_Ants
    All_Ordered_Lists_of_Bags_In_Vans = [[] for _ in range(Number_of_Ants)]
    
    # Calls the function to fill the van and create a solution as 
    # many times as the value of the variabe Number_of_Ants
    for i in range(Number_of_Ants):
        Ordered_List_of_Bags_In_Van, Current_Van_Weight, Current_Van_Value, T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9 = Ant_fill_van(All_Sets_Of_Bags, T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9)
        
        # Store the results in lists
        All_Ordered_Lists_of_Bags_In_Vans[i] = Ordered_List_of_Bags_In_Van
        All_solution_Values[i] = Current_Van_Value
        
    # Find the best solution out of all the solutions found    
    Max_solution_Value = max(All_solution_Values)
    return All_Ordered_Lists_of_Bags_In_Vans, All_solution_Values, Max_solution_Value



# Creates lists of lists of the information on the solutions that
# have been found

List_of_Max_Values_of_list_of_max_Values = []
List_of_lists_of_list_of_bags_in_van = []
List_of_lists_of_All_solution_Values = []

# This runs the function Create_Multiple_Ant_Solutions as many times as
# the value of the variable Number_Of_Solution_Calculations
for _ in range(Number_Of_Solution_Calculations):
    
    All_Ordered_Lists_of_Bags_In_Vans, All_solution_Values, Max_solution_Value = Create_Multiple_Ant_Solutions(Number_of_Ants, All_Sets_Of_Bags, T_0, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9)
    # Add the solutions to the function in these lists
    List_of_Max_Values_of_list_of_max_Values.append(Max_solution_Value)
    List_of_lists_of_list_of_bags_in_van.append(All_Ordered_Lists_of_Bags_In_Vans)
    List_of_lists_of_All_solution_Values.append(All_solution_Values)

# This prints the best values that the different sets of ants have found
# and then prints the best of the best values.
print("List of max values from every batch p ants finding solutions: ")
print()
print()
print(List_of_Max_Values_of_list_of_max_Values)
print()
print()
print("The max value in the list of the numbers above: ")
print()
print()
print(max(List_of_Max_Values_of_list_of_max_Values))


# Code that can allow you to see the exact bags chosen in a specific 
# solution found by an ant, this is used to check the algorithm 
# works properly and is not selecting the same bag twice 

#print(List_of_lists_of_All_solution_Values[5][1])
#print(List_of_lists_of_list_of_bags_in_van[5][1])


# This function lets you check the exact weight in a van using a specific 
# solution formed by an ant, this lets you check the algorithm is 
# working and is not going over the weight limit or failing to add the 
# weight of a bag to the van weight.

#s = List_of_lists_of_list_of_bags_in_van[5][1]
#print(s)

#measured_van_weight = sum(weights[num -1] for num in s)
#print(measured_van_weight)