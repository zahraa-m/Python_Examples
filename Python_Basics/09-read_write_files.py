#read the song Bohemian Rhapsody by Queen
song=open('Bohemian_Rhapsody-Queen.txt', "r")
print(song.read())
song.close()


#open file by With
with open('Bohemian_Rhapsody-Queen.txt', "r") as song1:

    for n in range(4):
        lyrics = song1.readline()
        print(lyrics)




#write your name into a text file
test=open('writing_test.txt','w')
test.write("Hi, my name is Zozo")
test=open('writing_test.txt','r')
print(test.read())
test.close()

