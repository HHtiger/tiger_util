#!/bin/bash
project_name=$1
port=$2

if [ ! -n "$project_name" ] ; then
        echo "error input,do as 'deploy.sh project_name port'"
        exit 0
elif [ ! -n "$port" ] ;then
        echo "error input,do as 'deploy.sh project_name port'"
        exit 0
fi

#kill tomcat
echo "stop tomcat" 
res=`lsof -i:$port | awk '{print $2}' | cut -d " " -f2`
pid=${res/PID/""}
kill -9 $pid
echo "stop done." 

#deploy poject
echo "remve old file" 
rm -rf /opt/tomcat/webapps/*
echo "remove done."
echo "copy new file to tomcat."
cp /tmp/war/"$project_name".war /opt/tomcat/webapps/ 

if [[ $? -eq 0 ]];then 
        #start tomcat 
        echo "restart tomcat..." 
        bash /opt/tomcat/bin/startup.sh
else
        exit 0
fi
