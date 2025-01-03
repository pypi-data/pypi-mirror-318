# oppoudpsdk
Python SDK for Oppo UDP-20x media devices.
The primary goal is to use this to power integrations for [Home Assistant](https://www.home-assistant.io/).

## Installation
```pip install oppoudpsdk```

## Usage
### Simple example

```
async def main():
  logging.basicConfig(level=logging.DEBUG, format='%(asctime)-15s %(levelname)-8s %(message)s')

  loop = asyncio.get_event_loop()
  client = OppoClient(HOST_NAME, 23, loop)
  client.add_event_handler(EVENT_DEVICE_STATE_UPDATED, on_device_state_updated)
  await asyncio.ensure_future(client.async_run_client(), loop=loop)

if __name__ == "__main__":
  asyncio.run(main())
```

Please see `simple_example.py` for a full working example of usage of this library.

## Objects
### OppoClient(host_name, port_number = 23, mac_address = None, event_loop = None)
The main client class that initiates and maintains a connection with the Oppo device.  Handles the raw communications between the client and the device.
### OppoDevice(client, mac_addr)
A class that describes a media device.  This is abstracted from the client so that the media functionality is isolated from the communications infrastructure.

## API Overview

Please refer to this document for the Oppo IP control API: [http://download.oppodigital.com/UDP203/OPPO_UDP-20X_RS-232_and_IP_Control_Protocol.pdf](http://download.oppodigital.com/UDP203/OPPO_UDP-20X_RS-232_and_IP_Control_Protocol.pdf)
