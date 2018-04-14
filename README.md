[![Github All Releases](https://img.shields.io/github/downloads/bodastage/bts-ce/total.svg)](https://github.com/bodastage/bts-ce/releases/latest) [![GitHub repo size in bytes](https://img.shields.io/github/repo-size/bodastage/bts-ce.svg)](https://github.com/bodastage/bts-ce) [![Read the Docs](https://img.shields.io/readthedocs/bts-ce-docs.svg)]() [![GitHub release](https://img.shields.io/github/release/bodastage/bts-ce.svg)](https://github.com/bodastage/bts-ce/releases) [![license](https://img.shields.io/github/license/bodastage/bts-ce.svg)](https://raw.githubusercontent.com/bodastage/bts-ce/master/LICENCE)

## Boda Telecom Suite Community Edition (BTS-CE)

[![Join the chat at https://gitter.im/bts-ce/Lobby](https://badges.gitter.im/bts-ce/Lobby.svg)](https://gitter.im/bts-ce/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Boda Telecom Suite Community Edition - An open source telecommunication network management platform

## Features

* Generation of network topology from configuration data
* Radio network element browsing
* CM managed object browsing 
* Automatic network baseline generation
* Radio Access Network (RAN) audit (relations, conflicts, parameter values vs baseline )


## Requirements 

* 4GB memory
* 64 bit OS
* [Docker](https://www.docker.com/get-docker)
* 5GB hard disk space
* Latest web browser

## Deployment/Installation

### Windows
* Download latest release files from https://github.com/bodastage/bts-ce/releases
* Unzip the downloaded files to Drive:/Bodastage
* Launch the Windows **command prompt**
* Change directory to **Drive**:/Bodastage/bts-ce-**version** from the Windows command prompt
  ```batch 
  > cd  <Drive>:/Bodastage/bts-ce-<version>
  ```
* Run :  
  ```batch 
  > bts setup
  ```
* Access application at http://localhost from a supported browsers


> Enable Virtualization from the BIOS if using Windows Hyper-V


## Supported Web Browsers

| Desktop Browsers | Tablets |  Phones |
| -------- | ------- | ----------- |
| Safari 6.1+ | iPad 3+ |  iOS 8+ |
| Google Chrome 32+ |  Android 4.3+ | Android 4.3+ |
| Microsoft Edge |  |  |
| Firefox 27+ | | |

## Built With
- [Python](https://www.python.org)
- [PostgreSQL](https://www.postgresql.org/)
- [Apache Airflow](https://airflow.apache.org/)
- [BackboneJs](http://backbonejs.org/)

## Resources

* [Community Forum at TelecomHall.net](http://telecomHall.net)
* [Online Documentation](http://bts.bodastage.org)

## Copyright / License

Copyright 2017 - 2018 [Bodastage Solutions](http://www.bodastage.com)

Licensed under the Apache License, Version 2.0 ; you may not use this work except in compliance with the License. You may obtain a copy of the License in the LICENSE file, or at:

https://www.apache.org/licenses/LICENSE-2.0