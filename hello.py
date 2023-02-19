fname = input('enter file name ')
if len(fname) < 1 : fname ='clown.txt'
hand = open(fname)


di = dict()
for lin in hand:
    lin = lin.rstrip()
    #print(lin)
    for w in wds:
        # odiom: retrieve/create/update counter
        
        di[w]= di.get(w,0) +1
        #print(w,'new',di[w])

        
        #print(w,di[w])
#print(di)

tmp = list()
for k,v in di.items():
    #print(k,v)
    newt = (v,k)
    tmp.append(newt)
#print('flipped',tmp)
tmp = sorted(tmp , reverse=True)
#print('sorted',tmp)

for v,k in tmp:
    print(k,v)