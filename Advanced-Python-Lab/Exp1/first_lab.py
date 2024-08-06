# with open("hello.txt", "r+") as f:
#     text = f.read()
#     print(text)
#     print("____________")
#     f.seek(0)
#     print(f.read())


myArray = [4,5, 6, 7,4, 7]  
a, b, c, d, e, f = myArray
print(d)
text = "this is a funny text"

data, isd, another, important = text.strip().split(maxsplit=3)
print(another)