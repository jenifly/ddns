import json
import requests
import random
import re
import chardet
import os
import time

from aliyunsdkcore.client import AcsClient
import DescribeDomainRecordsRequest
import UpdateDomainRecordRequest

class IP(object):
  def __init__(self):
    from tool import user_agent_list
    self.user_agent_list = user_agent_list
    self.api_list = [
      'http://ip.chinaz.com/getip.aspx',
      'http://www.net.cn/static/customercare/yourip.asp',
      'https://ip.cn/',
      'http://www.ip168.com/json.do?view=myipaddress',
      'http://pv.sohu.com/cityjson',
      'http://pv.sohu.com/cityjson',
      'http://ip.taobao.com/service/getIpInfo.php?ip=myip',
      'http://2018.ip138.com/ic.asp',
      'http://ip.42.pl/raw'
    ]

  def ip_query(self):
    while True:
      url = random.sample(self.api_list, 1)[0]
      headers = random.sample(self.user_agent_list, 1)[0]
      try:
        res = requests.get(url, headers={'User-Agent':headers}, timeout=5)
        encoding = chardet.detect(res.content)['encoding']
        html = res.content.decode(encoding)
        out = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',html)
        if out != []: return out[0]
      except Exception as e:
        continue

class Aliyunddns(object):
  def __init__(self):
    self.local_ip = IP()
    self.client = AcsClient('LTAIe22FMMuyzR6j', 'lWuTpekTvHylvUoiwVIUOHt9ZmkNsh')
    self.domain = 'hctpx.cn'

  def IsConnectNet(self):
    try:
      requests.get('http://www.baidu.com',timeout=5)
      return True
    except requests.exceptions.ConnectionError as e:
      return False

  def CheckLocalip(self):
    if not self.IsConnectNet():
      print('No net...')
      return
    self.netip = self.local_ip.ip_query()
    if os.path.exists('ip.txt'):
      with open('ip.txt','r') as fp:
        file_ip = fp.read()
      if file_ip == self.netip:
        return print('same IP')
      else:
        print('start...')
        with open('ip.txt','w') as fp:
          fp.write(self.netip)
          fp.close()
        self.GetDomainRecords()
    else:
      with open('ip.txt','w') as fp: 
        fp.write(self.netip)
        fp.close()
      self.GetDomainRecords()

  def Update(self, record):
    udr = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
    udr.set_accept_format('json')
    udr.set_RecordId(record['RecordId'])
    udr.set_RR(record['RR'])
    udr.set_Type(record['Type'])
    udr.set_Value(self.netip)
    response = self.client.do_action_with_exception(udr)
    UpdateDomainRecordJson = json.loads(response.decode('utf-8'))
    print(UpdateDomainRecordJson)

  def GetDomainRecords(self):
    DomainRecords = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
    DomainRecords.set_DomainName(self.domain)
    DomainRecords.set_accept_format('json')
    response = self.client.do_action_with_exception(DomainRecords)
    record_dict = json.loads(response.decode('utf-8'))
    print(record_dict)
    for record in record_dict['DomainRecords']['Record']:
      if not record['RR'] in ['@','www']:
        continue
      if record['Value'] != self.netip:
        self.Update(record)

if __name__ == '__main__':
  Aliyunddns().CheckLocalip()