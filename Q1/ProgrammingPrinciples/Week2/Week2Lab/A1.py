# A1: Boolean conditions

A = True
B = True

print("True AND True: " + str(A and B))

B = False
C = True

print("True AND False AND True: " + str(A and B and C))

B = True

print("True OR True OR True: " + str(A or B or C))

B = False

print("True OR False: " + str(A or B))

B = not False
C = not False
D = True

print("True AND Not False AND Not False AND True: " + str(A and B and C and D))
