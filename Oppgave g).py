
x_list=[1,2,3,4,5,6,7,8,9,10]
y_list=[1,2,3,4,5,6,7,8,9,10]


x_in= x_list[0]
y_in = y_list[0]

def xavrg(x_list):
    sum_1=0
    for element in x_list:
        sum_1 +=element
    
    return sum_1/len(x_list)


def yavrg(y_list):
    sum_2=0
    for element in y_list:
        sum_2 +=element
    
    return sum_2/len(y_list)
ya=yavrg(y_list)
xa = xavrg(x_list)

def a(x_in,y_in,ya,xa):
    
    sum1=0
    for n in range(len(x_list)):
        sum1 += (x_in-xa)*(y_in-ya) /(x_in-xa)**2
         
        

    return sum1
        
a = a(x_in,y_in,ya,xa)

def b(ya,a,xa):
    b = ya-(a*xa)
    return b
if b(ya,a,xa) <0:
    
    print(f'verdien til funksjoonen er {a}X {b(ya,a,xa)}')
else:
    print(f'verdien til funksjoonen er {a}X + {b(ya,a,xa)}')
        
        
        
        
        