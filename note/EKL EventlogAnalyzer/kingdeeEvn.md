# kingdee Enviroment
## ElasticSearch
``` cmd 
cd d:\Downloads\soft\elasticsearch-7.14.0-windows-x86_64\elasticsearch-7.14.0\
-- start
.\bin\elasticsearch.bat
```
## Kibana
``` cmd 
cd d:\Downloads\soft\kibana-7.14.0-windows-x86_64\
-- start
.\bin\kibana.bat
```
## Filebeat
``` cmd 
cd d:\Downloads\soft\filebeat-7.14.0-windows-x86_64\

-- start
./filebeat -e -c my-filebeat.yml -d "publish"

---- 清空加载缓存，重新加载已经加载过的数据，开发时常用
 rm .\data\registry\

-- configFiles
cd d:\Downloads\soft\filebeat-7.14.0-windows-x86_64\*.yml
```
## Logstack
``` cmd 
cd d:\Downloads\soft\logstash-7.14.0-windows-x86_64\logstash-7.14.0\

-- start
bin/logstash -f config/first-pipeline.conf --config.reload.automatic

-- configFiles
d:\Downloads\soft\logstash-7.14.0-windows-x86_64\logstash-7.14.0\config\*.conf
```
