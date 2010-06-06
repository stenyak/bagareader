from waveapi import events
from waveapi import robot
from waveapi import appengine_robot_runner
import logging
import bagafeed

def OnWaveletSelfAdded(event, wavelet):
    """Invoked when the robot has been added."""
    wavelet.reply("This is BagaReader helper bot.\nI will now retrieve a sample feed entry in real time.")
    wavelet
    logging.info("OnWaveletSelfAdded called")
    text = bagafeed.printLastEntry("http://www.motorpasion.com/index.xml")
    wavelet.reply(text)
    """
    part = "stenyakstk@googlewave.com"
    try:
        wavelet.participants.add(part)
        wavelet.reply("\nAdded user %r" %part)
    except Exception, e:
        wavelet.reply("\nFailed to add user %r: %r" %(part, e))
    """
  
def OnWaveletParticipantsChanged(event, wavelet):
    logging.info("OnParticipantsChanged called")
    newParticipants = event.participants_added
    #for newParticipant in newParticipants:
    #    wavelet.reply("\nHi : " + newParticipant)

if __name__ == '__main__':
    myRobot = robot.Robot('BagaReader helper bot', 
        image_url='http://bagareader.googlecode.com/hg/bagareader.png',
        profile_url='http://code.google.com/p/bagareader');
    myRobot.register_handler(events.WaveletParticipantsChanged, OnWaveletParticipantsChanged)
    myRobot.register_handler(events.WaveletSelfAdded, OnWaveletSelfAdded)
    appengine_robot_runner.run(myRobot)
