def graphicUp(x, a, b):
    return ((x-b)/(a-b))

def graphicDown(x, a, b):
    return ((a-x)/(a-b))

def graphicUp(x, a, b):
    return ((x-b)/(a-b))

def graphicDown(x, a, b):
    return ((a-x)/(a-b))

def temperatureMF(x):
    d = {}
    LabelSN=""
    LabelST=""
    SN=0;
    ST=0;
    if(x<=0):
        SN=1
        LabelSN="cold"
    elif(x>0 and x<3):
        SN=graphicUp(x,3,0)
        LabelSN="mild"
        ST=graphicDown(x,3,0)
        LabelST="cold"
    elif(x>=3 and x<=12):
        SN=1
        LabelSN="mild"
    elif(x>12 and x<15):
        SN=graphicUp(x,15,12)
        LabelSN="normal"
        ST=graphicDown(x,15,12)
        LabelST="mild"
    elif(x>=15 and x<=24):
        SN=1
        LabelSN="normal"
    elif(x>24 and x<27):
        SN=graphicUp(x,27,24)
        LabelSN="warm"
        ST=graphicDown(x,27,24)
        LabelST="normal"
    elif(x>=27 and x<=36):
        SN=1
        LabelSN="warm"
    elif(x>36 and x<39):
        SN=graphicUp(x,39,36)
        LabelSN="hot"
        ST=graphicDown(x,39,36)
        LabelST="warm"
    else:
        SN=1
        LabelSN="hot"
    if(LabelSN!="" and SN!=0):
        d = {LabelSN : SN}
    if(LabelST!="" and ST!=0):
        d.update({LabelST : ST})
    return d

def humidityMF(x):
    LabelLN=""
    LabelLT=""
    LN=0;
    LT=0;
    if(x<=10):
        LN=1
        LabelLN="dry"
    elif(x>10 and x<20):
        LN=graphicUp(x,20,10)
        LabelLN="moist"
        LT=graphicDown(x,20,10)
        LabelLT="dry"
    elif(x>=20 and x<=40):
        LN=1
        LabelLN="moist"
    elif(x>40 and x<50):
        LN=graphicUp(x,50,40)
        LabelLN="wet"
        LT=graphicDown(x,50,40)
        LabelLT="moist"
    else:
        LN=1
        LabelLN="wet"
    if(LabelLN!="" and LN!=0):
        d = {LabelLN : LN}
    if(LabelLT!="" and LT!=0):
        d.update({LabelLT : LT})
    return d

def rules(d1, d2):
    res = {}
    for key1 in d1:
        for key2 in d2:
            if(key1 == "cold" and key2 == "dry"):
                res.update({"long":min(d1[key1], d2[key2])})
            elif(key1=="cold" and key2=="moist"):
                res.update({"short":min(d1[key1], d2[key2])})
            elif(key1=="cold" and key2=="wet"):
                res.update({"short":min(d1[key1], d2[key2])})
            elif(key1=="mild" and key2=="dry"):
                res.update({"long":min(d1[key1], d2[key2])})
            elif(key1=="mild" and key2=="moist"):
                res.update({"short":min(d1[key1], d2[key2])})
            elif(key1=="mild" and key2=="wet"):
                res.update({"short":min(d1[key1], d2[key2])})
            elif(key1=="normal" and key2=="dry"):
                res.update({"long":min(d1[key1], d2[key2])})
            elif(key1=="normal" and key2=="moist"):
                res.update({"medium":min(d1[key1], d2[key2])})
            elif(key1=="normal" and key2=="wet"):
                res.update({"short":min(d1[key1], d2[key2])})
            elif(key1=="warm" and key2=="dry"):
                res.update({"long":min(d1[key1], d2[key2])})
            elif(key1=="warm" and key2=="moist"):
                res.update({"medium":min(d1[key1], d2[key2])})
            elif(key1=="warm" and key2=="wet"):
                res.update({"short":min(d1[key1], d2[key2])})
            elif(key1=="hot" and key2=="dry"):
                res.update({"long":min(d1[key1], d2[key2])})
            elif(key1=="hot" and key2=="moist"):
                res.update({"medium":min(d1[key1], d2[key2])})
            elif(key1=="hot" and key2=="wet"):
                res.update({"short":min(d1[key1], d2[key2])})
    return res

