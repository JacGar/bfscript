from lxml import html
import requests


def next(letter):
    if letter is 'A':
        return 'B'
    if letter is 'B':
        return 'C'
    if letter is 'C':
        return 'D'
    if letter is 'D':
        return 'E'
    if letter is 'E':
        return 'F'
    if letter is 'F':
        return 'A'



url = 'http://s3-eu-west-1.amazonaws.com/puzzleinabucket/'

letter1='F'
letter2='F'
letter3='F'
letter4='F'
letter5='F'
letter6='F'

list=[]

for x in range(0,6):
    letter1=next(letter1)
    for x in range(0,6):
        letter2=next(letter2)
        for x in range(0,6):
            letter3=next(letter3)
            for x in range(0,6):
                letter4=next(letter4)
                for x in range(0,6):
                    letter5=next(letter5)
                    for x in range(0,6):
                        letter6=next(letter6)
                        string = letter1+letter2+letter3+letter4+letter5+letter6
                        list.append(string)
                        






i=1
for item in list:
    print str(i)+" of "+str(len(list))
    page = requests.get(url+item+'.html')
    print page.url
    tree = html.fromstring(page.content)
    text=tree.xpath('//*[@id="ctl00_PlaceHolderMain_ctl01__ControlWrapper_RichHtmlField"]/p[3]/strong/text()[1]')
    string2comp='Sorry - you did not get all the questions correct. Please '
    if text[0]!=string2comp:
        print "This is the one: "+page.url
        break
    i+=1
    



