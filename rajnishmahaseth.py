#open input file to read input
input_file=open("sample_input.txt", "r")

#open output file to write output 
output_file =open("output.txt", "w+") 
goodies={}
output_list=[]
#reading input file into the dict
for f in input_file:                   
                   index_toRead_price=f.index(":")
                   print(f[index_toRead_price+1 :].strip())
                   print(f[:index_toRead_price])
                   goodies[f[:index_toRead_price]]=f[index_toRead_price+1:].strip()
                   #print(goodies)

print(goodies)
#list of prices from dict
prices_only=list(goodies.values())
prices_only=[int(i) for i in prices_only]
             
#sorted list in descending order to get prices to be distributed in the order 
prices_only.sort(reverse=True)
print (prices_only)
             
#taking inputs
no_of_employees=int(input("Enter the number of employees: " ))
length_considered=(len(prices_only)-no_of_employees)
print(length_considered)

#finding minimum_ difference between highest and lowest 
for i in range(length_considered):
                    maxPrice=prices_only[i]
                    minPrice=prices_only[no_of_employees+i]
                    if i==0:
                        difference=maxPrice-minPrice 
                        chosen_index=i
                    elif (maxPrice-minPrice) <difference :
                        difference=maxPrice-minPrice 
                        chosen_index=i

chosen_prices=prices_only[chosen_index:no_of_employees+chosen_index]

#difference between high and low price
difference=max(chosen_prices)-min(chosen_prices)
print ("difference",difference)

count=0
for key,value in goodies.items():
    prices_only [count]
    print (value)
    if int (value) in chosen_prices and count<no_of_employees:
        str1=key+" : "+value
    #preparing list for output
        output_list.append(str1)
        count+=1
        print(str1)

#writing to output file
output_file.write("The goodies selected for distribution are: ")
output_file.write ("\n")

for i in output_list:
    output_file.write(i)
    output_file.write("\n")
output_file.write("The difference between the chosen goodie with highest price and the lowest price is "+str (difference))

input_file.close() 
output_file.close()
