## microServices
[microservices](https://martinfowler.com/articles/microservices.html)
### 特征（Characteristics)
*  服务组件化 Componentization via Services
> We define **libraries** as components that are linked into a program and called using in-memory function calls, while **services** are out-of-process components who communicate with a mechanism such as a web service request, or remote procedure call. (This is a different concept to that of a service object in many OO programs [3](https://martinfowler.com/articles/microservices.html#footnote-service-object).)
优点：
	- 服务独立部署，类库服务整体部署
	- 服务功能模块清晰的对外接口
缺点：
	-  远程调用更耗资源
* Organized around Business Capabilities
* Products not Projects
* Smart endpoints and dumb pipes（智能终端，愚蠢管道）
* Decentralized Governance（去中心化治理分散式管治）