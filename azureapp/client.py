from azure.identity import ClientSecretCredential
# from azure.storage.queue import QueueClient
from azure.storage.queue.queue_client import QueueClient

class Client:
    def __init__(self, client, secret, tenant):
        self.client = client
        self.secret = secret
        self.tenant = tenant

    def get_token(self):
        credentials = ClientSecretCredential(client_id=self.client, secret=self.secret, tenant_id=self.tenant)
        return credentials


    def get_client_service(self, credentials):
        account_url = "https://storageinput/queue/core.windows.net"
        cred=self.get_token()
        client_obj = QueueClient(account_url=account_url, credentials=cred)
        print(client_obj)
