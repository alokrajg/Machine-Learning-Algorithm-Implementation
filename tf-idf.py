docA = 'Now you are just the somebody that I used to know'
docB = 'I want you to be more than just somebody that I used to know'

all_word = set(docA.split()).union(set(docB.split()))
print(all_word)

worddictA = dict.fromkeys(all_word, 0)
worddictB = dict.fromkeys(all_word, 0)

for word in docA.split():
    worddictA[word] +=1
    
for word in docB.split():
    worddictB[word] +=1
    
worddict_df = pd.DataFrame([worddictA, worddictB])
print(worddict_df)

def computeTF(worddict, bow):
    tfdict = {}
    bowcount = len(bow)
    for word, count in worddict.items():
        tfdict[word] = count/float(bowcount)
    return tfdict
  
tfA = computeTF(worddictA, docA.split())
tfB = computeTF(worddictB, docB.split())

def computeIDF(doclist):
    import math
    idfdict = {}
    N = len(doclist)
    
    idfdict = dict.fromkeys(doclist[0].keys(), 0)
    for doc in doclist:
        for word, val in doc.items():
            if val>0:
                idfdict[word] +=1
                
    for word, val in idfdict.items():
        idfdict[word] = math.log10(N/float(val))
        
    return idfdict
  
idfs = computeIDF([worddictA, worddictB])
  
def computeTFIDF(tf, idf):
    tfidf = {}
    for word, val in tf.items():
        tfidf[word] = val*idf[word]
    return tfidf
  
tfidfA = computeTFIDF(tfA, idfs)
tfidfB = computeTFIDF(tfB, idfs)

pd.DataFrame([tfidfA, tfidfB])
