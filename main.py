import gambling_subprocessor as gambler
import configparser, os, json

baseURI = '/'

welcomeString = """welcome to rolldie.live!
to use rolldie.live, simply pass your dice roll as such:
  rolldie.live/1d20

source code on https://github.com/woovie/rolldie.live"""

def application(env, start_response):
    returnString = ''
    reqURI = env['REQUEST_URI']
    if 'favicon' in reqURI:
        start_response('404 File Not Found')
        return [b'404 File Not Found']
    if reqURI == baseURI:
        returnString = welcomeString
    elif reqURI.startswith(baseURI) and len(reqURI) > 3:
        quantity, sides = reqURI.replace(baseURI, '').split('d')
        returnString = ", ".join(str(x) for x in gambler.simple_math(int(quantity), int(sides)))
    else:
        returnString = f"{welcomeString}\n\nSorry, it seems the provided URI is invalid:\n{reqURI}"
    return [f"{returnString}\n".encode()]
