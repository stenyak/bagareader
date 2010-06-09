#!/bin/bash

realYaml="app.yaml"
refYaml="$realYaml.official"

localRev=$(hg head |grep changeset |sed "s/.*:\s*\(.*\):.*/\1/g")
appName="${GOOGLEAPPENGINE_DEV_APP_NAME}"

if [ "$appName" == "" ]
then
    appName=$USER
fi

rm $realYaml
echo "#############################################################################" >> $realYaml
echo "# THIS IS A TEMPORARY $realYaml FILE GENERATED BY $(basename $0)" >> $realYaml
echo "# CHANGES TO THIS FILE WILL BE IGNORED. MODIFY $refYaml INSTEAD" >> $realYaml
echo "#############################################################################" >> $realYaml
cat $refYaml |sed "s/^application:.*/application: $appName/g;s/^version:.*/version: dev-$localRev/g" >> $realYaml
echo "#############################################################################" >> $realYaml

#appcfg.py update .

#rm $realYaml