import pandas as pd
import math

df = pd.read_excel("DataFinal2.xlsx")
q1List = df['Are you a new student or mentor?'].values.tolist()
q2List = df['What course are you taking?'].values.tolist()
q3List = df['What excites you most about university?'].values.tolist()
q4List = df['It is mid-semester, feeling tired but it is Friday night, I am going to:'].values.tolist()
q5List = df['Exams are coming, I am feeling:'].values.tolist()
#q6List = df['I am being shipped off to a deserted island, I can only bring one of the following items, I will be taking:'].values.tolist()
q7List = df['Which of these words best describes me:'].values.tolist()
q8List = df['Your report is due today, but your lecturer emails you the deadline has been postponed a week. You:'].values.tolist()
q9List = df['Got a not-so-good grade in a test, I am feeling:'].values.tolist()
q10List = df['I have pledged to spend 100 days without eating chocolate, but on the 80th day someone offers me a bit:'].values.tolist()
nameList = df['What is your first and last name? (Please submit without any accents or specific language characters)'].values.tolist()
emailList = df['Username'].values.tolist()
genderList =df['What is your gender?'].values.tolist()
    
class person:
    def __init__(self,name,email,gender,q1,q2,q3,q4,q5,q7,q8,q9,q10,x1,y1,z1):
        self.name=name
        self.email=email
        self.gender=gender
        self.q1=q1
        self.q2=q2
        self.q3=q3
        self.q4=q4
        self.q5=q5
        #self.q6=q6
        self.q7=q7
        self.q8=q8
        self.q9=q9
        self.q10=q10
        self.x1=0
        self.y1=0
        self.z1=0


studentsList = []     
namesList = []
def assignStudentsToClass():
    i=0
    while i<(len(q1List)):
        student=person(nameList[i],emailList[i],genderList[i],q1List[i],q2List[i],q3List[i],q4List[i],q5List[i],q7List[i],q8List[i],q9List[i],q10List[i],0,0,0)
        if student.name not in namesList :
            namesList.append(student.name)
            studentsList.append(student)
        i+=1
    return studentsList

assignStudentsToClass()

#print(namesList)
#print(studentsList)

MentorList=[]
FresherList=[]
IMEEList=[]
EEEList=[]
RoboticsList=[]
IMEEMentorList=[]
EEEMentorList=[]
RoboticsMentorList=[]

def sortingMentorsAndFreshers():
    x=0
    for x in range(len(studentsList)):
        if studentsList[x].q1=='Mentor':
            MentorList.append(studentsList[x])
        else:
            FresherList.append(studentsList[x])
            
            
def sortingFresherCourses():
    x=0
    for x in range(len(studentsList)):
        if studentsList[x].q2=='Integrated Mechanical and Electrical Engineering (IMEE)' and studentsList[x].q1=='New student':
            IMEEList.append(studentsList[x])
        if studentsList[x].q2=='Robotics Engineering'and studentsList[x].q1=='New student':
            RoboticsList.append(studentsList[x])
        if studentsList[x].q2=='Electrical and Electronic Engineering (EEE)' and studentsList[x].q1=='New student':
            EEEList.append(studentsList[x])

def sortingMentorCourses():
    x=0
    for x in range(len(studentsList)):
        if studentsList[x].q2=='Integrated Mechanical and Electrical Engineering (IMEE)' and studentsList[x].q1=='Mentor':
            IMEEMentorList.append(studentsList[x])
        if studentsList[x].q2=='Robotics Engineering'and studentsList[x].q1=='Mentor':
            RoboticsMentorList.append(studentsList[x])
        if studentsList[x].q2=='Electrical and Electronic Engineering (EEE)' and studentsList[x].q1=='Mentor':
            EEEMentorList.append(studentsList[x])
    
sortingMentorsAndFreshers()
sortingFresherCourses()
sortingMentorCourses()
UnassignedFresherList =[]
UnassignedFresherList = FresherList

def personalityScore():
    x=0
    for x in range(len(studentsList)):
        if studentsList[x].q3=='Joining/attending sports clubs or societies':
            studentsList[x].x1+=0
            studentsList[x].y1+=0
        if studentsList[x].q3=='Nightlife and partying':
            studentsList[x].x1+=0
            studentsList[x].y1+=1
        if studentsList[x].q3=='Studying and expanding your knowledge':
            studentsList[x].x1+=1
            studentsList[x].y1+=0
        if studentsList[x].q4=='Stay home and rest, I have done loads this week!':
            studentsList[x].x1+=0
            studentsList[x].y1+=(-1)
        if studentsList[x].q4=='Gotta go out, will rest sunday':
            studentsList[x].x1+=0
            studentsList[x].y1+=1
        if studentsList[x].q4=='Will probably chill at home with some friends':
            studentsList[x].x1+=0
            studentsList[x].y1+=0
        if studentsList[x].q5=='A bit stressed, probably should have done more work':
            studentsList[x].x1+=(-1)
            studentsList[x].y1+=0
        if studentsList[x].q5=='Good, everything is up to date, studied regularly':
            studentsList[x].x1+=1
            studentsList[x].y1+=0
        if studentsList[x].q5=='Prepared for most exams, but there is always that one I should have studied more for':
            studentsList[x].x1+=0
            studentsList[x].y1+=0
        if studentsList[x].q7=='Responsible':
            studentsList[x].x1+=1
            studentsList[x].y1+=0
        if studentsList[x].q7=='Extrovert':
            studentsList[x].x1+=0
            studentsList[x].y1+=1
        if studentsList[x].q7=='Curious':
            studentsList[x].x1+=0
            studentsList[x].y1+=0
        if studentsList[x].q7=='Dynamic':
            studentsList[x].x1+=1
            studentsList[x].y1+=1
        if studentsList[x].q7=='Shy':
            studentsList[x].x1+=0
            studentsList[x].y1+=(-1)
        if studentsList[x].q7=='Sociable':
            studentsList[x].x1+=0
            studentsList[x].y1+=0.5
        if studentsList[x].q7=='Pragmatic':
            studentsList[x].z1+=(-0.5)
        if studentsList[x].q8=='Submit it the same day, the report was good enough for submission already':
            studentsList[x].x1+=1
            studentsList[x].y1+=0
        if studentsList[x].q8=='Work on in another week - there was a lot of room for improvement':
            studentsList[x].x1+=(-1)
            studentsList[x].y1+=0
        if studentsList[x].q8=='Maybe will add some final touches , but not too much':
            studentsList[x].x1+=(-0.25)
            studentsList[x].y1+=0
        # if studentsList[x].q8=='I am an expert at spending 20h in the library but only 3h studying':
        #     studentsList[x].x1+=0.5
        #     studentsList[x].y1+=1
        # if studentsList[x].q8=='What does studying even mean?':
        #     studentsList[x].x1+=-1
        #     studentsList[x].y1+=0
        if studentsList[x].q9=='Not so good, a bit disappointed':
            studentsList[x].z1+=1
        if studentsList[x].q9=='Ok, will be better next time':
            studentsList[x].z1+=0
        if studentsList[x].q9=='Good, just have to go home and study a bit more':
            studentsList[x].z1+=-1
        if studentsList[x].q10=='I will have some, I am really hungry and will not have much':
            studentsList[x].z1+=0.5
        if studentsList[x].q10=='A promise is a promise, cannot have any':
            studentsList[x].z1+=-1
        if studentsList[x].q10=='I will take it, been eating chocolate for the past days already':
            studentsList[x].z1+=1
        else:
            studentsList[x].x1+=0
            studentsList[x].y1+=0
personalityScore()
        
def numberFreshers():
    j=0
    for x in range(len(studentsList)):
        if studentsList[x].q1=='New student':
            j+=1
    #print(j)
    return j

def numberMentors():
    #print()
    return (len(studentsList)-numberFreshers())

def freshersPerMentor():
    
    return numberFreshers()//numberMentors()

print('---')
print(len(studentsList))
print(numberFreshers())
print(numberMentors())
print('---')




GroupsDictionary = {}
MentorsKeys = list(GroupsDictionary.keys())
StudentsValues = list(GroupsDictionary.values())




def distance(p1,p2,x,y):
    return math.sqrt((p1[x].x1-p2[y].x1)**2+(p1[x].y1-p2[y].y1)**2 + (p1[x].z1-p1[y].z1)**2)

def isAllocationComplete():
    if len(studentsList) == 0:
        print('All' ,numberFreshers(),' freshers have been allocated')
    else:
        print((len(UnassignedFresherList)), 'students waiting to be allocated')

def stopNumber():
    k=numberFreshers()//numberMentors()
    x=(len(IMEEList)//len(IMEEMentorList))
    x1=(len(IMEEList)%len(IMEEMentorList))
    y=(len(RoboticsList)//len(RoboticsMentorList))
    y1=(len(RoboticsList)%len(RoboticsMentorList))
    z=(len(EEEList)//len(EEEMentorList))
    z1=(len(EEEList)%len(EEEMentorList))
    
    if x >= 1:
        if x> freshersPerMentor() :
            x=freshersPerMentor()*len(IMEEMentorList)
        else:
            x=x*len(IMEEMentorList)
    else: x = len(IMEEList)
    
    if y >= 1:
        if y> freshersPerMentor():
            y=freshersPerMentor()*len(RoboticsMentorList)
        else:
            y=y*len(RoboticsMentorList)
    else: y = len(RoboticsList)
    
    if z >= 1:
        if z> freshersPerMentor() :
            z=freshersPerMentor()*len(EEEMentorList)
        else:
            z=z*len(EEEMentorList)
    else: z = len(EEEList)
    r=x1+y1+z1
    #print(x1+y1+z1)
    #print(x + y + z + r + k)
    return (x + y + z + r +k)
stopNumber = stopNumber()


def ShowResults():
    y=0
    x=0
    z=0
    for x in range((len(list(GroupsDictionary.keys())))):
       print('Mentor', list(GroupsDictionary.keys())[x].name,'is from course', list(GroupsDictionary.keys())[x].q2, 'and has',(len(list(GroupsDictionary.values())[x])),'mentees')
       y=0
       while y < (len(list(GroupsDictionary.values())[x])):
          print('Mentee', list(GroupsDictionary.values())[x][y].name,'is from course',list(GroupsDictionary.values())[x][y].q2)
          #print('Mentee', list(GroupsDictionary.values())[x][y].name ,' from mentor' ,list(GroupsDictionary.keys())[x].name, 'got scores', list(GroupsDictionary.values())[x][y].x1,list(GroupsDictionary.values())[x][y].y1,list(GroupsDictionary.values())[x][y].z1,'is from course',list(GroupsDictionary.values())[x][y].q2)
          y=y+1
          z+=1
       
       #print('Mentor', list(GroupsDictionary.keys())[x].name,'from course',list(GroupsDictionary.keys())[x].q2, 'has', y , 'mentees')
       print('---------')
    if x == len(MentorList): print("All mentors responded")
    else: print('Missing', numberMentors() - (x+1) , 'mentors - assigned:', numberMentors())
    if z== numberFreshers(): print("All new students assigned - assigned:", )
    else: print('Missing', numberFreshers()-z, 'new students to be assigned')

def allocate(): 
    assignedStudents = 0
    #print('#1')
    #c1=c2=c3=False
    while assignedStudents < 96: # or (len(IMEEList)): 89!!!
    #while (c1 ==False and c2==False and c3==False) :#stopNumber or (len(IMEEList)):
            for x in range(len(MentorList)):
               #ShowResults()
                # print('#2')
                # print('unnassgined freshers :', len(UnassignedFresherList))
                # print('stop number is:', stopNumber)
                # print('number of assigned is :',assignedStudents)
                # print('imee list is:', len(IMEEList))               
                # print('robotics list is:',len(RoboticsList))
                # print('eee list is:',len(EEEList))
                # print('imee mentor list is:',len(IMEEMentorList))               
                # print('robotics mentor list is:',len(RoboticsMentorList))
                # print('eee mentor list is:',len(EEEMentorList))
                
                if MentorList[x].q2=='Integrated Mechanical and Electrical Engineering (IMEE)':
                    # if len(GroupsDictionary[(MentorList[x])]) == freshersPerMentor():
                    #      c1=True
                    #print('#3')
                    if  len(IMEEList)>0:
                        #print('#4')
                        d=100
                        selectedPos=0
                        for y in range (len(IMEEList)):
                            #print('#5')
                            distance = math.sqrt((MentorList[x].x1-IMEEList[y].x1)**2+(MentorList[x].y1-IMEEList[y].y1)**2 + (MentorList[x].z1-IMEEList[y].z1)**2)
                            if distance<d:
                                d=distance
                                selectedPos = y
                            else:
                                d=d
                        if MentorList[x] in GroupsDictionary.keys():
                            #print('#6')
                            if len(list(GroupsDictionary.values())[x]) <= freshersPerMentor():
                                GroupsDictionary[(MentorList[x])].append(IMEEList[selectedPos])
                                assignedStudents +=1
                            #print('SECOND KEY ENTRY')
                        else:
                            #print('#7')
                            #print('NEW KEY ENTRY')
                            GroupsDictionary[MentorList[x]]=[]
                            GroupsDictionary[(MentorList[x])].append(IMEEList[selectedPos])
                            assignedStudents +=1
                        UnassignedFresherList.remove(IMEEList[selectedPos])
                        IMEEList.pop(selectedPos)
                #print('#8')
                        
                        
                if MentorList[x].q2=='Robotics Engineering':
                    # if len(GroupsDictionary[(MentorList[x])]) == freshersPerMentor():
                    #     c2=True
                    #print('#9')
                    if  len(RoboticsList)>0:
                        #print('#10')
                        d=100
                        selectedPos=0
                        for y in range (len(RoboticsList)):
                            #print('#11')
                            distance = math.sqrt((MentorList[x].x1-RoboticsList[y].x1)**2+(MentorList[x].y1-RoboticsList[y].y1)**2 + (MentorList[x].z1-RoboticsList[y].z1)**2)
                            if distance<d:
                                d=distance
                                selectedPos = y
                            else:
                                d=d

                        if MentorList[x] in GroupsDictionary.keys():
                            #print('#12')
                            if len(list(GroupsDictionary.values())[x]) <= freshersPerMentor():
                                #print('#13')
                                GroupsDictionary[(MentorList[x])].append(RoboticsList[selectedPos])
                                assignedStudents +=1
                        else:
                            GroupsDictionary[MentorList[x]]=[]
                            GroupsDictionary[(MentorList[x])].append(RoboticsList[selectedPos])
                            assignedStudents +=1
                        UnassignedFresherList.remove(RoboticsList[selectedPos])
                        RoboticsList.pop(selectedPos) 
                if MentorList[x].q2=='Electrical and Electronic Engineering (EEE)':
                    # if len(GroupsDictionary[(MentorList[x])]) == freshersPerMentor():
                    #     c3=True
                    #print('#14')
                    if  len(EEEList)>0:
                        #print('#15')
                        d=100
                        selectedPos=0
                        for y in range (len(EEEList)):
                            #print('#16')
                            distance = math.sqrt((MentorList[x].x1-EEEList[y].x1)**2+(MentorList[x].y1-EEEList[y].y1)**2 +(MentorList[x].z1-EEEList[y].z1)**2)
                            if distance<d:
                                d=distance
                                selectedPos = y
                            else:
                                d=d
                        if MentorList[x] in GroupsDictionary.keys():
                            #print('#17')
                            if len(list(GroupsDictionary.values())[x]) <= freshersPerMentor():
                                GroupsDictionary[(MentorList[x])].append(EEEList[selectedPos])
                                assignedStudents +=1
                        else:
                            #print('#18')
                            GroupsDictionary[MentorList[x]]=[]
                            GroupsDictionary[(MentorList[x])].append(EEEList[selectedPos])
                            assignedStudents +=1
                        UnassignedFresherList.remove(EEEList[selectedPos])
                        EEEList.pop(selectedPos)
                    
                    
def getEmailingLists():
    y=0
    x=0
    for x in range((len(list(GroupsDictionary.keys())))):
        a=""
        if list(GroupsDictionary.keys())[x].q2 == "Integrated Mechanical and Electrical Engineering (IMEE)":
            a="IMEE"
        if list(GroupsDictionary.keys())[x].q2 == "Robotics Engineering":
            a="REng"
        if list(GroupsDictionary.keys())[x].q2 == "Electrical and Electronic Engineering (EEE)":
            a="EEE"
            
        print('Mentor:',list(GroupsDictionary.keys())[x].name,'-',a,'/ email:', list(GroupsDictionary.keys())[x].email ) 
        y=0
        while y < (len(list(GroupsDictionary.values())[x])):
            b=""
            if list(GroupsDictionary.values())[x][y].q2 == "Integrated Mechanical and Electrical Engineering (IMEE)":
                b="IMEE"
            if list(GroupsDictionary.values())[x][y].q2 == "Robotics Engineering":
                b="REng"
            if list(GroupsDictionary.values())[x][y].q2 == "Electrical and Electronic Engineering (EEE)":
                b="EEE"           
            
            print('New student:',list(GroupsDictionary.values())[x][y].name,'-',b, '/ email:',list(GroupsDictionary.values())[x][y].email )
            y=y+1
        print('---------')
    

def finalAllocation():
    while (len(UnassignedFresherList) >0): 
        c=1000
        k=0
        for x in range(len(MentorList)):  
            if len(GroupsDictionary[(MentorList[x])])<c:
                c=len(GroupsDictionary[(MentorList[x])])
                k=x
            else:
                k=k
        selectedPos=0
        d=100
        if (len(UnassignedFresherList)>0):
            for y in range(len(UnassignedFresherList)):
                distance = math.sqrt((MentorList[k].x1-UnassignedFresherList[y].x1)**2+(MentorList[k].y1-UnassignedFresherList[y].y1)**2 +(MentorList[k].z1-UnassignedFresherList[y].z1)**2)
                if distance<d:
                    d=distance
                    selectedPos = y
                else:
                    d=d
            GroupsDictionary[(MentorList[k])].append(UnassignedFresherList[selectedPos])
            UnassignedFresherList.pop(selectedPos)



allocate()  
finalAllocation()
ShowResults()
getEmailingLists()








