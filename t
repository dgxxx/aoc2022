def calc_t(h,t):
    if abs(h["x"]-t["x"])<=1 and abs(h["y"]-t["y"])<=1:
        print("no need to move t")


    elif h["x"]-t["x"] ==0:
        if h["y"]-t["y"]>1:
            t["y"]+=1
        elif h["y"]-t["y"]<-1:
            t["y"]-=1
    elif h["y"]-t["y"]==0:
        if h["x"]-t["x"] >1:
            t["x"]+=1
        elif h["x"]-t["x"] <-1:
            t["x"]-=1
    elif h["x"]-t["x"]>0 and h["y"]-t["y"]>0:
        t["x"]+=1
        t["y"]+=1
    elif h["x"]-t["x"]>0 and h["y"]-t["y"]<0:
        t["x"]+=1
        t["y"]-=1
    elif h["x"]-t["x"]<0 and h["y"]-t["y"]<0:
        t["x"]-=1
        t["y"]-=1
    elif h["x"]-t["x"]<0 and h["y"]-t["y"]>0:
        t["x"]-=1
        t["y"]+=1