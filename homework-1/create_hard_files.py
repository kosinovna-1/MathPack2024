hard = open('hard_puzzles.txt','r')
i = 1
for line in hard:
    f = open('hard_puzzles/hardpuzzle'+str(i)+'.txt','w')
    f.write(line)
    f.close()
    i+=1
hard.close()
