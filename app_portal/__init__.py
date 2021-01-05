from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


import configs
from core.check_param import SubCheckParam
from core.zyz_flask import ZyzFlask, ZyzBlueprint
from configs import DEFAULT_METHODS
from core.core import check_param


app = ZyzFlask(__name__)
app.config.from_object(configs)
CORS(app)
db = SQLAlchemy(app)


root = ZyzBlueprint('root', __name__,default_methods=DEFAULT_METHODS)
inner = ZyzBlueprint('inner', __name__,default_methods=DEFAULT_METHODS)
outer = ZyzBlueprint('outer', __name__,default_methods=DEFAULT_METHODS)
manager = ZyzBlueprint('manager', __name__,default_methods=DEFAULT_METHODS)
owner = ZyzBlueprint('owner', __name__,default_methods=DEFAULT_METHODS)
member = ZyzBlueprint('member', __name__,default_methods=DEFAULT_METHODS)
third = ZyzBlueprint('third', __name__,default_methods=DEFAULT_METHODS)
offline = ZyzBlueprint('offline', __name__,default_methods=DEFAULT_METHODS)


app.register_blueprint(root)
app.register_blueprint(inner, url_prefix='/inner')
app.register_blueprint(outer, url_prefix='/outer')
app.register_blueprint(manager, url_prefix='/manager')
app.register_blueprint(owner, url_prefix='/owner')
app.register_blueprint(member, url_prefix='/member')
app.register_blueprint(third, url_prefix='/third')
app.register_blueprint(offline, url_prefix='/offline')


check_root = SubCheckParam(DEFAULT_METHODS)
check_inner = SubCheckParam(DEFAULT_METHODS)
check_outer = SubCheckParam(DEFAULT_METHODS)
check_manager = SubCheckParam(DEFAULT_METHODS)
check_owner = SubCheckParam(DEFAULT_METHODS)
check_member = SubCheckParam(DEFAULT_METHODS)
check_third = SubCheckParam(DEFAULT_METHODS)

check_param.register_check_param(check_root)
check_param.register_check_param(check_inner, url_prefix='/inner')
check_param.register_check_param(check_outer, url_prefix='/outer')
check_param.register_check_param(check_manager, url_prefix='/manager')
check_param.register_check_param(check_owner, url_prefix='/owner')
check_param.register_check_param(check_member, url_prefix='/member')
check_param.register_check_param(check_third, url_prefix='/third')