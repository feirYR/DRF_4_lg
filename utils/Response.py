from rest_framework.response import Response

class MyResponse(Response):
    def __init__(self,status=200,message=0,results=None,http_status=None,headers=None,exception=False,**kwargs):
        data={
            'status':status,
            'message':message
        }

        if results:
            data['results']=results
        # print('自定义响应', kwargs)
        data.update(kwargs)

        super().__init__(status=http_status,data=data,headers=headers,exception=exception)