def getLength(txt):
    lasttext=txt.split()[-1]
    return len(lasttext)
    
def validate(txt):

    if not len(txt):
        raise Exception("String cannot be empty")
        
    if  len(txt)>104:
        raise Exception("String length cannot be greater than 104")
    

        
if __name__ == '__main__':
    try:
        txt=input().strip()
        validate(txt)
        print(getLength(txt), end="\n")      
    except Exception as e:
        print(str(e), end="\n")

