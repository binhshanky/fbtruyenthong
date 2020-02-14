import requests
import os
clear = lambda: os.system('clear')
def delete(id, access_token):
    result = requests.delete('https://graph.facebook.com/' + str(id) + '?access_token='+access_token)
    
def getComment(meid, id, after, access_token):
    if(after == '1'):
        after = ''
    result = requests.get('https://graph.facebook.com/'+str(meid)+ "_" + str(id) + '/comments?limit=100&after='+after+'&access_token='+access_token)
    return result.json()
def fbget(param, access_token):
    result = requests.get('https://graph.facebook.com/'+ str(param) + '?access_token='+access_token)
    return result.json()
def checkResult(comments):
    backlist = ['Test page']
    # EDIT THEO CU PAGE ['TEN NGUOI CAN XOA', 'NGUYEN VAN A', 'NGUYEN VAN B']
    for i in backlist:
        if(i in comments):
            return True
    return False
print('Nhap Access Token User: ')
usertoken = input()
print('Nhap ID Page: ')
idpage = input()
user = fbget('me/accounts', usertoken)
user = user['data']
accToken = ''
for j in user:
    if(j['id'] == idpage):
        accToken = j['access_token']
        break

if(accToken == ''):
    clear()
    print('Khong tim thay Page nay !')
    exit()
clear()
print('Dang xu ly')

me = fbget('me', accToken)
meid = me['id']
clear()
print('Nhap bai viet')
idbv = input()
clear()
next = "1"
while(next != ""):
    comments = getComment(meid, idbv, next, accToken)
    dulieu = comments['data']
    n = len(comments['data'])
    if('paging' not in comments):
        print('Delete complete')
        break

    if('next' in comments['paging']):
        next = comments['paging']['cursors']['after']
    else:
        next = ""

        
    for i in range(n):
        if(checkResult(dulieu[i]['from']['name'])):
            delete('{}_{}'.format(idbv, dulieu[i]['id']), accToken)
            print('[{}_{}] Nội dung:'.format(idbv, dulieu[i]['id']))
            #print('-------')
            print(dulieu[i]['message'])
            #print('-------')
            print('============')
