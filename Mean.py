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
values=len(newData)
sum=0
for x in newData:
    sum=sum+x
mean=sum/values
print(mean)


