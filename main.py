import gambling_subprocessor as gambler
import configparser, json, re

baseURIRemove = 'rolldie/'
baseURI = '/'
formats = ['json', 'csv', 'raw']

welcomeString = """welcome to rolldie.live!
to use rolldie.live, simply pass your dice roll as such:
  rolldie.live/1d20

other examples:
  rolldie.live/20d20
  rolldie.live/100d20/json

Available formats are: json, csv, raw

source code on https://github.com/woovie/rolldie.live"""

def application(env, start_response):
    returnString = ''
    reqURI = env['REQUEST_URI'].replace(baseURIRemove, '')
    if 'favicon' in reqURI:
        start_response('404 File Not Found')
        return [b'404 File Not Found']
    reqSplit = reqURI.split('/')
    if reqURI == baseURI:
        returnString = welcomeString
    elif re.match("^\d+d\d+$", reqSplit[1]):
        quantity, sides = reqSplit[1].split('d')
        gamblerResult = gambler.simple_math(int(quantity), int(sides))
        if len(reqSplit) == 2:
            returnString = ", ".join(str(x) for x in gamblerResult)
            if len(gamblerResult) > 1:
                returnString += f"\nTotal: {sum(gamblerResult)}"
        if len(reqSplit) == 3:
            if reqSplit[2] == 'json':
                returnString = json.dumps(gamblerResult)
            elif reqSplit[2] == 'csv':
                returnString = ",".join(str(x) for x in gamblerResult)
            elif reqSplit[2] == 'raw':
                returnString = " ".join(str(x) for x in gamblerResult)
            else:
                returnString = ", ".join(str(x) for x in gamblerResult)
                if len(gamblerResult) > 1:
                    returnString += f"\nTotal: {sum(gamblerResult)}"
                returnString += f"\n\nProvided format type ({reqSplit[2]}) incompatible, available options: {', '.join(formats)}"
    else:
        returnString = f"{welcomeString}\n\nSorry, it seems the provided URI is invalid:\n{reqURI}"
    return [f"{returnString}\n".encode()]
