print("Player 1\n")
for i in range(0,P1_fighter_stats):
    print("Fighter #No: ",str(i+1))
    for r in i:
        print(Stats[i.index(r)]+":",r)            
    print("\n")
