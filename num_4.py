
import urllib.request

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
Nothing = urllib.request.urlopen(url + "8022") # we have started at 12345 but you know the devil
for i in range(85,401):
    temp = str(Nothing.read())
    none = "and the next nothing is " 
    Nothing = urllib.request.urlopen(url + str(temp[temp.find(none,0, len(temp)) + len(none):]))
    print (i,temp)
    




