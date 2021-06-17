import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):

    @task
    def predict(self):
        data = '''{  
                    "CHAS":{  
                        "0":0
                    },
                    "RM":{  
                        "0":6.575
                    },
                    "TAX":{  
                        "0":296.0
                    },
                    "PTRATIO":{  
                        "0":15.3
                    },
                    "B":{  
                        "0":396.9
                    },
                    "LSTAT":{  
                        "0":4.98
                    }
                    }'''
        self.client.post("/predict", data=data, headers={"Content-Type": "application/json"} )