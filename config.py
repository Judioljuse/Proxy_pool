# Redis数据库的地址和端口
REDIS_HOST = 'localhost'
REDIS_PORT = '6379'

# 如果Redis有密码，则添加这句密码，否则设置为None或''
REDIS_PASSWORD = ''

# Redis Key
REDIS_KEY = 'proxies'

# 获得代理测试时间界限
get_proxy_timeout = 9

# 代理池数量界限
POOL_UPPER_THRESHOLD = 10000

#批量测试最大值
BATCH_TEST_SIZE = 100

# 测试分数
MAX_SCORE = 100        #最大分数
MIN_SCORE =0           #最小分数
INITIAL_SCORE = 10     #初始分数

# 检查周期
VALID_CHECK_CYCLE = 60
POOL_LEN_CHECK_CYCLE = 20

# 测试URL
TEST_URL = 'https://movie.douban.com/'

#响应码
VALID_STATUS_CODES = [200]