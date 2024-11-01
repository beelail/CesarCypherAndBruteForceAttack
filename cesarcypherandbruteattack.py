#import stopwords list 
from nltk.corpus import stopwords
# define all statistic in language francais
letterfrequency={'a':9.42,'b':1.02,'c':2.64,'d':3.39,'e':15.87,'f':0.95,'g':1.04,'h':0.77,'i':8.41,'j':0.98,'k':0.00,'l':5.34,'m':3.24,'n':7.15,'o':5.14,'p':2.86,'q':1.06,'r':6.46,'s':7.90,'t':7.26,'u':6.24,'v':2.15,'w':0.00,'x':.30,'y':0.24,'z':0.32}
conbinationfrequency={"es":3318,"de":2409,"le":2366,"en":2121,"re":1885,"nt":1964,"on":1646,"er":1514,"te":1484,"el":1382,"an":1372,"se":1377,"et":1307,"la":1270,"ai":1255,"it":1243,"me":1099,"ou":1086,"em":1056,"ie":1030,"ent":900,"les":801,"ede":630,"des":609,"que":607,"alt":542,"lle":509,"sde":508,"ion":477,"eme":472,"ela":437,"res":432,"men":425,"ese":416,"del":404,"ant":397,"tio":383,"par":360,"esd":351,"tde":350}

def extract(filename):
    special="(){}§!?%&*¨'""^£$#:;-_." # define all special caracteres
    clean=""
    with open (filename+".txt", "r") as f1:
        p=f1.read().split() # open file and split phrase into word in list 
    listmotclean=[word for word in p if word not in stopwords.words('french')] # test every word and remove all stop words
    # test every letter and remove special caracteres
    for i in listmotclean:
        for j in i :
            if j in special:
                continue
            clean+=j
        clean+=" "    
    return clean # retrun the the clean phrase
            
# use cesar encrytion 
def cesarencryption(plaintext):
    cyphertext=""
    dep=65
    for i in plaintext:
        if i==" ":
           cyphertext+=" "
           continue
        if "a"<=i<="z":
            dep=97
        x2=(chr((((ord(i)-dep)+3)%26)+dep)) # use cesar methode to replace with the letters that comes after the orignal letters with 3 position 
        cyphertext+=x2
    return cyphertext # retrun the  encrypted phrase

# test all possible decryption resultes
def cesarebruteforce(cyphertext):
    dep=65
    listpossiblephrases=[]
    for k in range(1,26): # for to try every key 
        possiblephrase=""
        for i in cyphertext:
            if i==" ":
                possiblephrase+=" "
                continue
            if "a"<=i<="z":
                dep=97
            x2=(chr((((ord(i)-dep)-k)%26)+dep)) # reverse cesar encrytion
            possiblephrase+=x2
        listpossiblephrases.append(possiblephrase+"\n")
        # write all possible phrases in file 
        with open("possiblephrase.txt","w") as f:
            f.writelines(listpossiblephrases)
# using statistic try to find optimal result
def findrightphrase():
    listpossiblephrasesscore={}
    with open ("possiblephrase.txt","r") as f:
       possiblephrases=f.readlines()   # put possible phrases in list 
       
    for i in possiblephrases:
        phrasescore=0
        for j in conbinationfrequency:
            if j in i :
                phrasescore+=conbinationfrequency[j]   # add score of every conbination to phrase score if cobination find in phrase
        for j in letterfrequency:
            if j in i:
                phrasescore+=letterfrequency[j] 
        listpossiblephrasesscore[i]=phrasescore # append to dic ever phrase and its score
    return (sorted(listpossiblephrasesscore.items(),key=lambda x:x[1],reverse=True)) #  return sort phrases using score of every phrase 



with open ("t.txt", "r") as f1:
        print("the original phrase  :"+f1.read()) 
cleanphrase=extract("t") #extract phrase from file t.tx and remove all stop words and sepcial caracteres
print("clean phrase : "+cleanphrase) 
cyphertext=cesarencryption(cleanphrase) # encrypt the found phrase using cesar encryption methode
print("cypher text : " +cyphertext)    
cesarebruteforce(cyphertext) # using all possible key to decrypt the encryption
bestdecipher=findrightphrase() # calculate and find the best and more optimal decryption in the possiblephrase file
print("best decipher : " ,bestdecipher[0]) # print the optimal decryption