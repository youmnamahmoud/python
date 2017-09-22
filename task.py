import csv
while True:
    name = input('Enter your name: ')
    if name == 'STOP':
        break
    email = input('Enter your email: ')
    if email == 'STOP':
        break
    mobile = input('Enter your mobile: ')
    if mobile == 'STOP':
        break
    university = input('Enter your university: ')
    if university == 'STOP':
        break
    major = input('Enter your major: ')
    if major == 'STOP':
        break
    myDict = {'NAME': name, 'EMAIL': email, 'MOBILE': mobile, 'UNIVERSITY': university, 'MAJOR': major}
    with open('test.csv', 'wb') as f:
        w = csv.writer(f)
        w.writerow(myDict.keys())
        w.writerow(myDict.values())
