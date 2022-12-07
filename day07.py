from tools import config, log,helper
import logging

today="7"
dirs={}
inputfile="input."+today

def pdirs(workdir):
    root=False
    while not root:
        size=dirs[workdir]["size"]
        parent=dirs[workdir]["parent"]
        if workdir=="/":
            root=True
            print("/ [{}]".format(size))
        else:
            print("{} [{}] - ".format(workdir,size),end="")
        #print("WORKDIR: {} size: {} PARENT: {} size: {}".format(workdir,dirs[workdir]["size"],parent,dirs[parent]["size"]))
        
        workdir=parent
        

def updatesize(workdir,size):
    root=False
    while not root:
        dirs[workdir]["size"]+=size
        parent=dirs[workdir]["parent"]
        if workdir=="/":
            root=True
            print("/ [{}] + {}".format(dirs[workdir]["size"],size))
        else:
            print("{} [{}] - ".format(workdir,dirs[workdir]["size"]),end="")
        #print("WORKDIR: {} size: {} PARENT: {} size: {}".format(workdir,dirs[workdir]["size"],parent,dirs[parent]["size"]))
        workdir=parent
# not used


def gendir(dir,parent):
    dirs[dir]={}
    dirs[dir]["size"]=0
    dirs[dir]["parent"]=parent
    dirs[dir]["subdirs"]=[]


def createdirtree():
    inputdata = helper.read_input(inputfile)
    gendir("/","/")

    dir="/"
    parentdir="/"
    currentdir=dir
    for item in inputdata:
        print("{} :".format(item),end=" ")
        currentdir=dir
        if item.find("$ cd")==0:
            dir=item.split(" ")[-1]
            #print("directory change: "+dir)
            if dir=="..":
                dir=dirs[currentdir]["parent"]
                pdirs(dir)
            elif dir=="/":
                currentdir="/"
                pdirs(dir)
            else:
                dir=currentdir+"/"+dir
                if not dirs.get(dir,False):
                    dirs[dir]={}
                    dirs[dir]["parent"]=currentdir
                    dirs[dir]["size"]=0
                currentdir=dir
                pdirs(dir)
        elif item.find("dir")==0:
            #print("dir found")
            c,d=item.split(" ")
            if not dirs.get(d,False):
                
                dirs[d]={}
                dirs[d]["parent"]=currentdir
                dirs[d]["size"]=0
                logging.debug("added to dirs with parrent {}".format(currentdir))
            else:
                logging.debug("dir known")        
        elif item.find("$ ls")==0:
            logging.debug("no action")
            #next
        else:
            #print("sizes:"+item)
            size,fname=item.split(" ")
            updatesize(currentdir,int(size))

def puzzle_01():
    
    result=0
    
    createdirtree()
    #print(dirs)
    logging.debug("XXXXXXXXXXXXXXXXXXXXXXXXXX")
    logging.debug("Filtering DIRS")
    result=0
    for dir in dirs:
        if dirs[dir]["size"]<=100000:
            pdirs(dir)
            result+=dirs[dir]["size"]
    print("Puzzle-1: Result: {}".format(result))


def puzzle_02():

    inputdata = helper.read_input(inputfile)
    result=0
    diskmax=70000000
    spaceneeded=30000000    

    freespace=diskmax-dirs["/"]["size"]
    #print("Freespace: {}".format(freespace))
    toCleanup=spaceneeded-freespace
    #print("Need to cleanup: {}".format(toCleanup))
    #print("Puzzle-2: Result: {}".format(result))
    dirstouse=[]
    for dir in dirs:
        size=dirs[dir]["size"]
        
        if size >=toCleanup:
            #print("dir: {} size: {}".format(dir,size))
            dirstouse.append(size)
    dirstouse.sort()
    result=dirstouse[0]
    print("Puzzle-2: Result: {}".format(result))

print("-------------------------------")
print("Day {} Results".format(today))
print("-------------------------------")
puzzle_01()
print("-------------------------------")
puzzle_02()
print("-------------------------------")
