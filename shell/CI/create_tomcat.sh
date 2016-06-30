#!/bin/bash
port=$1

if [ ! -n "$port" ] ; then
         echo "error input port'"
         exit 0
fi

cp -r /opt/tomcat_9016 /opt/tomcat_$port
sed -i "s/16/${port:2}/g" "/opt/tomcat_"$port"/conf/server.xml"