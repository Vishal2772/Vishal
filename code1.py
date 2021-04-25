def Fun(lst):
    ##print(lst)
    res_dct = {lst[i]: int(lst[i + 1]) for i in range(0, len(lst), 2)}
    ###print (res_dct)
    return res_dct

def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i-1
        nxt_element = InputList[i]
# Compare the current element with next one
		
        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
        InputList[j+1] = nxt_element
        

    

def MainFun(array_val,n,k,l):
    res = float('inf')
    final_output.clear()
    insertion_sort(array_val)
    ##print("input values",input_items)
    #print("array values", array_val)
    lind=rind=None
    for i in range(n-k+1):
        if res>int(min(res, array_val[i+k-1] - array_val[i])):
            res = int(min(res, array_val[i+k-1] - array_val[i]))
            lind=i
            rind=i+k-1
    #final_res={array_val.keys()[i]:array_val.values()[i] for i in range(lind,rind+1)} 
   # #print("final res=",final_res)
    #print("indes ", lind,rind)
    for j in range(k):
        for name,value in input_items.items():
            if(int(value)==array_val[j+lind]):                
                val = Fun([name,value])
                final_output.update(val)
    #print(final_output.items())
    return res


input_file = open("sample_input.txt",'r')
global input_items, final_output 
input_items = {}
final_output = {}

for line in input_file:
    lines = line.split(":")
    val = Fun(lines)
    input_items.update(val)
   
#print (input_items.values())
val = (input_items.values())
actual = []
for n in val:
    actual.append(int(n))

arr= actual 
n =len(arr) 
input_file.close()
while(True):
    f = open("output.txt", "a")
    k = int(input("Number of employees : ")) 
    f.write("Number of employees : "+str(k))
    f.write("\n")
    f.write("Here the input_items that are selected for distribution are:")
    f.write("\n")
    res = MainFun(arr, n, k,k)
    for name,value in final_output.items():
        f.write(name+" : "+str(value))
        f.write("\n")
    print("Output File Written")
    f.write("And the difference between the chosen goodie with highest price and the lowest price is "+str(res))
    f.write("\n")
    f.write("\n")
    f.close()