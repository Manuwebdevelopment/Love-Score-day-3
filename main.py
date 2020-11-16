# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
comb_name = name1 + name2
all_lowercase = comb_name.lower()
t = all_lowercase.count('t')
r = all_lowercase.count('r')
u = all_lowercase.count('u')
e = all_lowercase.count('e')

true = t + r + u + e

l = all_lowercase.count('l')
o = all_lowercase.count('o')
v = all_lowercase.count('v')
e = all_lowercase.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
  print(f'Your love score is {love_score}, you go together like coke and mentos.')
elif love_score >= 40 and love_score <= 50:
  print(f'Your love score is {love_score}, you are alright together.')
else:
  print(f'Your love score is {love_score}')