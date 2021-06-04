import requests, os

def lineNotifyMessage(token, msg, pic):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token,
        #"Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {
        'message': msg,
        'stickerPackageId': 446,
        'stickerId': 1990
        }
    if pic:
        files = {'imageFile': open(pic, 'rb')}
        print(files)

    r = requests.post(
            url,
            headers=headers, 
            params=payload,
            files = files)
    return r.status_code

# Read LOG file
log = open("LOG.txt", "r").read()

# Success rate calculation
success_cnt = log.count('SUCCESS')
fail_cnt = log.count('FAIL')
rate = float('{:.3f}'.format(success_cnt/(success_cnt+fail_cnt))) * 100
rate_str = str(rate) + "%"


message = "[MMS] Success : " + rate_str
# Line notify token
token = 'bg8CjdBtdT24M8BkSCnDLwSM3z7wxV2tmvC4O5F2VqK'
picURI = "frenchie.jpg"

result = lineNotifyMessage(token, message, picURI)
print(result)

