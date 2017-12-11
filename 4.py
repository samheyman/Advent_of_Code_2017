result = 0
div = 0 
count = 0
sentances = 0
line = 1  
phrase_good = 0
anagram = False
text = open('passphrases.txt','r')
content = text.readlines()

def isAnagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()

    return (str1_list == str2_list)

#First step
# for sentance in content:
#     sentances += 1
#     sentance = sentance[:-1]
#     words = sentance.split(' ')
#     repeat_word = False

#     for word in words:
#         if words.count(word) > 1:
#             print("Line {}, multiple occurance of: {}".format(line, word))
#             count += 1
#             break
#     line += 1

#Second step
for sentance in content:
    sentances += 1
    sentance = sentance[:-1]
    words = sentance.split(' ')
    print("Sentence {}".format(line))
    
    for word in words:
        if words.count(word) > 1:   
            anagram = True
            print("- Same word: {}".format(word))
        else:
            if not anagram:
                for i in range(1,len(words)):                
                    if (word != words[i]) and isAnagram(word, words[i]):
                        anagram = True
                        print("- Anagram #{}: {} and {}".format(count, word, words[i]))
                        count += 1   
    if not anagram:
        phrase_good += 1     
    line += 1
    anagram = False
    print("Number of valid sentances: {}".format(phrase_good))

print("Number of valid phrases: {} ({} sentances and {} invalid)".format(sentances - phrase_good, sentances, phrase_good))
