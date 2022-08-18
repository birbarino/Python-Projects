'''
naive APPROACH:

import beautifulsoup or another webscraping lib?
import something useful for creating tables

prompt user to log into site, store no creds in program
log into website
scrape info from website
put into table, formatted beautifly and print?
export to CSV?
    -- prompt user for preference
'''


'''
CURL REQUEST - Available Apptmts for a Given Day at a Given Temple ID
*** '48' is the Temple ID used in this case, which is the Seattle Temple



curl 'https://tos.churchofjesuschrist.org/api/templeSchedule/getSessionInfo' -X POST 
-H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0' 
-H 'Accept: application/json' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' 
-H 'Content-Type: application/json;charset=utf-8' -H 'X-XSRF-TOKEN: f3235b7f-9897-4719-8fc1-f24f079d9584' 
-H 'Origin: https://tos.churchofjesuschrist.org' -H 'DNT: 1' -H 'Connection: keep-alive' 
-H 'Referer: https://tos.churchofjesuschrist.org/?locale=en&noCache=1654485128595' 
-H 'Cookie: AMCV_66C5485451E56AAE0A490D45%40AdobeOrg=1176715910%7CMCIDTS%7C19150%7CMCMID%7C52033211225016407328959528403025176614%7CMCOPTOUT-1654492328s%7CNONE%7CvVersion%7C5.4.0; 
    PFpreferredHomepage=COJC; 
    notice_behavior=implied|us; 
    AMCVS_66C5485451E56AAE0A490D45%40AdobeOrg=1; 
    mbox=session#10edf1af45c04174992deed79e384849#1654486988; 
    at_check=true; 
    amlbcookie-prod=01; 
    ORIG_URL=/sso?realm=/church&service=OktaOIDC&goto=https://www.churchofjesuschrist.org/services/platform/v4/set-wam-cookie&authIndexType=service&authIndexValue=OktaOIDC; 
    NTID=TNAdz1UTXoS1ICULlwIGNyYWmCaS94t7; 
    OAUTH_LOGOUT_URL=; 
    ChurchSSO=gmWiozcVJFc91cnNVONsCun_TGI.*AAJTSQACMDIAAlNLABxydTdyK3F6SjhIOCt1eG1TYVdtV2NEQzJFbFE9AAR0eXBlAANDVFMAAlMxAAIwMQ..*; 
    verificationNotice=hide; 
    BIGipServerpool_chl.cf.churchofjesuschrist.org_HTTP=4236785162.20480.0000; 
    BIGipServerpool_temple.churchofjesuschrist.org_HTTPS=813396746.47873.0000; 
    Church-auth-jwt-prod=eyJ0eXAiOiJKV1QiLCJraWQiOiIvQnA5UHlqa2QwWE9WT1RoZVlOb21URitHa3M9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJldGhuc3lycyIsImF1ZGl0VHJhY2tpbmdJZCI6Ijg1MzBiOTRkLTc5ODI
        tNDA4Ni05YjA3LWVlNzViZDc4YzYxZS0zMTYwMTA5ODQiLCJpc3MiOiJudWxsOi8vaWRlbnQtcHJvZC5jaHVyY2hvZmplc3VzY2hyaXN0Lm9yZzo0NDMvc3NvL29hdXRoMiIsInRva2VuTmFtZSI6ImlkX3Rva2VuIiwibm9uY2UiOi
        JPTmJGMnRpM0ZQNVY2R1ZiIiwiYXVkIjoibDE4MzgyIiwiYWNyIjoiMCIsImF6cCI6ImwxODM4MiIsImF1dGhfdGltZSI6MTY1NDQ4MjYyMCwiZm9yZ2Vyb2NrIjp7InNzb3Rva2VuIjoiZ21XaW96Y1ZKRmM5MWNuTlZPTnNDdW5fV
        EdJLipBQUpUU1FBQ01ESUFBbE5MQUJ4eWRUZHlLM0Y2U2poSU9DdDFlRzFUWVZkdFYyTkVRekpGYkZFOUFBUjBlWEJsQUFORFZGTUFBbE14QUFJd01RLi4qIiwic3VpZCI6IjU0MmY2MjJmLTAyNzItNDgyMy1hN2IyLTE4MjRlNWJh
        MzVhNS0zMTI1MTQ1OTEifSwicmVhbG0iOiIvY2h1cmNoIiwiZXhwIjoxNjU0NTI4MzI3LCJ0b2tlblR5cGUiOiJKV1RUb2tlbiIsImlhdCI6MTY1NDQ4NTEyNywiYWdlbnRfcmVhbG0iOiIvY2h1cmNoIn0.SYfsWcQENAG99ANmWoS
        P2i0wB9qlF8VIKnhizivCZqIc1YFexbtg1joZ-YV3nSXiPpUqUfuNKfjoFJ2wK1kjOZcizKQ9d_-gSLhKAlC65-Bsh7Hx9IQFMTQpncVNXJsZ96wknGXky4DwZ7YCCfzf0cfei75Z5DLXmAam7l0pb1_qEI4iPh45WlF8OT7HXFpf8a
        SrraNastZGIQYsbXq8OrMhwIVFdHufgQttAcV3qMCxHWEmg-0btjTgBUjD8TEzGvnZAJ0q1MOfKDtlRaTaT1xzDFmsaj26daJYyE1sPLZ6qtgRQaNPSvAPS55HU7QlVkwLgVkIuQGjmbN27WOIrw; 
        JSESSIONID=9F3670CBE0381886CBED5C20F4CCDE21; 
    __VCAP_ID__=1702ddb0-a4ae-4ef7-4cc5-46b0; 
    XSRF-TOKEN=f3235b7f-9897-4719-8fc1-f24f079d9584; 
    tisLocale=en; 
    ADRUM_BTa=R:68|g:dec4b402-42bc-4896-8f86-cd5834d8e5ea|n:churchofjesuschrist-prod_6b18a1f3-d5bd-4201-be20-78fa6c4d8152; 
    SameSite=None; 
    ADRUM_BT1=R:68|i:1375344|e:144' 
-H 'Sec-Fetch-Dest: empty' 
-H 'Sec-Fetch-Mode: cors' 
-H 'Sec-Fetch-Site: same-origin' 
-H 'TE: trailers' 
--data-raw 
    '{"sessionYear":2022,"sessionMonth":5,"sessionDay":11,"appointmentType":"PROXY_BAPTISM","templeOrgId":48}'


Output: a large JSON with apptmt info based on chosen date and user's session - '{"sessionList":[{"sessionTime":"07:00", ... "}'
'''

# --------------------------------------

'''
CURL REQUEST - Online-Viewable Apptmt Types for Given Temple ID
*** '48' is the Temple ID used in this case, which is the Seattle Temple



curl 'https://tos.churchofjesuschrist.org/api/templeConfig/activeOnline/appointmentTypes/48' 
-H 'User-Agent: Python' -H 'Accept: application/json' 
-H 'Accept-Language: en-US,en;q=0.5' 
-H 'Accept-Encoding: gzip, deflate, br' 
-H 'X-XSRF-TOKEN: f3235b7f-9897-4719-8fc1-f24f079d9584' 
-H 'DNT: 1' -H 'Connection: keep-alive' 
-H 'Referer: https://tos.churchofjesuschrist.org/?locale=en&noCache=1654489403715' 
-H 'Cookie: AMCV_66C5485451E56AAE0A490D45%40AdobeOrg=1176715910%7CMCIDTS%7C19150%7CMCMID%7C52033211225016407328959528403025176614%7CMCOPTOUT-1654496603s%7CNONE%7CvVersion%7C5.4.0; 
    PFpreferredHomepage=COJC; notice_behavior=implied|us; AMCVS_66C5485451E56AAE0A490D45%40AdobeOrg=1; at_check=true; amlbcookie-prod=01; 
    ORIG_URL=/sso?realm=/church&service=OktaOIDC&goto=https://www.churchofjesuschrist.org/services/platform/v4/set-wam-cookie&authIndexType=service&authIndexValue=OktaOIDC; 
    NTID=BpxnSRLyjAuDhUjs5PlPUJ8W7Akb6eUZ; OAUTH_LOGOUT_URL=; verificationNotice=hide; BIGipServerpool_chl.cf.churchofjesuschrist.org_HTTP=4236785162.20480.0000; 
    BIGipServerpool_temple.churchofjesuschrist.org_HTTPS=813396746.47873.0000; 
    Church-auth-jwt-prod=eyJ0eXAiOiJKV1QiLCJraWQiOiIvQnA5UHlqa2QwWE9WT1RoZVlOb21URitHa3M9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJldGhuc3lycyIsImF1ZGl0VHJhY2tpbmdJZCI6ImY1YzRmNzJlLTgxMzU
        tNDU1Yi1iOGVjLTgwNTAyNTY2MjU4OC0zOTI1MzcxNTgiLCJpc3MiOiJudWxsOi8vaWRlbnQtcHJvZC5jaHVyY2hvZmplc3VzY2hyaXN0Lm9yZzo0NDMvc3NvL29hdXRoMiIsInRva2VuTmFtZSI6ImlkX3Rva2VuIiwibm9uY2UiOi
        IwYVpGaEtHd2JVQjNXclIxIiwiYXVkIjoibDE4Mzg1IiwiYWNyIjoiMCIsImF6cCI6ImwxODM4NSIsImF1dGhfdGltZSI6MTY1NDQ4OTEwMiwiZm9yZ2Vyb2NrIjp7InNzb3Rva2VuIjoieVlMbUs0SzRGUDRnMndYS0RWZ2pCd1MzVF
        VnLipBQUpUU1FBQ01ESUFBbE5MQUJ3elpIbHhVRU4xT1cxME5VbGFLMjEyYVNzd2VtMDVRblZqUkZFOUFBUjBlWEJsQUFORFZGTUFBbE14QUFJd01RLi4qIiwic3VpZCI6IjU0MmY2MjJmLTAyNzItNDgyMy1hN2IyLTE4MjRlNWJhMz
        VhNS0zMjExNjIwMTQifSwicmVhbG0iOiIvY2h1cmNoIiwiZXhwIjoxNjU0NTMyNjAyLCJ0b2tlblR5cGUiOiJKV1RUb2tlbiIsImlhdCI6MTY1NDQ4OTQwMiwiYWdlbnRfcmVhbG0iOiIvY2h1cmNoIn0.c05gXjsVVPfBrRciaZnnxR
        YH96XByj-Rds1xidv5cgJURaD8jwrcOnrnbjjMqRJrF9-J2Zx4_2GkBcaoPH2Cyw70MmlZ7YDfdszMtV4Yk6dITQ3PD8Mh_Qjg2qjdIvgGcxbKHj-EDbsSrJus88yR9GY69a5sI9dl5zfLInPdyghEdoV27rbIPevOG7YfpYYigSv7lg
        wo45SN5GFOfiixfju6f0h2W33mbP1-xNyccZtSlBxYkvdu9PQbyLtGvAo-rIAUyqkgmCvDDESsqWvKwYNviKnBNyRoMUmg3JmKc_qjmZeTMVMiHGxny4ex72tD0UJPDUI3Ec7SVvpEfBFw1g; 
        
    JSESSIONID=9F3670CBE0381886CBED5C20F4CCDE21; 
    __VCAP_ID__=1702ddb0-a4ae-4ef7-4cc5-46b0; 
    XSRF-TOKEN=f3235b7f-9897-4719-8fc1-f24f079d9584; 
    tisLocale=en;
    mbox=session#99288dec173f40f58a0f510a59a2a2a8#1654491263; 
    ChurchSSO=yYLmK4K4FP4g2wXKDVgjBwS3TUg.*AAJTSQACMDIAAlNLABwzZHlxUEN1OW10NUlaK212aSswem05QnVjRFE9AAR0eXBlAANDVFMAAlMxAAIwMQ..*; 
    SameSite=None; 
    ADRUM_BTa=R:68|g:e320ce0b-b271-46c9-8fc1-b6e063e7956a|n:churchofjesuschrist-prod_6b18a1f3-d5bd-4201-be20-78fa6c4d8152; 
    ADRUM_BT1=R:68|i:1375334|e:56' 
-H 'Sec-Fetch-Dest: empty' 
-H 'Sec-Fetch-Mode: cors' 
-H 'Sec-Fetch-Site: same-origin'



Output: ["PROXY_BAPTISM","PROXY_INITIATORY","PROXY_ENDOWMENT","PROXY_SEALING"]
'''



'''
PYTHON REQUEST - Available Apptmts for a Given Day at a Given Temple ID
    REQUIREMENTS - Valid cookie/login session. Must be stored in "Cookie" header/key
'''
# TODO: Use "from x import y" with all required 
import requests
from requests.structures import CaseInsensitiveDict

url = "https://tos.churchofjesuschrist.org/api/templeSchedule/getSessionInfo"

headers = CaseInsensitiveDict()
headers["User-Agent"] = "TempleScraper" 
headers["Accept"] = "application/json"
headers["Accept-Language"] = "en-US,en;q=0.5"
headers["Accept-Encoding"] = "gzip, deflate, br"    # Probably can be changed to just gzip
headers["Content-Type"] = "application/json;charset=utf-8"
headers["X-XSRF-TOKEN"] = "f3235b7f-9897-4719-8fc1-f24f079d9584"    # TODO: Figure out what this header does
headers["Origin"] = "https://tos.churchofjesuschrist.org"
headers["DNT"] = "1"
headers["Connection"] = "keep-alive"
headers["Referer"] = "https://tos.churchofjesuschrist.org/?locale=en&noCache=1654485128595"

# TODO: Figure out a way to get a cookie with little user intervention.
headers["Cookie"] = "AMCV_66C5485451E56AAE0A490D45%40AdobeOrg=1176715910%7CMCIDTS%7C19150%7CMCMID%7C52033211225016407328959528403025176614%7CMCOPTOUT-1654492328s%7CNONE%7CvVersion%7C5.4.0; PFpreferredHomepage=COJC; notice_behavior=implied|us; AMCVS_66C5485451E56AAE0A490D45%40AdobeOrg=1; mbox=session#10edf1af45c04174992deed79e384849#1654486988; at_check=true; amlbcookie-prod=01; ORIG_URL=/sso?realm=/church&service=OktaOIDC&goto=https://www.churchofjesuschrist.org/services/platform/v4/set-wam-cookie&authIndexType=service&authIndexValue=OktaOIDC; NTID=TNAdz1UTXoS1ICULlwIGNyYWmCaS94t7; OAUTH_LOGOUT_URL=; ChurchSSO=gmWiozcVJFc91cnNVONsCun_TGI.*AAJTSQACMDIAAlNLABxydTdyK3F6SjhIOCt1eG1TYVdtV2NEQzJFbFE9AAR0eXBlAANDVFMAAlMxAAIwMQ..*; verificationNotice=hide; BIGipServerpool_chl.cf.churchofjesuschrist.org_HTTP=4236785162.20480.0000; BIGipServerpool_temple.churchofjesuschrist.org_HTTPS=813396746.47873.0000; Church-auth-jwt-prod=eyJ0eXAiOiJKV1QiLCJraWQiOiIvQnA5UHlqa2QwWE9WT1RoZVlOb21URitHa3M9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJldGhuc3lycyIsImF1ZGl0VHJhY2tpbmdJZCI6Ijg1MzBiOTRkLTc5ODItNDA4Ni05YjA3LWVlNzViZDc4YzYxZS0zMTYwMTA5ODQiLCJpc3MiOiJudWxsOi8vaWRlbnQtcHJvZC5jaHVyY2hvZmplc3VzY2hyaXN0Lm9yZzo0NDMvc3NvL29hdXRoMiIsInRva2VuTmFtZSI6ImlkX3Rva2VuIiwibm9uY2UiOiJPTmJGMnRpM0ZQNVY2R1ZiIiwiYXVkIjoibDE4MzgyIiwiYWNyIjoiMCIsImF6cCI6ImwxODM4MiIsImF1dGhfdGltZSI6MTY1NDQ4MjYyMCwiZm9yZ2Vyb2NrIjp7InNzb3Rva2VuIjoiZ21XaW96Y1ZKRmM5MWNuTlZPTnNDdW5fVEdJLipBQUpUU1FBQ01ESUFBbE5MQUJ4eWRUZHlLM0Y2U2poSU9DdDFlRzFUWVZkdFYyTkVRekpGYkZFOUFBUjBlWEJsQUFORFZGTUFBbE14QUFJd01RLi4qIiwic3VpZCI6IjU0MmY2MjJmLTAyNzItNDgyMy1hN2IyLTE4MjRlNWJhMzVhNS0zMTI1MTQ1OTEifSwicmVhbG0iOiIvY2h1cmNoIiwiZXhwIjoxNjU0NTI4MzI3LCJ0b2tlblR5cGUiOiJKV1RUb2tlbiIsImlhdCI6MTY1NDQ4NTEyNywiYWdlbnRfcmVhbG0iOiIvY2h1cmNoIn0.SYfsWcQENAG99ANmWoSP2i0wB9qlF8VIKnhizivCZqIc1YFexbtg1joZ-YV3nSXiPpUqUfuNKfjoFJ2wK1kjOZcizKQ9d_-gSLhKAlC65-Bsh7Hx9IQFMTQpncVNXJsZ96wknGXky4DwZ7YCCfzf0cfei75Z5DLXmAam7l0pb1_qEI4iPh45WlF8OT7HXFpf8aSrraNastZGIQYsbXq8OrMhwIVFdHufgQttAcV3qMCxHWEmg-0btjTgBUjD8TEzGvnZAJ0q1MOfKDtlRaTaT1xzDFmsaj26daJYyE1sPLZ6qtgRQaNPSvAPS55HU7QlVkwLgVkIuQGjmbN27WOIrw; JSESSIONID=9F3670CBE0381886CBED5C20F4CCDE21; __VCAP_ID__=1702ddb0-a4ae-4ef7-4cc5-46b0; XSRF-TOKEN=f3235b7f-9897-4719-8fc1-f24f079d9584; tisLocale=en; ADRUM_BTa=R:68|g:dec4b402-42bc-4896-8f86-cd5834d8e5ea|n:churchofjesuschrist-prod_6b18a1f3-d5bd-4201-be20-78fa6c4d8152; SameSite=None; ADRUM_BT1=R:68|i:1375344|e:144"

headers["Sec-Fetch-Dest"] = "empty"
headers["Sec-Fetch-Mode"] = "cors"
headers["Sec-Fetch-Site"] = "same-origin"
headers["TE"] = "trailers"

# Data to pass into request, specifies appointment type and location
data = '{"sessionYear":2022,"sessionMonth":5,"sessionDay":11,"appointmentType":"PROXY_BAPTISM","templeOrgId":48}'

# Use POST method to make a request and store the response.
resp = requests.post(url, headers=headers, data=data)

# 200-299 means success. 401 means Unauthorized, 403 means Forbidden.
print(resp.status_code)

# JSON with all schedule information (byte literal)
print(resp.content)
