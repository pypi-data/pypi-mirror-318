from dataclasses import dataclass

@dataclass
class QingpingDeviceProperty:
  property: str
  value: float
  status: int
  
  DEV_PROP_SPEC = { # see https://developer.qingping.co/cloud-to-cloud/specification-guidelines#2-products-list-and-support-note
    "battery": {
      "unit": "%", 
      "desc": "device battery", 
      "status": {
        0: "not plug in power", 
        1: "plug in power and in charging",
        2: "plug in power and 100%"
      }
    },
    "signal": {
      "unit": "dBm", 
      "desc": "device signal", 
      "status": None
    },
    "timestamp": {
      "unit": "", 
      "desc": "time of the message", 
      "status": None
    },
    "temperature": {
      "unit": "°C", 
      "desc": "value of temperature sensor", 
      "status": {
        0: "sensor normal", 
        1: "sensor abnormal",
        2: "sensor in the preparation stage"
      }
    },
    "prob_temperature": {
      "unit": "°C", 
      "desc": "value of external temperature sensor", 
      "status": None
    },
    "humidity": {
      "unit": "%", 
      "desc": "value of humidity sensor", 
      "status": {
        0: "sensor normal", 
        1: "sensor abnormal",
        2: "sensor in the preparation stage"
      }
    },
    "pressure": {
      "unit": "kPa", 
      "desc": "value of pressure sensor", 
      "status": None
    },
    "pm10": {
      "unit": "μg/m³", 
      "desc": "PM10", 
      "status": {
        0: "sensor normal", 
        1: "sensor abnormal",
        2: "sensor in the preparation stage"
      }
    },
    "pm50": {
      "unit": "μg/m³", 
      "desc": "PM5.0", 
      "status": {
        0: "sensor normal", 
        1: "sensor abnormal",
        2: "sensor in the preparation stage"
      }
    },
    "pm25": {
      "unit": "μg/m³", 
      "desc": "PM2.5", 
      "status": {
        0: "sensor normal", 
        1: "sensor abnormal",
        2: "sensor in the preparation stage"
      }
    },
    "co2": {
      "unit": "ppm", 
      "desc": "CO2", 
      "status": None
    },
    "tvoc": {
      "unit": "ppb", 
      "desc": "value of TVOC sensor", 
      "status": None
    },
    "tvoc_index": {
      "unit": "index", 
      "desc": "index of TVOC sensor", 
      "status": None
    },
    "noise": {
      "unit": "dB", 
      "desc": "inoise", 
      "status": {
        0: "sensor normal", 
        1: "sensor abnormal",
        2: "sensor in the preparation stage"
      }
    },
    "radon": {
      "unit": "pCi/L", 
      "desc": "value of radon sensor", 
      "status": None
    },
    "UNSUPPORTED": {
      "unit": "UNSUPPORTED", 
      "desc": "UNSUPPORTED PROPERTY", 
      "status": None
    }
  }

  def get_unit(self) -> str:
    return self.DEV_PROP_SPEC[self.property]["unit"]
  def get_desc(self) -> str:
    return self.DEV_PROP_SPEC[self.property]["desc"]
  def get_status(self) -> str:  
    return self.DEV_PROP_SPEC[self.property]["status"].get(self.status, "Unknown")

  def __str__(self) -> str:
    return f"{self.property}: {self.value} {self.get_unit()}"
