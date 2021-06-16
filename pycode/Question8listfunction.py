# Q8.	Given a list, l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9], store 3 sub-lists such that those
# contains multiples of 2, 3 and 4 respectively. Print the lists.
# Repeat storing and printing the lists same as above as multiples of 2, 3 and 4 but take
# l1 as [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
j = k = l = 1

sublist2 = []
sublist3 = []
sublist4 = []
sublist2multiples = []
sublist3multiples = []
sublist4multiples = []
#print (j, k, sublist2multiples, sublist3multiples, sublist4multiples )
listing =0
while listing <=2:
    if listing == 0:
        for i in l1:
       # print("now entering 2nd if", i)
       # print("now entering 2nd if ", j)
       # print("now entering 2nd if ", k)
           #create sublist
        
            if i ==2 and j <= 3:
                while j<=3:
                    sublist2.append(i*j)   
                    j+=1
                    
            if i ==3 and k<=3:
                while k<=3:
                    sublist3.append(i*k)
                    k+=1
        
         
            if i ==4 and l<=3:
                while l<=3:
                    sublist4.append(i*l)   
                    l+=1
            
        print("Sublist for 2 created from list l1 =", sublist2)
        print("Sublist for 2 created from list l1 =", sublist3)
        print("Sublist for 2 created from list l1 =", sublist4)
    
    elif listing ==1:
        print("listing =", listing, "entering into second for loop")
        i = j = k = l = 1
        for i in l2:

            if i == 2 and j <= 3:
                while j<=3:
                    sublist2multiples.append(i*j)   
                    j+=1
                  
            if i ==3 and k<=3:
                while k<=3:
                    sublist3multiples.append(i*k)
         #       print("i = ", i)
         #      print("k = ", j)
                    k+=1
        
         
            if i ==4 and l<=3:
                while l<=3:
                    sublist4multiples.append(i*l)   
                    l+=1
            
        print(sublist2multiples)
        print(sublist3multiples)
        print(sublist4multiples)
    print("increment listing now =", listing)
    listing += 1




