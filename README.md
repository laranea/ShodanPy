# ShodanPy
ShodanPy is a simple command line framework wrapper around the Shodan API. It includes most of the core features offered by the shodan engine like getting information about a host, statistical data, searching for services, ports, servers, products and giving detailed information about them. It also includes a module for giving information about all possible vulnerabilities and exploits available for a service.

##Getting Started

###Prerequisites

API_key

    By creating an account on www.shodan.io

Json python library
      
      pip install json

Urllib2
  
    pip install urllib2

PyFiglet
  
    pip install pyfiglet

###Executing the Tool

Download the repository and execute main.py:

    python main.py

##Screenshots

###The Main and Help Module

![screen shot 2016-10-12 at 2 18 21 am](https://cloud.githubusercontent.com/assets/20644368/19288965/1e357962-9026-11e6-9924-0470bf7140a4.png)

###Search Module

![screen shot 2016-10-12 at 2 16 57 am](https://cloud.githubusercontent.com/assets/20644368/19289083/a4356662-9026-11e6-8995-406ecdf5b3c8.png)


###Host Module

![screen shot 2016-10-12 at 2 15 36 am](https://cloud.githubusercontent.com/assets/20644368/19289047/77a2e1f6-9026-11e6-90f8-47c49467a672.png)


###The Exploits Module

The user has to type in the service or application name and the shodan api will search for all possible vulnerabilities and exploits corresponding to that particular service from exploitdb, CVE and few other sources and prints them on the screen.

![screen shot 2016-10-12 at 2 14 45 am](https://cloud.githubusercontent.com/assets/20644368/19289020/5a654958-9026-11e6-9b95-37d8ead8cc74.png)



##Developer

Vasisht Duddu(vduddu)

##License

This project is licensed under the MIT License - see the LICENSE file for details
