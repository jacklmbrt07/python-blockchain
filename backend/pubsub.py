import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-e9af7018-6480-4235-88da-30d51b145b49'
pnconfig.publish_key = 'pub-c-4b50a9c5-642a-4efe-90e5-1a092dcfddce'
pubnub = PubNub(pnconfig)

TEST_CHANNEL = 'TEST_CHANNEL'

pubnub.subscribe().channels([TEST_CHANNEL]).execute()

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Incoming message_object: {message_object}')

pubnub.add_listener(Listener())

def main():
    time.sleep(1)
    
    pubnub.publish().channel(TEST_CHANNEL).message({ 'foo': 'bar' }).sync()

if __name__ == '__main__':
    main()