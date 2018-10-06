import gambling_subprocessor as gambler
import configparser, os, json

welcomeString = """welcome to rolldie.live!
to use rolldie.live, simply pass your dice roll as such:
  rolldie.live/1d20

source code on https://github.com/woovie/rolldie.live"""

def application(env, start_response):
    returnString = ''
    reqURI = env['REQUEST_URI']
    if reqURI == '/rolldie':
        returnString = welcomeString
    elif reqURI.startswith('/rolldie/') and len(reqURI) > 11:
        quantity, sides = reqURI.replace('/rolldie/', '').split('d')
        returnString = ", ".join(str(x) for x in gambler.simple_math(int(quantity), int(sides)))
    else:
        returnString = f"{welcomeString}\n\nSorry, it seems the provided URI is invalid:\n{reqURI}"
    return [f"{returnString}\n".encode()]
    

#    if message.content.startswith('!roll'):
#            "{0}: {1}".format(message.author, gambler.roll(message.content)))
#    elif message.content.startswith('!cast'):
#            "{0}: {1}".format(message.author, gambler.cast(message.content)))
