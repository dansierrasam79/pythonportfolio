# Welcome to the Lumos Coding Quest
# you have been given a linked list with duplicate values
# upon running this code, you will see a string that has been formed by collecting the data in the nodes of the linked list
# you need to complete the "MyAnswer" function and ensure that it removes the duplicate nodes from the linkedlist
# when you collate the string that this new linked list contains, you will get the link to the whitelist form
# Note:- "list" represents the said linked list

# Please dont edit anything in this file.
class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self, *args):
      self.headval = None

   def listprint(self):
      printval = self.headval
      answer = ""
      while printval is not None:
         answer += printval.dataval
         printval = printval.nextval
      print(answer)

def duplicatesCheck(aList):
   addList = []
   delList = []
   delDict = {}
   finalList = []
   last =[]
   for i in range(0,len(aList)):
      index = -1
      for j in range(0,len(aList)):
         index += 1
         if aList[i] == aList[j]:
            delList.append(index)
      delDict[aList[i]] = delList
      delList = []

   for k,v in delDict.items():
      for i in range(0, len(v)):
         if i != 0 and len(v) > 1:
            finalList.append(v[i])

   last = sorted(finalList)
   return last
   
def removeLinkedListNode(self, position):
   if self.headval is None:
            return
   index = 0
   current = self.headval
   while current.nextval and index < position:
      previous = current
      current = current.nextval
      index += 1
   if index < position:
      print("\nIndex is out of range.")
   elif index == 0:
      self.headval = self.headval.nextval
   else:
      previous.nextval = current.nextval
      # current = None #Optional statement

def firsttime(self):
   myList = []
   answer = ""
   myVal = self.headval
   while myVal is not None:
      if myVal.dataval not in myList:
         myList.append(myVal.dataval)
         answer += myVal.dataval
      myVal = myVal.nextval
   return answer

def MyAnswer(mylinkdlist):
   aList = []
   aList.append(mylinkdlist.headval.dataval)
   aList.append(e1.dataval)
   aList.append(e2.dataval)
   aList.append(e3.dataval)
   aList.append(e4.dataval)
   aList.append(e5.dataval)
   aList.append(e6.dataval)
   aList.append(e7.dataval)
   aList.append(e8.dataval)
   aList.append(e9.dataval)
   aList.append(e10.dataval)
   aList.append(e11.dataval)
   aList.append(e12.dataval)
   aList.append(e13.dataval)
   aList.append(e14.dataval)
   aList.append(e15.dataval)
   aList.append(e16.dataval)
   aList.append(e17.dataval)
   aList.append(e18.dataval)
   aList.append(e19.dataval)
   aList.append(e20.dataval)
   aList.append(e21.dataval)
   aList.append(e22.dataval)
   aList.append(e23.dataval)
   aList.append(e24.dataval)
   aList.append(e25.dataval)
   aList.append(e26.dataval)
   aList.append(e27.dataval)
   aList.append(e28.dataval)
   aList.append(e29.dataval)
   aList.append(e30.dataval)
   aList.append(e31.dataval)
   aList.append(e32.dataval)
   aList.append(e33.dataval)
   aList.append(e34.dataval)
   aList.append(e35.dataval)
   aList.append(e36.dataval)
   aList.append(e37.dataval)
   aList.append(e38.dataval)
   aList.append(e39.dataval)
   aList.append(e40.dataval)
   aList.append(e41.dataval)
   aList.append(e42.dataval)
   aList.append(e43.dataval)
   aList.append(e44.dataval)
   aList.append(e45.dataval)
   aList.append(e46.dataval)
   aList.append(e47.dataval)
   aList.append(e48.dataval)
   aList.append(e49.dataval)
   aList.append(e50.dataval)
   aList.append(e51.dataval)
   aList.append(e52.dataval)
   aList.append(e53.dataval)
   aList.append(e54.dataval)
   aList.append(e55.dataval)
   aList.append(e56.dataval)
   aList.append(e57.dataval)
   aList.append(e58.dataval)
   aList.append(e59.dataval)
   aList.append(e60.dataval)
   indexValues = duplicatesCheck(aList)
   # Associate firsttime method with the SLinkedList class
   SLinkedList.firsttime = firsttime
   # Associate removeLinkedListNode with the SLinkedList class
   SLinkedList.removeLinkedListNode = removeLinkedListNode
   # remove linked list based on duplicate indices found
   for i in range(0, len(indexValues)):
      mylinkdlist.removeLinkedListNode(indexValues[i]-i)
   #Initialize myanswer to a string of 0 length
   myanswer = ""
   mylinkdlist.listprint()
   #call the firsttime method on mylinkdlist to eliminate duplicates
   myanswer = mylinkdlist.firsttime()
   #Display the Lumos Metaverse hyperlink
   # Expected output -> https://forms.lumoslabs.co/survey/t/65a5a0c3-15b9-42da-a99c-06622e0c7bac/r/o
   print(myanswer)

#Call the MyAnswer function with the created linkdlist with 60 nodes
linkdlist = SLinkedList()
linkdlist.headval = Node("ht")
e1 = Node("ht")
e2 = Node("tps:")
e3 = Node("//")
e4 = Node("for")
e5 = Node("tps:")
e6 = Node("ms")
e7 = Node(".")
e8 = Node("for")
e9 = Node("lumos")
e10 = Node("//")
e11 = Node("ht")
e12 = Node("labs.")
e13 = Node("ms")
e14 = Node("co")
e15 = Node("/su")
e16 = Node("rvey")
e17 = Node("for")
e18 = Node("/")
e19 = Node("labs.")
e20 = Node("t/")
e21 = Node("65a5a0c3")
e22 = Node("-15b9")
e23 = Node("-42")
e24 = Node("65a5a0c3")
e25 = Node("da")
e26 = Node("-a99c")
e27 = Node("-")
e28 = Node("06622")
e29 = Node("e0c7")
e30 = Node("bac/")
e31 = Node("r/")
e32 = Node("o")
e33 = Node("//")
e34 = Node("/su")
e35 = Node("labs.")
e36 = Node("ms")
e37 = Node("bac/")
e38 = Node("/su")
e39 = Node(".")
e40 = Node("65a5a0c3")
e41 = Node("rvey")
e42 = Node("-15b9")
e43 = Node("bac/")
e44 = Node("lumos")
e45 = Node("-42")
e46 = Node("bac/")
e47 = Node("-")
e48 = Node("bac/")
e49 = Node("rvey")
e50 = Node("r/")
e51 = Node("o")
e52 = Node(".")
e53 = Node("for")
e54 = Node("-15b9")
e55 = Node("-a99c")
e56 = Node("bac/")
e57 = Node("t/")
e58 = Node("lumos")
e59 = Node("da")
e60 = Node("da")
# Link first Node to second node
linkdlist.headval.nextval = e1
# Link second Node to third node
e1.nextval = e2
# Link third Node to fourth node
e2.nextval = e3
e3.nextval = e4
# Link fourth Node to fifth node
e4.nextval = e5
# Link fifth Node to sixth node
e5.nextval = e6
# Link sixth Node to seventh node
e6.nextval = e7
e7.nextval = e8
e8.nextval = e9
e9.nextval = e10
e10.nextval = e11
e11.nextval = e12
e12.nextval = e13
e13.nextval = e14
e14.nextval = e15
e15.nextval = e16
e16.nextval = e17
e17.nextval = e18
e18.nextval = e19
e19.nextval = e20
e20.nextval = e21
e21.nextval = e22
e22.nextval = e23
e23.nextval = e24
e24.nextval = e25
e25.nextval = e26
e26.nextval = e27
e27.nextval = e28
e28.nextval = e29
e29.nextval = e30
e30.nextval = e31
e31.nextval = e32
e32.nextval = e33
e33.nextval = e34
e34.nextval = e35
e35.nextval = e36
e36.nextval = e37
e37.nextval = e38
e38.nextval = e39
e39.nextval = e40
e40.nextval = e41
e41.nextval = e42
e42.nextval = e43
e43.nextval = e44
e44.nextval = e45
e45.nextval = e46
e46.nextval = e47
e47.nextval = e48
e48.nextval = e49
e49.nextval = e50
e50.nextval = e51
e51.nextval = e52
e52.nextval = e53
e53.nextval = e54
e54.nextval = e55
e55.nextval = e56
e56.nextval = e57
e57.nextval = e58
e58.nextval = e59
e59.nextval = e60
print("This is what the unsolved quest looks like: \n")
linkdlist.listprint()
print("\n")
print("Hurray! I was able to solve the quest - here is my output: \n")
MyAnswer(linkdlist)
