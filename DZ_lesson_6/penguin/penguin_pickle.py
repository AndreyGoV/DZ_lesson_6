import pickle


n = 3
str1 = '   _~_    '
str2 = '  (o o)   '
str3 = ' /  V  \\  '
str4 = '/(  _  )\\ '
str5 = '  ^^ ^^   '

obj = f'{str1 * n}\n{str2 * n}\n{str3 * n}\n{str4 * n}\n{str5 * n}'

with open("data.pkl", "wb") as f:
    pickle.dump(obj, f, 2)

print(obj)
