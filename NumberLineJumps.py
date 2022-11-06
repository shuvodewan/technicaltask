def kangaroo(x1, v1, x2, v2):
    if v1 <= v2 or (x2 - x1) % (v1 - v2) != 0:
        return "NO"
    else:
        return "YES"
    

def valuValidator(x1, v1, x2, v2):
    if x1<0 and x1>x2:
    	raise Exception("X1 must be smaler than x2 & greater than 0")
    if x2>10000:
    	raise Exception("X2 cant be grater than 10000")
    if v1<0 and v1>10000:
    	raise Exception("v1 cant be grater than 10000 & smaler than 1") 
    if v2<0 and v2>10000:
    	raise Exception("v2 cant be grater than 10000 & smaler than 1")
    	
         
def inputValidator(inp):
    
    values=inp.rstrip().split()
    if  len(values) != 4:
         raise Exception("all 4 input valus are required")
         
    return [int(i) for i in values]
    
    
if __name__ == '__main__':
    
    try:
       #Take input parameters
        inp=input()
            
        #validate inputes
        x1,v1,x2,v2=inputValidator(inp)
        valuValidator(x1,v1,x2,v2)
            
        #print result
        print(kangaroo(x1,v1,x2,v2), sep="\n")
    except Exception as e:
        print(str(e), end="\n")
    
