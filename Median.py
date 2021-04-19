import csv
with open("HeightWeight.csv",newline="") as f:
    reader=csv.reader(f)
    fileData=list(reader)
fileData.pop(0)
newData=[]
n=len(fileData)
for i in range(n):
    num=fileData[i][1]
    newData.append(float(num))
newData.sort()
value=len(newData)
if value%2 ==0:
    num1=float(newData[value//2])
    num2=float(newData[(value//2)-1])
    median=(num1+num2)/2
else:
    num=float(newData[value//2])
    median=num
print(median)
