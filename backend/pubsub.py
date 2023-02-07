import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-e9af7018-6480-4235-88da-30d51b145b49'
pnconfig.publish_key = 'pub-c-4b50a9c5-642a-4efe-90e5-1a092dcfddce'

TEST_CHANNEL = 'TEST_CHANNEL'

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Channel: {message_object.channel} | Message: {message_object.message}')

class PubSub():
    """
    Handles the publish/subscribe layer of the application
    Provides communication between the nodes of the blockchain network.
    """
    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels([TEST_CHANNEL]).execute()
        self.pubnub.add_listener(Listener())

    def publish(self, channel, message):
        """
        Publish the message object to the channel.
        """
        self.pubnub.publish().channel(channel).message(message).sync()


def main():
    pubsub = PubSub()

    time.sleep(1)
    
    pubsub.publish(TEST_CHANNEL, { 'foo': 'bar' })

if __name__ == '__main__':
    main()