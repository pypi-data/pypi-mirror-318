# ToDo

- [x] most basic QingpingCloud class with get_token and list_devices support that just respond with raw JSONs
- [x] __main__ wrapper for CLI with env variables reading for credentials
- [x] finalize docs
- [x] parse response data into QingpingDevice and QingpingDeviceProperty classes
- [ ] store token in ENV and attempt re-using known one
- [ ] support device history data
- [ ] support device history event
- [ ] support device settings modification
- [ ] package and publish
- [ ] improve CLI with proper level logging and error handling
- [ ] review more precise data type for QingpingDeviceProperty
- [ ] add unit conversion to QingpingDeviceProperty (temperature, ppb in tvoc, timestamp to human readable or seconds since now)
