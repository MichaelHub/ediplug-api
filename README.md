# Ediplug-API

A simple, deployable Python-based API to control Edimax devices. Based
on [wendlers/ediplug-py](https://github.com/wendlers/ediplug-py) and should work on the Edimax SP1101W/SP2101W, but has
only been tested with the SP1101W. Tested with Python 3.7.

## Configuration

The following environment variables are required:

* `HOST`: Hostname (ex. 192.168.1.100)
* `USERNAME`: Username for device, configured on initial device setup (ex. admin)
* `PASSWORD`: Password for device, configured on initial device setup (ex. hunter2)

## Endpoints

| Endpoint | Purpose | Payload | Method |
| ------ | ------ | ------ | ----- |
| /info | Provides power state and device information | ```{"device": {"mac":"12345678ABCDEF", "model":"SP2101W" ,"name":"DeviceName" ,"vendor":"Edimax" ,"version":"2.03"} ,"state":"ON"}``` | GET |
| /toggle | Toggles the power of the device and returns current power state | ```{"state":"ON"}``` | GET, POST |
| /on | Sets power to on and returns current power state | ```{"state":"ON"}``` | GET, POST |
| /off | Sets power to off and returns current power state | ```{"state":"OFF"}``` | GET, POST |
| /status | Provides power state information | ```{"state":"ON"}``` | GET |
| /schedule | Provides schedule information | GET ```[{"day":0,"sched":[],"state":"OFF"},{"day":1,"sched":[],"state":"OFF"},{"day":2,"sched":[],"state":"OFF"},{"day":3,"sched":[],"state":"OFF"},{"day":4,"sched":[],"state":"OFF"},{"day":5,"sched":[],"state":"OFF"},{"day":6,"sched":[],"state":"OFF"}]``` | GET |
| /usage | Returns information about current power usage | ```{"current":"8.7879","wattage":"1000.07"}``` | GET |