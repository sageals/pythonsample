from pathlib import Path


path = Path("ecommerce")
print(path.exists())
#path1 = Path("NewFolder")
#print(path1.rmdir())   #also use to create a directory use mkdir()
path2 = Path()
for file in path2.glob('*.py'):
    print(file)


