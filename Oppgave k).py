


y_list=[-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18,
21, 26, 21, 31, 15, 4, 1, -2]

x_list = list()
for index in range(len(y_list)):
    x_list.append(index)

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

if a==0:
    print("Det er ingen trend")
elif a >0:
    print("Trenden er positiv")
else:
    print("Trenden er negativ")
        
        