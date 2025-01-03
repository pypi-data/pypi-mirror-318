SeawayCli

## 1. 安装

### 1.1. python3环境安装

brew install python3


### 1.2. seaway安装

pip3 install seaway

## 2. 使用

### 2.1. 初始化APP壳工程

```
seaway init app
```

* 在工程目录下运行 
* 初始化成功后在gradle.properties配置你的信息
    ```
    #seaway config
    seaway.depRepo=请填写依赖git地址
    seaway.versionName=请填写APP版本名
    seaway.versionCode=请填写APP版本号
    seaway.appName=请填写APP名
    seaway.useLocalDependencies=false
    seaway.hostApp=true
    ```

### 2.2. 初始化组件壳工程
```
seaway init mp
```

* 在工程目录下运行 seaway init mp
* 初始化成功后在gradle.properties配置你的信息
    ```
    #seaway config
    seaway.depRepo=请填写依赖git地址
    ```

### 2.3. 初始化组件模块
```
seaway init module
  -dir , --dirPath   组件工程路径(默认命令运行目录)
  -g , --group       maven group
  -a , --artifact    maven artifact
```
* 可以指定group和artifact 
    ```
    seaway init module -g group -a artifact
    ```

* 可以交互式输入group和artifact 
    ```
    seaway init module
    ```


* 初始化成功后在模块的nexus.properties确认你的信息
    ```
    nexus_groupId=123
    nexus_artifactId=123
    ```

## 3. 变更日志
请查看 [变更日志](CHANGELOG.md) 了解详细版本更新信息。