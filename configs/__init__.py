import os

from configs.base_setting import *

flask_env = os.getenv('FLASK_ENV')
print('FLASK_ENV: %s' % flask_env)

if flask_env == "PROD":
    print('Loading config: PROD')
    from configs.prod_setting import *
else:
    print('Loading config: DEV')
    from configs.dev_setting import *