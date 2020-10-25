import os

if os.path.exists('map.txt'):
    os.remove('map.txt')

new_story = open("map.txt","w+")

story = open('../text.txt', 'r')
for x in story:
    for c in x:
        new_story.write(str(ord(c))+",")
    new_story.write("/n")

story.close()
new_story.close()

