def getRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    roman=""
      
    while number:
        div = number // num[i]
        number %= num[i]
  
        while div:
            roman = roman+sym[i]
            div -= 1
        i -= 1
    return roman 
    
if __name__ == '__main__':
    try:
        number=int(input())
        
        if number<1 or number>3999:
            print("Number must be between 1 - 3999", end="\n")
        else:
            print(getRoman(number))
            
    except:
        print("Input Must be valid number ", end="\n")
