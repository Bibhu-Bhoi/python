a=str(input("Enter a string:"))
reverse_str=a[::-1]
print("Reverse of the given string is:",reverse_str)
vowel=0
consonant=0
vowel_count=set("aeiouAEIOU")
for char in a:
    if char.isalpha():
        if char in vowel_count:
            vowel+=1
        else:
            consonant+=1
print("number of vowels is:",vowel)
print("number of consonant is:",consonant)
