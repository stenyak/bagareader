#!/bin/bash
appengineDir="$HOME/usr/shared/google_appengine"
waveapiDir="./waveapi"
echo " >>> Checking out project dependencies"
bash deps.sh
echo " >>> Checking out waveapi to $waveapiDir"
svn co http://wave-robot-python-client.googlecode.com/svn/trunk/src/waveapi waveapi
echo " >>> Checking out appengine to $appengineDir"
svn co http://googleappengine.googlecode.com/svn/trunk/python $appengineDir
echo " >>> Creating symlinks"
ln -fst ~/usr/bin/ $appengineDir/{dev_appserver.py,appcfg.py}
echo " >>> You can now serve the app locally using 'dev_appserver.py -p 10080 .'"
echo " >>> You can now deploy the app to server with 'appcfg.py update .'"
