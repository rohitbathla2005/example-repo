class Book():
    def __init__(self,name,title,pages):
        self.name = name
        self.title = title
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.name}"
    def __len__(self):
        return self.pages
b=Book('python','rock',200)
print(b)
print(str(b))
print(len(b))