import os


new_story = open('venv/map.txt', "r")
array = new_story.read().split("/n")
print(len(array))
story = ""
for line in array:
    linearray = line.split(",")
    for c in linearray:
        if c != "":
            story += chr(int(c))

#print(story)
array2 = story.splitlines()
iemptyline = []
linenumber = 0
for line in array2:
    if line == "":
        if 96< linenumber < 123:
            iemptyline.append(linenumber)
    linenumber+=1

#sort array from big to small
iemptyline = sorted(iemptyline, reverse=True)

#remove the first item
iemptyline.pop(0)

#move the first item to the last place
iemptyline.append(iemptyline[0])
iemptyline.pop(0)

#move 4 item from the end to the 2 place
iemptyline.insert(1,iemptyline[len(iemptyline)-4])
iemptyline.pop(len(iemptyline)-4)

#move 3 item to last
iemptyline.append(iemptyline[2])
iemptyline.pop(2)

#move 4 item from the last ot the 4 place
iemptyline.insert(3,iemptyline[len(iemptyline)-4])
iemptyline.pop(len(iemptyline)-4)

#replace item 5 & 7

iemptyline.insert(5,iemptyline[7])
iemptyline.insert(8,iemptyline[6])
iemptyline.pop(9)
iemptyline.pop(6)

#insert value 32 to index 5,8

iemptyline.insert(4,32)
iemptyline.insert(9,32)

#add index 58 to the end

iemptyline.append(58)

#copy the first 3 items to the end to the array
iemptyline.append(iemptyline[0])
iemptyline.append(iemptyline[1])
iemptyline.append(iemptyline[2])

#add all items from row[sum of iemptyline] to the end of the array

iemptyline.extend(array[sum(iemptyline)].split(","))


#convert number in arrray to char and add to string

story = ""
for x in iemptyline:
    if x != "":
        story += chr(int(x))


#print the answer and to the job



print(iemptyline)
print(story)

new_story.close()


