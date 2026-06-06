#Length of String - We use len() function to find the length of a string.
fruit = "Mango"
print("Length of the string is:", len(fruit))

#String Slicing - We can slice a string using the syntax: string_name[start_index:end_index]. It returns a substring from start_index to end_index-1. If we omit start_index, it starts from the beginning of the string. If we omit end_index, it goes till the end of the string.
print("Substring from index 0 to 4:", fruit[0:4])
print("Substring from index 1 to 4:", fruit[1:4])
print("Substring from index 0 to 5(omitting start_index):", fruit[:5])

#Negative Slicing - We can also use negative indexing to slice a string. Negative indexing starts from the end of the string. The last character has an index of -1, the second last character has an index of -2, and so on.

"""Character:  M  a  n  g  o
Index:         0  1  2  3  4
Negative:     -5 -4 -3 -2 -1"""
#We can also see it as - string_name[len(string_name)+start_index:len(string_name)+end_index]. For eg. - fruit[-3:-1] is same as fruit[len(fruit)-3:len(fruit)-1] which is same as fruit[2:4] and its output is "ng".But this is not when the start_index is 0 it will be same as fruit[len(fruit)+0:len(fruit)+end_index] which is same as fruit[len(fruit):len(fruit)+end_index] and its output is empty string because the start index is greater than the end index. When using negative slicing, the start index should be less than the end index for it to work properly.
print("Substring from index 0 to -3:", fruit[0:-3]) # 0 to -3 is same as 0 to len(fruit)-3 which is same as 0 to 2 and its output is "Ma".
print("Substring upto index -3(omitting start_index):", fruit[:-3])
print("Substring from index -1 to index -3 to end:", fruit[-1:-3]) #This will return an empty string because the start index is greater than the end index. When using negative slicing, the start index should be less than the end index for it to work properly.
print("Substring from index -3 to -1:", fruit[-3:-1])