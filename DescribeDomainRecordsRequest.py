from aliyunsdkcore.request import RpcRequest
class DescribeDomainRecordsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alidns', '2015-01-09', 'DescribeDomainRecords')

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_UserClientIp(self):
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self,UserClientIp):
		self.add_query_param('UserClientIp',UserClientIp)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_RRKeyWord(self):
		return self.get_query_params().get('RRKeyWord')

	def set_RRKeyWord(self,RRKeyWord):
		self.add_query_param('RRKeyWord',RRKeyWord)

	def get_TypeKeyWord(self):
		return self.get_query_params().get('TypeKeyWord')

	def set_TypeKeyWord(self,TypeKeyWord):
		self.add_query_param('TypeKeyWord',TypeKeyWord)

	def get_ValueKeyWord(self):
		return self.get_query_params().get('ValueKeyWord')

	def set_ValueKeyWord(self,ValueKeyWord):
		self.add_query_param('ValueKeyWord',ValueKeyWord)