string = "gcyzbytnnvsuepxqrpzcqrgppmcsfbelddmgdfvscpohfozydydvrlngarbfsfsxkefpkcioswvzkuzqvcnoqavqswxmdpmovtffwnwomrnwomolrczhcwzwuwjynxoiqtqmhmatfprteigxkgeoednzbwxotnwjgmypyakesezwmgtyozouebthzsvuftgoiefgesmwwoukwpkmqagucabbsyyaseocivkonxnlnjxjzhxpidmmdppyqnykromblwszvfmioktptqhdutpzkhzauxkonyrbvjaqqobhywwundxjypijwklshyixwayrlakcqljrhflwlkflzqwxaisjgaieciwokiqbtbscgdztpgfpyboalgmrjuylfwbperszskbbpcwflbwldmmotyieuirzetrikjhfwkilneqagollbxbwxlastrtxkmfxwoeszmfmqyoymzlnznlwalqufmtrybowpuqogwczuqxisjyryjpyxiucuovurmrggjvnfzobqlkkwkbwtsvsarwwhsryekfktczbbnctbodzygwuztmzkjwubpsfzzrsbrvfgyyjocjnkfhjyvjkehgfw"
print(len(string))
#if 1 > len(string) > 1000:
#    break
row = input("How many rows would you like? ")
#print(row)
row_count = int(row)
if len(string) < row_count:
    row_count = len(string)

print("Row count:", row_count)

diagonal_count = row_count - 2

make_columns = diagonal_count + 1

if make_columns == 0:
    make_columns = 1

#make a list of the various letters in
letters = list()
for letter in string:
    letters.append(letter)
print(letters)
#letters.pop()

master_column_list = list()
initial_index = 0

empty_count = row_count - 2
not_empty = row_count - 2


#NEXT TIME: ask Paige about whether lines 25-27 are necessary and how to rewrite them.


while len(letters) > 0:

#    if len(letters) < row_count:
#        rowcount = len(letters)
# would the above lines solve the


#python how to create n number of empty lists
#look up modulo? (tells you remainder) -- useful for finding out how many columns
#that I need to make.
#add a column to the master list each time. Maybe create column first and then
#add it to your master list.


#I want to append the first row_number of items from the list "letters" to
#column_one.
#you want to create a column before the first column, and then at each
#subsequent diagonalself.

    for x in range(make_columns):
        generic_column = list()
        master_column_list.append(generic_column)

#    print("line 40", master_column_list)
#    initial_index = 0
#master_column_list.insert(rat,letters[0])
#print(master_column_list[0])

#initial_letter = letters[0] . How come this didn't work in place of letters[0]?


#cat = master_column_list[0]
    #print("line 60, len(letters)", len(letters))
    #print("line 61 initial_index", initial_index)

    for x in range(row_count):
#    cat.append(letters[0])
#        print("initial_index at line 60:", initial_index)
#        print("length of letters at line 61:", len(letters))
        master_column_list[initial_index].append(letters[0])
        #print("initial_index at line 60:", initial_index)
        #print("length of letters at line 61:", len(letters))
        letters.pop(0)

#        if len(letters) < row_count:
        #    row_count = len(letters)

#    print("line 69: master_column_list[0] :", master_column_list[0])

#    print(cat)
#    rat = rat + 1
#    print(master_column_list[0])

    subsequent_index = initial_index + 1
    not_empty = empty_count
#    print("line 77, not_empty: ", not_empty)
    if len(letters) < 1:
        break
    for x in range(diagonal_count):
        if len(letters) > 0:
            for y in range(row_count):
                master_column_list[subsequent_index].append(0)
#        master_column_list[subsequent_index].append(letters[0])
#            print("Line 85, subsequent index: ",subsequent_index)
#            print("Line 86, not_empty: ", not_empty)
#            print("Line 89, master_column_list: ", master_column_list)
            master_column_list[subsequent_index][not_empty] = (letters[0])
            letters.pop(0)
            subsequent_index = subsequent_index + 1
            not_empty = not_empty - 1


    initial_index = subsequent_index
#    print("initial_index : ", initial_index)

    if len(letters) < row_count:
        row_count = len(letters)
#I thought the above two lines would keep the program from creating empty columns
# at the end. But for some reason they didn't.


    print(master_column_list)

#below removes the empty lists within master_column_list
#print(master_column_list)
while [] in master_column_list :
    master_column_list.remove([])

#print(master_column_list)
    #initial_index = subsequent_index + 1
#for i in master_column_list:
#    for x in i:
#        print(x)

#now we make a master list of all the rows.
master_rows_list = list()
column_number = 0
column_placement = 0
#generic_row = list()
row_count = int(row)
#column_placement_max = row_count - 1

#print("line 125, row_count: ", row_count)

for row in range(row_count):
    generic_row = list()
    master_rows_list.append(generic_row)
#print(master_column_list[column_number][column_placement])

#print(master_column_list)

for row_index in range(row_count):
    print("")
    print("")
    print("row index:", row_index)
    for column in master_column_list:
        print("")
        print("master_rows_list: ", master_rows_list)
        print("column: ", column)
        print("master_rows_list[row_index]: ", master_rows_list[row_index])
        if row_index < len(column):
            master_rows_list[row_index].append(column[row_index])
            print("master_rows_list[row_index]: ", master_rows_list[row_index])
            print("column[row_index]: ", column[row_index])
#            print("master_rows_list: ", master_rows_list)

final_list = []
for row in master_rows_list:
    for item in row:
        if item != 0:
            final_list.append(item)
print("final_list: ", final_list)
print("")
print("")
output = "".join(final_list)
print("This is the answer: ", output)







#What do I need the below to do?
#First go into first element in master_rows_list and add the first element from
#every row in master_column_list.
#Actually, sequentially append the elements of the first column in master_column_list
#into the first element of each row.
#row_index = 0
#while row_index < row_count:
    #for master_rows_list[row_index]:
#    column_number = 0
#    print("length of master column list: ", len(master_column_list))
#it's not changing row list after the first placment.
#    for element in range(len(master_column_list)):
#        if column_placement == row_count:
#            column_placment = 0
#    for x in range(len(master_column_list)):
#        if column_number < len(master_column_list):
#        print(master_column_list[column_number][column_placement])
#            print("column_number: ",column_number)
#            print("column_placment: ", column_placement)
#            print("line 142, master_rows_list: ", master_rows_list)
#            master_rows_list[row_index].append(master_column_list[column_number][column_placement])
#            column_number = column_number + 1


#    column_placement = column_placement + 1
#    row_index = row_index + 1
#    column_placement = 0

#print("line 129 master rows list: ", master_rows_list)



#else: break
#column_two = list()


#need to update diagonal_number each time through
#need to create new list each time through
#empty = 0
#variable = 1
#placement = row_count - variable
#print(placement)
#for x in range(diagonal_number):p
#    if variable < 1:
#        break
#    else:
#        column_two.insert(0,empty)
#        column_two.insert((row_count-1))
#p        variable = variable + 1


#print(column_one)

#Sure, you can use slice indexing:

#a_list[1:1] = b_list
#Just to demonstrate the general algorithm, if you were to implement the my_extend function in a hypothetical custom list class, it would look like this:

#def my_extend(self, other_list, index):
#    self[index:index] = other_list
