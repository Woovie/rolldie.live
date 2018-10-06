import gambling_subprocessor as gambler
import configparser
import os

def application(env, start_response):
    start_response('2OO OK', [('Content-Type', 'plaintext')])
    return [b'welcome to rolldie.live!']
    

#    # Roll dice, example: !roll 1d20 or !roll 1d20+3.
#    if message.content.startswith('!roll'):
#        await client.send_message(
#            message.channel,
#            "{0}: {1}".format(message.author, gambler.roll(message.content)))
#    # Stereotypical help message. Needs work.
#    elif message.content.startswith('!help'):
#        await client.send_message(
#            message.channel,
#            '{0}: Please use !roll 1d20 to roll.'.format(message.author))
#    # Uses json file to perform specific rolls based on the string following
#    # !cast
#    elif message.content.startswith('!cast'):
#        await client.send_message(
#            message.channel,
#            "{0}: {1}".format(message.author, gambler.cast(message.content)))

client.run(token)
