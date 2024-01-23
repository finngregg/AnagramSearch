def split(word):
    dict = {}
    for i in range(len(word)):
        if word[i] in dict:
            dict[word[i]]+=1        
        else: dict[word[i]]=1
    return dict

def main():
    print("***** Anagram Finder *****")
    try:
        f = open('EnglishWords.txt', 'r')
        lines = f.readlines()
        f.close()        
        
        search = input("Enter a word: ")
        for n in range(len(lines)):
            lines[n] = lines[n].strip("\n")
        lines = lines[60:]
        out = []
        for n in range(len(lines)):
            out.append(lines[n])

        anagrams = []
        s = split(search)
        
        for i in out:
            k = split(i)
            if s==k and i!=search:
                anagrams.append(i)        
        anagrams = sorted(anagrams)
        if len(anagrams)!=0:  
            print(anagrams)   
        else:
            if len(search)==0 or search=="NULL":
                print("Sorry, could not find file 'EnglishWords.txt'.")        
            else:
                print("Sorry, anagrams of '"+search+"' could not be found.")
    except IOError:
        print("Sorry, could not find file 'EnglishWords.txt'.")
main()        

