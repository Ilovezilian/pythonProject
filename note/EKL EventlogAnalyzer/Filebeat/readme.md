# Filebeat 7.14.0

Filebeat sends log files to Logstash or directly to Elasticsearch.

## Getting Started

To test yml config is ok, run:
```cmd
cd %path_to_filebeat_home%
.\filebeat.exe test config -c filebeat.yml

```

To reLoad the history file into filebeat, run:
```cmd
rm .\data\registry\

```


To get started with Filebeat, you need to set up Elasticsearch on
your localhost first. After that, start Filebeat with:

```cmd
./filebeat -e -c filebeat.yml -d "publish"

./filebeat -c filebeat.yml -e
```
This will start Filebeat and send the data to your Elasticsearch
instance. To load the dashboards for Filebeat into Kibana, run:

``` cmd
    ./filebeat setup -e
```
For further steps visit the
[Quick start](https://www.elastic.co/guide/en/beats/filebeat/7.x/filebeat-installation-configuration.html) guide.

## Documentation

Visit [Elastic.co Docs](https://www.elastic.co/guide/en/beats/filebeat/7.x/index.html)
for the full Filebeat documentation.

## Release notes

https://www.elastic.co/guide/en/beats/libbeat/7.x/release-notes-7.14.0.html

## Download Filebeat
[Download Filebeat](https://www.elastic.co/downloads/beats/filebeat)

[regexp-support](https://www.elastic.co/guide/en/beats/filebeat/7.14/regexp-support.html)
