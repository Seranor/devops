import logging
from rest_framework.views import exception_handler
from rest_framework.response import Response

logger = logging.getLogger("django")


def custom_exception_handler(exc, context):
    """
    自定义异常处理
    :param exc: 异常类实例对象
    :param context: 抛出异常的执行上下文[context，是一个字典格式的数据，里面记录了异常发生时的环境信息]
    :return: Response 响应对象
    """
    # 先让drf内置的异常处理函数先解决掉它能识别的异常
    res = exception_handler(exc, context)
    if res:
        res = Response(data={'code': 998, 'msg': res.data.get('detail', '服务器异常，请联系系统管理员')})
    else:
        res = Response(data={'code': 999, 'msg': str(exc)})
    request = context.get('request')
    view = context.get('view')
    logger.error('错误原因：%s,错误视图类：%s,请求地址：%s,请求方式：%s' % (str(exc), str(view), request.path, request.method))
    return res
