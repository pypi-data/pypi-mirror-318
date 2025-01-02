from celery import Celery

import config
from config import annotation

celery = Celery('tasks')
celery.config_from_object('cloudcelery.celery_config')
celery.conf.timezone = 'Asia/Shanghai'
celery.conf.setdefault('CELERY_DEFAULT_QUEUE', config.actor_name)  # 关心的是actor_name类型的任务

try:
    concurrent_count = annotation.get_value("${celery.concurrency:1}")
except:
    concurrent_count = 1
celery.conf.setdefault('CELERYD_CONCURRENCY', concurrent_count)  # 设置任务并发数,默认是1

# 这里增加一个这个配置,改成12小时,默认情况下redis做后端会有一个1小时的默认超时时间,也就是放到unacked的任务,一个小时就会被重新放入到task队列中. @see https://docs.celeryproject.org/en/stable/getting-started/backends-and-brokers/redis.html#redis-caveats
celery.conf.broker_transport_options = {'visibility_timeout': 43200}
celery.conf.result_backend_transport_options = {'visibility_timeout': 43200}

redis_url: str = annotation.get_value("${redis.url:}")

if redis_url is None or redis_url.strip() == '':
    # 说明是新的格式
    database = annotation.get_value("${spring.data.redis.database:0}")
    password = annotation.get_value("${spring.data.redis.password:}")
    nodes = annotation.get_value("${spring.data.redis.sentinel.nodes:}")
    if nodes is None or nodes == '':
        # 说明是单机
        host = annotation.get_value("${spring.data.redis.host:}")
        # 说明是单机
        url = f'redis://{f":{password}@" if (password is not None and password != "") else ""}{host}/{database}'
    else:
        # 说明是哨兵
        master = annotation.get_value("${spring.data.redis.sentinel.master:}")
        split = nodes.split(",")
        url = ";".join(
            [
                f'sentinel://{f":{password}@" if (password is not None and password != "") else ""}{url}/{database}'
                for
                url in split])
        celery.conf.broker_transport_options['master_name'] = master
        celery.conf.result_backend_transport_options['master_name'] = master
else:
    try:
        redis_password = annotation.get_value("${redis.password:}")
    except:
        redis_password = None

    try:
        redis_database = annotation.get_value("${redis.database:0}")
    except:
        redis_database = 0

    # 选择redis类型的缓存时,redis服务器的地址 格式为: ip:port
    # 现在支持了redis3-cluster,多个IP使用逗号分割
    # 现在支持了redis3-sentinel哨兵模式,使用分号分割. 第一个表示主节点名字. MASTERNAME;哨兵IP1:PORT1;哨兵IP2:PORT2;哨兵IP3:PORT3的方式
    if "," in redis_url:
        # 说明是redis-cluster 那么就要初始化集群
        raise NotImplementedError("celery还不支持,see: https://github.com/celery/kombu/pull/1021")
    elif ";" in redis_url:
        # 说明是哨兵形式的主从集群
        # app.conf.broker_url = 'sentinel://localhost:26379;sentinel://localhost:26380;sentinel://localhost:26381'
        # app.conf.broker_transport_options = {'master_name': "cluster1"}
        split = redis_url.split(";")
        sentinel = split[0]
        split.remove(sentinel)
        url = ";".join(
            [
                f'sentinel://{f":{redis_password}@" if (redis_password is not None and redis_password != "") else ""}{url}/{redis_database}'
                for
                url in split])
        celery.conf.broker_transport_options['master_name'] = sentinel
        celery.conf.result_backend_transport_options['master_name'] = sentinel

        # 2023-01-06 18:38:42  在哨兵的模式下, kombu-transport-redis 里面在 _get_pool的时候(1145行)的时候,并没有像在单机的情况下一样
        #  执行了 self.keyprefix_fanout = self.keyprefix_fanout.format(db=params['db']) 方法, 哨兵模式下并没有. 我觉得这应该是一个BUG
        #  好在,他为了兼容celery4.0以下的版本,在构造函数__init__()中,判断了外部的参数输入(512行), 也就是在transport_options中能手动指定fanout_prefix参数,
        #  作为self.keyprefix_fanout的值,也就是最前面的/{db}. 进行替换.从而解决了问题
        celery.conf.broker_transport_options['fanout_prefix'] = f"/{redis_database}."
        celery.conf.result_backend_transport_options['fanout_prefix'] = f"/{redis_database}."
    else:
        # 说明是单机
        url = f'redis://{f":{redis_password}@" if (redis_password is not None and redis_password != "") else ""}{redis_url}/{redis_database}'

celery.conf.broker_url = url  # 中间件
celery.conf.result_backend = url  # 结果存储

# 这里为了监控,需要再连接一个redis
from redis import Redis


def celery_redis_client() -> Redis:
    return celery.backend.client
