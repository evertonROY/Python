N, S = input().split()
while N != "#":
 S = int(S)
 if S >= 90 and S <= 100:
    print(N, "Alta")
 else:
     print(N, "Internar")
 N, S = input().split()
print("")


