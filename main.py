# -*- coding: utf-8 -*-
# Date:2021/5/21 3:01 下午


"""
待处理，实现多租户权限，
优先处理，账号创建等权限处理

# """
from core.server import create_app

api_router = create_app()

if __name__ == '__main__':
    import uvicorn
    # for i in api_router.routes:
    #     if hasattr(i, "methods"):
    #         print({'path': i.path, 'name': i.name, 'methods': i.methods})
    uvicorn.run(app=api_router, host="0.0.0.0", port=80)


#class ApanError(Exception):
#    def __init__(self, err_desc: str = "Permission denied"):
#        self.err_desc = err_desc
#
#    def __str__(self):
#        return self.err_desc


#if True:
#    raise ApanError()

