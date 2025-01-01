import numpy as np
import pandas as pd

data = pd.read_csv('trainingdata.csv')
concepts = np.array(data.iloc[:, :-1])
target = np.array(data.iloc[:, -1])

def learn(concepts, target):
    specific_h = concepts[0].copy()
    general_h = [["?" for _ in range(len(specific_h))] for _ in range (len(specific_h))]

    print("Initialization of specific_h and general_h")
    print(specific_h)
    print(general_h)

    for i, instance in enumerate(concepts):
        if target[i] == "Yes":
            for x in range(len(specific_h)):
                if instance[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
        elif target[i] == "No":
            for x in range(len(specific_h)):
                if instance[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'

        print(f"\nSteps of Candidate Elimination Algorithm {i+1}")
        print(specific_h)
        print(general_h)

    general_h = [h for h in general_h if h!=["?"] * len(specific_h)]

    return specific_h, general_h

s_final, g_final = learn(concepts, target)

print("\nFinal Specific_h:")
print(s_final)
print("\nFinal General_h:")
print(g_final)
