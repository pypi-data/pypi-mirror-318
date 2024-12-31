import requests
import base64
import time
from .QingpingDevice import QingpingDevice
from .QingpingDeviceProperty import QingpingDeviceProperty

class QingpingCloud:
  OAUTH_TOKEN_URL = 'https://oauth.cleargrass.com/oauth2/token'
  API_URL_PREFIX = 'https://apis.cleargrass.com/v1/apis'
  
  def get_token(self) -> str:
    encoded_auth=base64.b64encode((self.app_key+":"+self.app_secret).encode()).decode()
    token_request = requests.post(
      self.OAUTH_TOKEN_URL,
      data={ 
        "grant_type": "client_credentials", 
        "scope": "device_full_access"
      },
      headers={
        "Content-Type": "application/x-www-form-urlencoded", 
        "Authorization": f"Basic {encoded_auth}",
        "Accept": "application/json"
      }
    )
    token=None
    if token_request.ok:
      try:
        token=token_request.json()["access_token"]
      except Exception as e:
        raise Exception(f"Error parsing token: {e}")
    else:
      raise Exception(f"Error getting token: {token_request.text}")
    self.token=token
    return token
  
  def _api_get(self, endpoint) -> dict:
    timestamp=int(time.time()*1000)
    if "?" in endpoint:
      url=f"{self.API_URL_PREFIX}/{endpoint}&timestamp={timestamp}"
    else:
      url=f"{self.API_URL_PREFIX}/{endpoint}?timestamp={timestamp}"
    
    api_request = requests.get(
      url,
      headers={
        "Authorization": f"Bearer {self.token}"
      }
    )
    
    api_response=None
    if api_request.ok:
      try:
        api_response=api_request.json()
      except Exception as e:
        raise Exception(f"Error parsing data: {e}")
    else:
      raise Exception(f"Error getting data: {api_request.text}")
    return api_response
  
  def get_devices(self) -> list[QingpingDevice]:
    api_response=self._api_get("devices")
    raw_devices=api_response.get("devices", [])
    devices = []
    for raw_device in raw_devices:
      data = {}
      for property_name, property_data in raw_device["data"].items():
        data[property_name] = QingpingDeviceProperty(
          property=property_name,
          value=property_data.get("value", float("nan")),
          status=property_data.get("status", 0)
        )
      device = QingpingDevice(
        name=raw_device["info"]["name"],
        mac=raw_device["info"]["mac"],
        group_id=raw_device["info"]["group_id"],
        group_name=raw_device["info"]["group_name"],
        status_offline=raw_device["info"]["status"]["offline"],
        version=raw_device["info"]["version"],
        created_at=raw_device["info"]["created_at"],
        product_id=raw_device["info"]["product"]["id"],
        product_name=raw_device["info"]["product"]["name"],
        product_en_name=raw_device["info"]["product"]["en_name"],
        setting_report_interval=raw_device["info"]["setting"]["report_interval"],
        setting_collect_interval=raw_device["info"]["setting"]["collect_interval"],
        data=data
      )
      devices.append(device)

    return devices
  
  def __init__(self, app_key, app_secret) -> None:
    self.app_key = app_key
    self.app_secret = app_secret
    
    self.get_token()
