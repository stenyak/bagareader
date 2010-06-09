#!/bin/bash
echo "==================================================================="
echo "This script will set up your development environment for BagaReader"
echo "==================================================================="
echo ""

prefix="$HOME/usr"

appengineDir="$prefix/share/google_appengine"
waveapiDir="./waveapi"
binDir="$prefix/bin"

mkdir -p appengineDir waveapiDir binDir

echo " >>> Checking out project dependencies"
bash deps.sh
echo " >>> Checking out waveapi to $waveapiDir"
svn co http://wave-robot-python-client.googlecode.com/svn/trunk/src/waveapi waveapi
echo " >>> Checking out appengine to $appengineDir"
svn co http://googleappengine.googlecode.com/svn/trunk/python $appengineDir
echo " >>> Creating symlinks"
ln -fst $prefix/bin/ $appengineDir/{dev_appserver.py,appcfg.py}
echo ""
echo "==================================================================="
echo "You can now deploy the bagareader bot to server using './deploy.sh'"
echo "==================================================================="
