from core.core import BaseError
from core.core import return_data

class Error(BaseError):

    @staticmethod
    def mobile_null_error():
        return return_data(code=-100, msg=u'手机号不能为空')

    @staticmethod
    def password_null_error():
        return return_data(code=-101, msg=u'密码不能为空')

    @staticmethod
    def account_status_close():
        return return_data(code=-102, data={'phone':'01056216855'}, msg=u'抱歉，您的账号已经被冻结\n如有疑问请联系客服010-56216855')

    @staticmethod
    def account_not_exist():
        return return_data(code=-103, msg=u'账号不存在')

    @staticmethod
    def invalid_verify_code():
        return return_data(code=-104, msg=u'验证码错误')

    @staticmethod
    def invalid_account_password():
        return return_data(code=-105, msg=u'账号不存在或密码错误')

    @staticmethod
    def verify_code_null():
        return return_data(code=-106, msg=u'验证码不能为空')

    @staticmethod
    def user_info_null():
        return return_data(code=-107, msg=u'用户信息不存在')

    @staticmethod
    def user_update_fail():
        return return_data(code=-108, msg=u'更新用户资料失败')

    @staticmethod
    def verify_code_app_key_null():
        return return_data(code=-109, msg=u'验证码appkey不能为空')

    @staticmethod
    def verify_code_verify_type_null():
        return return_data(code=-110, msg=u'验证码verifyType不能为空')

    @staticmethod
    def verify_code_sms_limit():
        return return_data(code=-111, msg=u'短信验证码请求超过上限，请使用语音验证码')

    @staticmethod
    def change_identity_fail():
        return return_data(code=-112, msg=u'用户身份选择失败')

    @staticmethod
    def reset_password_fail():
        return return_data(code=-113, msg=u'重置密码失败')

    @staticmethod
    def account_null():
        return return_data(code=-114, msg=u'账号不能为空')

    @staticmethod
    def verify_code_limit():
        return return_data(code=-115, msg=u'验证码请求超过上限，请明天再试')

    @staticmethod
    def password_null():
        return return_data(code=-116, msg=u'您的账号没有设置密码\n请使用验证码进入')

    @staticmethod
    def update_company_permission():
        return return_data(code=-117, msg=u'您没有修改公司权限')

    @staticmethod
    def company_no_repetition_binding():
        return return_data(code=-118, msg=u'该用户已绑定其它公司\n不能再绑定')

    @staticmethod
    def verify_code_past_due():
        return return_data(code=-119, msg=u'验证码错误')

    @staticmethod
    def verify_code_voice_limit():
        return return_data(code=-120, msg=u'语音验证码请求超过6次')

    @staticmethod
    def save_fail():
        return return_data(code=-121, msg=u'保存信息失败')

    @staticmethod
    def get_fail():
        return return_data(code=-122, msg=u'获取信息失败')

    @staticmethod
    def upload_fail():
        return return_data(code=-123, msg=u'上传失败')

    @staticmethod
    def send_job_fail():
        return return_data(code=-124, msg=u'很遗憾，贵公司今天已经发布20个职位，请明天再来吧！')

    @staticmethod
    def enterprise_send_job_fail():
        return return_data(code=-125, msg=u'您的账号尚未认证，认证后才能发布更多职位喔！')

    @staticmethod
    def old_password_fail():
        return return_data(code=-126, msg=u'旧密码错误')

    @staticmethod
    def old_password_null():
        return return_data(code=-127, msg=u'原密码不能为空')

    @staticmethod
    def password_type_error():
        return return_data(code=-128, msg=u'修改密码类型不正确')

    @staticmethod
    def resume_not_full():
        return return_data(code=-130, msg=u'简历信息不完整')

    @staticmethod
    def reserved_repeated():
        return return_data(code=-131, msg=u'你已申请过，不能重复申请')

    @staticmethod
    def no_point():
        return return_data(code=-132, msg=u'抱歉，账户余额不足\n可赚取积分或联系我们（010-56216855）充值M币')

    @staticmethod
    def limit_call_phone():
        return return_data(code=-133, msg=u'拨打电话超过上限')

    @staticmethod
    def limit_im_unautherized_count():
        return return_data(code=-135, msg=u'很抱歉，认证后才能与更多候选人主动发起沟通')

    @staticmethod
    def can_not_cancel_hr_auth():
        return return_data(code=-136, msg=u'您的认证已通过\n不可取消认证')


    #所有时段都已预约已满
    @staticmethod
    def reserved_full():
        return return_data(code=-139, msg=u'该职位预约已满\n去看看更多好职位吧')

    #报错时，和可预约时段为0时
    @staticmethod
    def session_overdue():
        return return_data(code=-139, msg=u'非常遗憾！\n该职位没有可预约的场次\n去看看更多好职位吧')

    # 过期，还有其他场次可预约
    @staticmethod
    def has_effective_session():
        return return_data(code=-140, msg=u'该时段面试已经开始\n换个时段吧')

    # 已满，还有其他场次可预约
    @staticmethod
    def has_effective_session2():
        return return_data(code=-141, msg=u'该时段面试预约已满\n换个时段吧')

    # 已暂停，还有其他场次可预约
    @staticmethod
    def no_session_reserve2():
        return return_data(code=-172, msg=u'该时段面试已暂停\n换个时段吧')

    # 已取消，还有其他场次可预约
    @staticmethod
    def cancel_has_session():
        return return_data(code=-171, msg=u'该时段面试已取消\n换个时段吧')

    # 没有可预约的时段
    @staticmethod
    def no_session_reserve():
        return return_data(code=-170, msg=u'没有可预约的时段\n去看看更多好职位吧')

    @staticmethod
    def verify_code_risk_limit():
        return return_data(code=-142, data={'phone':'01056216855'}, msg=u'验证码请求超出上限，如您需要紧急登录请联系客服（010-56216855）')

    @staticmethod
    def invalid_image_verify_code():
        return return_data(code=-143, msg=u'请先输入正确的图片验证码')

    @staticmethod
    def update_mobile_error():
        return return_data(code=-144, msg=u'手机号码已经存在')

    @staticmethod
    def mobile_exist_error():
        return return_data(code=-145, msg=u'手机号码已经存在')

    @staticmethod
    def created_job_error():
        return return_data(code=-146, msg=u'请勿发布重复职位')

    @staticmethod
    def backend_system_error():
        return return_data(code=-147, msg=u'后台系统异常')

    @staticmethod
    def verify_code_limit2():
        return return_data(code=-148, data={'phone':'01056216855'}, msg=u'验证码请求超过上限，请明天尝试\n如需紧急修改手机号码，请联系客服（010-56216855）')

    @staticmethod
    def verify_code_risk_limit2():
        return return_data(code=-149, data={'phone': '01056216855'}, msg=u'验证码请求超过上限，请明天尝试\n如需紧急修改手机号码，请联系客服（010-56216855）')

    @staticmethod
    def verify_code_risk_limit3():
        return return_data(code=-150, data={'phone': '01056216855'},
                           msg=u'验证码请求超过上限，请明天尝试\n如需紧急修改密码，请联系客服（010-56216855）')

    @staticmethod
    def invalid_uuid_code():
        return return_data(code=-151, msg=u'二维码过期')

    @staticmethod
    def get_resume_error():
        return return_data(code=-152, msg=u'获取简历失败')

    @staticmethod
    def invalid_uuid_key():
        return return_data(code=-153, msg=u'校验参数不合法')

    @staticmethod
    def get_question_error():
        return return_data(code=-154, msg=u'获取答题失败')

    @staticmethod
    def get_company_error():
        return return_data(code=-155, msg=u'获取公司失败')

    @staticmethod
    def delete_resume_error():
        return return_data(code=-156, msg=u'删除简历失败')

    @staticmethod
    def send_email_error():
        return return_data(code=-157, msg=u'发送邮件失败')

    @staticmethod
    def no_flow_ok():
        return return_data(code=-158, msg=u'没有需要确认的面试')

    @staticmethod
    def get_company_list_error():
        return return_data(code=-159, msg=u'获取公司列表信息失败')


    @staticmethod
    def get_advisor_seror():
        return return_data(code=-160, msg=u'获取顾问信息失败')

    @staticmethod
    def get_postion_seror():
        return return_data(code=-161, msg=u'获取职位信息失败')


    @staticmethod
    def no_career_Area():
        return return_data(code=-163, msg=u'求职期望城市为空')

    @staticmethod
    def no_gender():
        return return_data(code=-164, msg=u'性别为空')

    @staticmethod
    def get_survey_answer_error():
        return return_data(code=-165, msg=u'获取答题失败')

    @staticmethod
    def open_red_packet_error():
        return return_data(code=-166, msg=u'打开红包失败')

    @staticmethod
    def user_payment_error():
        return return_data(code=-167, msg=u'提现失败')

    @staticmethod
    def user_wechat_mapping_error():
        return return_data(code=-167, msg=u'微信绑定失败')

    @staticmethod
    def withdraw_filed_fail():
        return return_data(code=-167, msg=u'提现失败')

    @staticmethod
    def withdraw_filed_not_enouth():
        return return_data(code=-160, msg=u'余额小于20，不可提现，继续努力吧！')

    @staticmethod
    def create_resume_error():
        return return_data(code=-168, msg=u'创建简历失败')

    @staticmethod
    def upload_number_error():
        return return_data(code=-169, msg=u'上传简历数量超过限制')