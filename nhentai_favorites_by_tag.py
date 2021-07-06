from hentai import Hentai, Format
import pickle

from_doujin = 0 #doujin to start at

to_doujin = 0   #doujin to finish at

file = "tagsfavorites"
favourites = 0
tag = ""

try:
    saved_file = open(file,"rb")
    tagdictionary = pickle.load(saved_file)
    saved_file.close()

except:
    tagdictionary = {
    }

for i in range(from_doujin,to_doujin):
    try:
        
        doujin = Hentai(i)
        favourites = doujin.num_favorites
        
        for tagdata in doujin.tag:
            tag = tagdata.name
            
            try:
                tagdictionary.get(tag)
                tagdictionary[tag] = tagdictionary[tag] + favourites
                
            except:
                tagdictionary[tag] = favourites
    except:
        pass

saved_file = open(file,"wb")
pickle.dump(tagdictionary,saved_file)
saved_file.close()

print(tagdictionary)
