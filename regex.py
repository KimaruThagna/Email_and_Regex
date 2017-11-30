import re
import urllib.request
string="Michael is my M 30 year old son and lives with his wife Jess who is 25 years old.They have a joint account worth $125000"
ages=re.findall(r'\d{1,3}',string)
names=re.findall(r'[A-Z][a-z]*',string) # looking for strings with a beginning capital letter
#followed by 0 or more small letters
print(ages,names)
print(re.findall(r'[$]\d*',string))
# use of iterator This finds the first and last index of the occurence of the string we
#are looking for eg, this prints the first and last indices of occurrences of inform
str="We need to inform him about the latest received information"
for i in re.finditer("inform",str):
    print(i.span())
print(str[11:17])
# s="sat,hat,mat,pat"
# print(re.findall(r'[^h-m]at',s)) this prints anything outside the given range thus, sat and pat
#REPLACE A STRING
items="rome persia greece beijing berlin"
out=re.compile("beijing") #item to be replaced
items=out.sub("Nairobi",items) #new string
print(items)
# phone number verification
num="+254726700973,254705410,0726784166,07234119"
re1="[07]\d{9}"
re2="[+2547]\d{12}"
kenyan_phone_num=re.findall(r"(%s|%s)"%(re1,re2),num)
if(kenyan_phone_num):
    print(kenyan_phone_num)
# email verification
emails="sk@gmail.com @gmail.com custom@comp.co.ke dc@.com kk2b@g.com "
print(re.findall(r'[\w.%+-]{1,20}@[A-Za-z]{2,20}.[A-Za-z]{2,3}| [\w.%+-]{1,20}@[A-Za-z]{2,20}.[A-Za-z]{2,3}.[A-Za-z]{2}',emails))
#simple web parsing
url="http://www.summet.com/dmsi/html/codesamples/addresses.html"
response=urllib.request.urlopen(url)
html=response.read()
html_str=html.decode()
phone_data=re.findall(r'\(\d{3}\) \d{3}-\d{4}',html_str)
# the brackets are preceeded by back-slashes for escaping them. ie, they arent special
#characters but part of the pattern
for i in phone_data:
    print(i)
# from a file
text=open('poem.txt')
for line in text:
    line=line.rstrip()# to remove the newline character(\n)
    if re.search(r'[A-Z]{8,}',line):
        print(line)

s='127.0.0.1/blog 748596/blog/hello'
print(re.findall(r'blog[^\s]',s)) # if the carrat sign is included in the range brackets,
# the regex looks for anything apart from what is specified in the regex
# when used outside the range, it means 'match the beggining of a line'
#eg, only give me words that dont start with capital letters.
#^[^A_Z]