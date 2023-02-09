#1 replace special characters
#str1 ="/*jon is @developer & musician!!"


#2 appending new strng
s1 ="luminar"
s2 ="python"
lens1=len(s1)
middle_index=lens1//2
lens2=len(s2)
s3=s1[0:(middle_index+1)]
s4=s1[middle_index:lens1]
nstr=s3+s2+s4
print(nstr)
