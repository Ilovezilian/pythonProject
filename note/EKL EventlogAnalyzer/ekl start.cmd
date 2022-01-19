:: this bash is start ELK system.
:: Author shuai.pan
:: 2021-08-13
::

echo command for function:
echo 0-show all home path
echo 1-restart elastic search service
echo 2-restart kibana service
echo 3-restart logstash service
echo 4-restart filebeat service


set ELASTIC_SEARCH_HOME = d:\Downloads\soft\elasticsearch-7.14.0-windows-x86_64\elasticsearch-7.14.0
echo %ELASTIC_SEARCH_HOME%
%ELASTIC_SEARCH_HOME%\bin\elasticsearch.bat

set KIBANA_HOME = d:\Downloads\soft\kibana-7.14.0-windows-x86_64
echo %KIBANA_HOME%
%KIBANA_HOME%\bin\kibana.bat

set LOGSTACK_HOME = d:\Downloads\soft\logstash-7.14.0-windows-x86_64\logstash-7.14.0
echo %LOGSTACK_HOME%
%LOGSTACK_HOME%\bin\logstash -f config\first-pipeline.conf --config.reload.automatic

set FILEBEAT_HOME = d:\Downloads\soft\filebeat-7.14.0-windows-x86_64
echo %FILEBEAT_HOME%
%FILEBEAT_HOME%\filebeat -e -c my-filebeat.yml -d "publish"

rd .\data\registry\

:: 0 - show all home path
echo %ELASTIC_SEARCH_HOME%
echo %KIBANA_HOME%
echo %FILEBEAT_HOME%
echo %LOGSTACK_HOME%

