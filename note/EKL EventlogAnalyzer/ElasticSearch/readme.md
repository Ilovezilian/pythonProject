# Elastic Search
## Download Elasticsearch
[Download Elasticsearch](https://www.elastic.co/cn/downloads/elasticsearch)

## Document
[Elasticsearch Guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)

## start
* Start Elasticsearch:
```cmd
bin\elasticsearch.bat
```
* curl http://127.0.0.1:9200
```cmd
curl http://127.0.0.1:9200

windows web response:
{
  "name" : "QtI5dUu",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "v8OWkR1OQO-rgV8o_lRhEA",
  "version" : {
    "number" : "7.14.0",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "f4d76bd413ecfbd5122c3aa5dc85465960f18afe",
    "build_date" : "2021-04-23T15:58:28.336786977Z",
    "build_snapshot" : false,
    "lucene_version" : "8.8.2",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```



Elasticsearch is the distributed, RESTful search and analytics engine at the
heart of the 
[Elastic Stack](https://www.elastic.co/products). You can use
Elasticsearch to store, search, and manage data for:

* Logs
* Metrics
* A search backend
* Application monitoring
* Endpoint security

\... and more!

To learn more about Elasticsearch's features and capabilities, see our
[product page](https://www.elastic.co/products/elasticsearch).

## Get started

The simplest way to set up Elasticsearch is to create a managed deployment with
[Elasticsearch Service on Elastic Cloud](https://www.elastic.co/cloud/as-a-service).

If you prefer to install and manage Elasticsearch yourself, you can download
the latest version from 
[elastic.co/downloads/elasticsearch](https://www.elastic.co/downloads/elasticsearch).

For more installation options, see the
[Elasticsearch installation documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html).

## Upgrade

To upgrade from an earlier version of Elasticsearch, see the
[Elasticsearch upgrade documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html).

## Build from source

Elasticsearch uses [Gradle](https://gradle.org) for its build system.

To build a distribution for your local OS and print its output location upon
completion, run:
----
./gradlew localDistro
----

To build a distribution for another platform, run the related command:
----
./gradlew :distribution:archives:linux-tar:assemble
./gradlew :distribution:archives:darwin-tar:assemble
./gradlew :distribution:archives:windows-zip:assemble
----

To build distributions for all supported platforms, run:
----
./gradlew assemble
----

Distributions are output to `distributions/archives`.

To run the test suite, see xref:TESTING.asciidoc[TESTING].

## Documentation

For the complete Elasticsearch documentation visit
[elastic.co](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html).

For information about our documentation processes, see the
xref:docs/README.asciidoc[docs README].

## Contribute

For contribution guidelines, see xref:CONTRIBUTING.md[CONTRIBUTING]. 

## Questions? Problems? Suggestions?

* To report a bug or request a feature, create a
[GitHub Issue](https://github.com/elastic/elasticsearch/issues/new/choose). Please
ensure someone else hasn't created an issue for the same topic.

* Need help using Elasticsearch? Reach out on the
[Elastic Forum](https://discuss.elastic.co)or 
[Slack](https://ela.st/slack). A
fellow community member or Elastic engineer will be happy to help you out.

