mat=[[" "," "," "," "," "],
     [" "," "," "," "," "],
     [" "," "," "," "," "],
     [" "," "," "," "," "],
     [" "," "," "," "," "]]

def check(a):
    main=1
    for i in a:
        for j in i:
            if j==" " or j==16384:main =0
    return main

def transpose(a):
        x=0
        m=[]
        for i in range(len(a[1])):
            m+=[[]]
            for j in a:
                m[i]+=[(j[x])]
            x+=1
        return m

def shift(mat,user):
    if user in ["w","s"]:mat=transpose(mat)
    for k in range(5):
        for i in range(5):
            for j in range(5):
                if user in ["a","w"]:
                    if mat[i][j]==" ":
                        mat[i].pop(j)
                        mat[i]+=[" "]
                elif user in ["d","s"]:
                    if mat[i][j]==" ":
                        mat[i].pop(j)
                        mat[i].insert(0," ")
    if user in ["w","s"]:mat=transpose(mat)
    return mat

def insert2(a):        
    import random
    i=random.randint(0,4)
    j=random.randint(0,4)
    if a[i][j]!=" ":insert2(a)
    else:a[i][j]=2

def combine(a,user):
    if user in ["w","s"]:a=transpose(a)
    for i in range(5):
        for j in range(4):
            if user in ["a","w"]:
                if a[i][j]!=" " != a[i][j+1] and a[i][j]==a[i][j+1]:
                        a[i][j]+=a[i][j+1]
                        a[i][j+1]+=a[i][j]
                        a[i][j+1]=" "
            elif user in ["d","s"]:
                if a[i][j]!=" " != a[i][j+1] and a[i][j]==a[i][j+1]:
                        a[i][j+1]+=a[i][j]
                        a[i][j]+=a[i][j+1]
                        a[i][j]=" "
    if user in ["w","s"]:a=transpose(a)
    return a

def display(mat):
    for i in mat:
        for j in i:
            print("|",j,end="")
        print("|")

def spinput():
    user=input("w,a,s,d:")
    if user in ["w","a","s","d","W","A","S","D"]:
        return user.lower()
    else:
        print("Only w,a,s,d")
        spinput()


point=[]
def score(mat,point):
    for i in mat:
        for j in i:
            if j!=" " and j!= 2:
                point+=[int(j)]

while 1:
    insert2(mat)
    display(mat)
    if check(mat)==1:break
    print("\n")
    user=spinput()
    mat=shift(mat,user)
    mat=combine(mat,user)
    display(mat)
    print("\n")
    if check(mat)==1:break
    score(mat,point)
print("okok.. there's no space for one more element that means its the end...")

point=set(point)
print("Your score is",sum(point))