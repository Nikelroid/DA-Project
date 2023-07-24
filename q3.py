
def place_rook(n, rectangles):
    rectangles.sort(key=lambda x: (x[2]))
    qc= [x[4] for x in rectangles]

    last_rook = -2
    chosen = set()
    col = []
    for r in rectangles:
        n = max(r[0],last_rook)
        while n in chosen:
            n += 1
            if r[2]<n:
                return [],[]
        last_rook= n-400
        chosen.add(n)
        col.append(n)
    



    rectangles.sort(key=lambda x: (x[3]))
    qr= [x[4] for x in rectangles]
    last_rook = -2
    chosen = set()
    row = []
    for r in rectangles:
        n = max(r[1],last_rook)
        while n in chosen:
            n += 1
            if r[3]<n:
                return [],[]
        last_rook= n-400
        chosen.add(n)
        row.append(n)

    col = list(zip(col,qc))
    row = list(zip(row,qr))
    col.sort(key=lambda x: x[1])
    row.sort(key=lambda x: x[1])

    return col,row

import sys
rects = []
n = int(sys.stdin.readline().strip())
for i in range (n):
    inp = list(map(int, sys.stdin.readline().strip().split()))
    inp.append(i)
    rects.append(inp)

cc,rr = place_rook(n,rects)

if (min(len(cc),len(rr))<n):
    sys.stdout.write("impossible")
else:
    for row,col in zip(cc,rr):
        sys.stdout.write(str(row[0]) + " " + str(col[0]) + "\n")    