from waveapi import events
from waveapi import robot
from waveapi import element
from waveapi import appengine_robot_runner
import logging
import bagafeed

def OnWaveletSelfAdded(event, wavelet):
    """Invoked when the robot has been added."""
    logging.info("OnWaveletSelfAdded called")
    blip = wavelet.root_blip
    blip.append('Please, insert the URL for the feed, and press the button.\n')
    blip.append(element.TextArea(name='feedUrl', value='http://www.motorpasion.com/index.xml'))
    blip.append('\n')
    blip.append( element.Button(name='updateFeedUrl', value='Update Feed URL'))
    blip.append('\n')
    blip.append(element.Image(url='http://bagareader.googlecode.com/hg/bagareader.png', width=64, height=64))
    blip.append('\n')


  
def OnFormButtonClicked(event, wavelet):
    logging.info("OnParticipantsChanged called")
    blip = wavelet.reply("Button %r pressed! Getting last entry." %event.button_name)
    ta = (blip.first(element.TextArea)).value
    blip.append("\n\n%r\n\n" %ta.value)
    #text = bagafeed.printLastEntry("http://www.motorpasion.com/index.xml")
    #blip.append(text)

if __name__ == '__main__':
    myRobot = robot.Robot('BagaReader helper bot', 
        image_url='http://bagareader.googlecode.com/hg/bagareader.png',
        profile_url='http://code.google.com/p/bagareader');
    myRobot.register_handler(events.FormButtonClicked, OnFormButtonClicked)
    myRobot.register_handler(events.WaveletSelfAdded, OnWaveletSelfAdded)
    appengine_robot_runner.run(myRobot)
