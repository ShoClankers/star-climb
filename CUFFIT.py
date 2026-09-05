def ways(stairs):
    if stairs < 0:
        return 0 
    if stairs == 0:
        return 1
    return ways(stairs - 1) + ways(stairs - 2)

input("ways count every dinstinct way up n stairs - 1 step or 2 steps at a time: ")
print("  ways(3) =", ways(3))
print("  ways(4) =", ways(4))

n = int(input("enter number of steps (try 5 or 6): "))
guess = input("What is ways(" + str(n) + ")? ")
input("ways(stairs) = ways(stairs-1) + ways(stairs-2) - 1 step or 2 steps at a time")
print(" ways(" + str(n) + ") =", ways(n), " your guess was", guess)