import requests, os, json
from time import sleep
from datetime import datetime
cccc=0
while True:
  phut = datetime.now()
  m = phut.minute
  h = phut.hour
  if m % 2 == 0 and cccc == 0 :
    cccc=1
    sleep(5)
    os.system('clear')
    print(f'\r{h} : {m}')
    for concec in range(5):
      if concec == 0:
        cc = requests.get('https://api.im2018.com/api/game/guess_odd?page=1&limit=31&type=24').text
        ccc = json.loads(cc)
        kq = [entry['result'] for entry in ccc['data']]
        print('\n-------------------\n'+str(kq[0])+'\n\n'+str(kq[29])+'\n'+str(kq[30]))
        print('-------------------\nCầu: ',end='')
        dau = [int(char) for char in kq[0] if char.isdigit()]
        cuoi = [int(char) for char in kq[30] if char.isdigit()]
        if dau > cuoi:
          if 'odd' in kq[29]:
            print('Even')
            c = 'Even'
          else:
            print('Odd')
            c = 'Odd'
        if dau < cuoi:
          if 'odd' in kq[29]:
            print('Odd')
            c = 'Odd'
          else:
            print('Even')
            c = 'Even'
        if dau == cuoi:
          print('2 cái = nhau skip')
      if concec == 1:
        cc = requests.get('https://api.im2018.com/api/game/guess_odd?page=1&limit=61&type=24').text
        ccc = json.loads(cc)
        kq = [entry['result'] for entry in ccc['data']]
        print('\n-------------------\n'+str(kq[0])+'\n\n'+str(kq[59])+'\n'+str(kq[60]))
        print('-------------------\nCầu: ',end='')
        dau = [int(char) for char in kq[0] if char.isdigit()]
        cuoi = [int(char) for char in kq[60] if char.isdigit()]
        if dau > cuoi:
          if 'odd' in kq[59]:
            print('Even')
            c = 'Even'
          else:
            print('Odd')
            c = 'Odd'
        if dau < cuoi:
          if 'odd' in kq[59]:
            print('Odd')
            c = 'Odd'
          else:
            print('Even')
            c = 'Even'
        if dau == cuoi:
          print('2 cái = nhau skip')
      if concec == 2:
        cc = requests.get('https://api.im2018.com/api/game/guess_odd?page=1&limit=91&type=24').text
        ccc = json.loads(cc)
        kq = [entry['result'] for entry in ccc['data']]
        print('\n-------------------\n'+str(kq[0])+'\n\n'+str(kq[89])+'\n'+str(kq[90]))
        print('-------------------\nCầu: ',end='')
        dau = [int(char) for char in kq[0] if char.isdigit()]
        cuoi = [int(char) for char in kq[90] if char.isdigit()]
        if dau > cuoi:
          if 'odd' in kq[89]:
            print('Even')
            c = 'Even'
          else:
            print('Odd')
            c = 'Odd'
        if dau < cuoi:
          if 'odd' in kq[89]:
            print('Odd')
            c = 'Odd'
          else:
            print('Even')
            c = 'Even'
        if dau == cuoi:
          print('2 cái = nhau skip')
          c = skip
      if concec == 3:
        cc = requests.get('https://api.im2018.com/api/game/guess_odd?page=1&limit=121&type=24').text
        ccc = json.loads(cc)
        kq = [entry['result'] for entry in ccc['data']]
        print('\n-------------------\n'+str(kq[0])+'\n\n'+str(kq[119])+'\n'+str(kq[120]))
        print('-------------------\nCầu: ',end='')
        dau = [int(char) for char in kq[0] if char.isdigit()]
        cuoi = [int(char) for char in kq[120] if char.isdigit()]
        if dau > cuoi:
          if 'odd' in kq[119]:
            print('Even')
            c = 'Even'
          else:
            print('Odd')
            c = 'Odd'
        if dau < cuoi:
          if 'odd' in kq[119]:
            print('Odd')
            c = 'Odd'
          else:
            print('Even')
            c = 'Even'
        if dau == cuoi:
          print('2 cái = nhau skip')
      if concec == 4:
        cc = requests.get('https://api.im2018.com/api/game/guess_odd?page=1&limit=151&type=24').text
        ccc = json.loads(cc)
        kq = [entry['result'] for entry in ccc['data']]
        print('\n-------------------\n'+str(kq[0])+'\n\n'+str(kq[149])+'\n'+str(kq[150]))
        print('-------------------\nCầu: ',end='')
        dau = [int(char) for char in kq[0] if char.isdigit()]
        cuoi = [int(char) for char in kq[150] if char.isdigit()]
        if dau > cuoi:
          if 'odd' in kq[149]:
            print('Even')
            c = 'Even'
          else:
            print('Odd')
            c = 'Odd'
        if dau < cuoi:
          if 'odd' in kq[149]:
            print('Odd')
            c = 'Odd'
          else:
            print('Even')
            c = 'Even'
        if dau == cuoi:
          print('2 cái = nhau skip')
      if concec == 0:
        try:  
          print('Cầu trước:',truoc,end='')
          if truoc in kq[0]:
            print(' (win)')
          elif truoc == 'skip':
            print(' (skip)')
          else:
            print(' (lose)')
        except:
          pass
        truoc = c
      if concec == 1:
        try:  
          print('Cầu trước:',truocc,end='')
          if truocc in kq[0]:
            print(' (win)')
          elif truocc == 'skip':
            print(' (skip)')
          else:
            print(' (lose)')
        except:
          pass
        truocc = c
      if concec == 2:
        try:  
          print('Cầu trước:',truoccc,end='')
          if truoccc in kq[0]:
            print(' (win)')
          elif truoccc == 'skip':
            print(' (skip)')
          else:
            print(' (lose)')
        except:
          pass
        truoccc = c
      if concec == 3:
        try:  
          print('Cầu trước:',truocccc,end='')
          if truocccc in kq[0]:
            print(' (win)')
          elif truocccc == 'skip':
            print(' (skip)')
          else:
            print(' (lose)')
        except:
          pass
        truocccc = c
      if concec == 4:
        try:  
          print('Cầu trước:',truoccccc,end='')
          if truoccccc in kq[0]:
            print(' (win)')
          elif truoccccc == 'skip':
            print(' (skip)')
          else:
            print(' (lose)')
        except:
          pass
        truoccccc = c
  if m % 2 != 0:
    cccc=0