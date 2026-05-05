# class student:
#     m = []
#     for i in range(1,4):
#         a = int(input(f"enter marks for {i}:"))
#         m.append(a)
#     d =sum(m)//3
#     def __init__(self,n,m,d):
#        self.name = n
#        self.marks = m
#        self.division = d
# s1 = student("vijay",student.m,student.d)
# print(f"name is {s1.name},\nmarks is {s1.marks},\navg is {s1.division}")
# class Student:

#     def __init__(self) : 
#        self.acc = False
#        self.brk = False

#     def car(self):
#         self.acc = True
#         self.brk = True
#         print("the car is running anf u r goood to go")

# s1 = Student()
# s1.car()
# import csv
# name = "exe.csv"
# d = [
#     ['Name', 'Age', 'City'],
#     ['Alice', 25, 'New York'],
#     ['Bob', 30, 'Los Angeles']
# ]
# with open(name,"w",newline = "") as f:
#     write = csv.writer(f)
#     for i in d:
#         write.writerow(i)
#         print(i)
# data = [
#     {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
#     {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'}
# ]
# with open("ex.csv","w",newline= '') as f:
#     write = csv.DictWriter(f,feildnames = ["name",'age','city'])
#     write.writeheader()
#     write.writerows(data)
# with open('ts.tsv', mode='r', newline='') as file:
#     reader = csv.reader(file, delimiter=';')
#     for row in reader:
#         print(row)
# line = 3
# lin = "hello,im vijay and now im having a lap and im learning python okay bye\n"
# with open("munna.txt","r") as f:
#     linew = f.readlines()
# linew.insert(line-1,lin)
# with open("munna.txt","w") as f:
#     f.writelines(linew)
# try:

#     with open("demo.txt","x") as f:
#         d = f.write("successfully new file is created")
#         print(d)
# except FileExistsError:
#     print("file is alredy there ")   

# import csv
# total_marks = 0
# count = 0

# with open("exe.csv","r") as f:
#     read = csv.reader(f)
#     header = next(read)

#     for i in read:
#         name = i[1]
#         roll = i[0]
#         marks = int(i[2])
#         print("roll:",roll,"name:",name,"marks:",marks)
#         count += 1
#         total_marks += marks
#     print(total_marks/count)
# import csv
# name ="marks.csv"
# data = [
#     ['Name', 'Age', 'City'],
#     ['Alice', 25, 'New York'],
#     ['Bob', 30, 'Los Angeles']
# ]
# with open(name,"w",newline="") as f:
#     writ = csv.writer(f)
#     for i in data:
#         writ.writerow(i)
#         print(i)
# n = input("enter u r name:")
# print(f"{n}\nhello welcome to KBC")
# quetions = [
# {
#   "que" : "1.Which planet is known as the red planet?",
#   "opt" :
#     {
#       "a":"venus",
#       "b":"mars",
#       "c":"saturn",
#     },
#     "ans" : "b",
#    "prize":"1000",
# },
# {
#     "que": "Who was the first Prime Minister of India?",
#     "opt":{
#         "a":" Mahatma Gandhi",
#         "b":" Jawaharlal Nehru",
#     },
#     "ans": "b",
#     "prize": "5000",
# },

      


# ]
# p_m = 0
# for i in quetions:
#     print(i["que"])
#     for key, value in i["opt"].items():
#         print(f"{key}-{value}")
#     user_ans = input("enter u ans:").lower()
#     if(user_ans == i["ans"]):
#         p_m +=int(i["prize"])
#     else:
#         print(f"incorrect ans and the ans is {i['ans']}")
# print(p_m)
import random as rd
print('''
      r = rock
      p = paper
      s= scisscors
     ''' )
score_user = 0
score_mac = 0
t = 0
r = 0
s = 0
def calling():
            global score_mac,score_user
            if(a == w):
              print("tie point to both")
              score_user += 1
              score_mac += 1
            elif((a == "p" and w == "r" ) or (a == "s" and w =="p" )or (a == "r" and w == "s")):
                 print("user won")
                 score_user += 1
            else:
                print("mac won")
                score_mac +=1
print("game starts\nget ready to bet the mac!")
while True:
    try:
        w = rd.choice(["r","p","s"])
        a = input("enter ur choice from above: ")
        if a not in ["r", "p", "s"]:
            if(a == "n"):
                print(f"wanna try later okay\nthe ur score is :{score_user} and mac score is :{score_mac}\nthank you")
                break
            else:
                raise ValueError
        if(a == "r"):
            r += 1
        elif(a == "p"):
            t += 1
        else:
            s += 1
        calling()
        if(t == 1 and r == 1 and s == 1):
          a1 = input("wanted to play ,y/n: ")
          if(a1 not in ["y","n"]):
             raise ValueError
          if(a1.lower() == "y" ):
             s,r,t = 0,0,0
             print(f"the ur score is :{score_user} and mac score is :{score_mac}")
             continue
          else:
               print(f"             >the ur score is:{score_user}\n           >the mac score is:{score_mac}")
               print("thank you")  
               break  
    except ValueError:
       print("enter correct input")
       continue
   

