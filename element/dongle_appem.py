#_*_encoding:GBK*_
# APP 定位元素文件
class app_element_position():
    # 更新提示
    APP_tips_but = "//*[@resource-id='com.hpplay.happycast:id/tips_window_btn']"
    # 设备列表 设备名称
    APP_devicename_txt = "//*[@resource-id='com.hpplay.happycast:id/device_name_tv'][contains(@text,'我家的乐播投屏')]"
    # 返回
    APP_brack_but = "//android.widget.ImageView[@content-desc='返回']"
    # 立即开始
    APP_start_but = "//*[@resource-id='android:id/button1'][contains(@text,'立即开始')]"
    # 电视投屏码
    TV_pinCode_tv = "//*[@resource-id='com.hpplay.happyplay.aw:id/pinCode_tv‘]"
    # 加号更多
    APP_castadd_but = "//*[@resource-id='com.hpplay.happycast:id/fragment_cast_add_ib']"
    # 投屏码投屏
    APP_castCode_but = "//*[@resource-id='com.hpplay.happycast:id/device_name_tv']"
    #手机相册
    APP_photo_but = "//*[@resource-id='com.hpplay.happycast:id/add_menu_photo_ll']"
    # 相片  /android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.ImageView
    APP_image_item = "//*[@resource-id='com.hpplay.happycast:id/image_item']"
    # 打开相片，投屏按钮
    APP_piccast_but = "//*[@resource-id='com.hpplay.happycast:id/right_ib']"
    # 本地视频
    APP_video_but = "//*[@resource-id='com.hpplay.happycast:id/add_menu_video_ll']"
    # 输入投屏码文本框
    APP_entercode_txt = "//*[@resource-id='com.hpplay.happycast:id/phone_cast_code_et']"
    # 连接提交按钮
    APP_connect_but = "//*[@resource-id='com.hpplay.happycast:id/phone_cast_connect_btn']"
    # 结束投屏
    APP_castconnect_but = "//*[@resource-id='com.hpplay.happycast:id/cast_stop_tv']"
    # 扫码投屏按钮
    APP_scanCode_but = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[2]"
    # 断开连接   com.hpplay.happycast:id/dis_connect_btn
    APP_disconnect_but = "//*[@resource-id='com.hpplay.happycast:id/dis_connect_btn'][contains(@text,'断开连接')]"
    # 我的
    # login
    # APP_wode_icon = "//*[@resource-id='com.hpplay.happycast:id/textview'][contains(@text,'断开连接')]"
    # 进入登录界面
    APP_login_but = "//*[@resource-id='com.hpplay.happycast:id/login_content_tv']"
    # 密码登录
    APP_pwd_icon = "//*[@resource-id='com.hpplay.happycast:id/pwd_ib']"
    #账号输入框
    APP_mobile_input = "//*[@resource-id='com.hpplay.happycast:id/mobile_et']"
    # 密码输入框
    APP_pwdword_input = "//*[@resource-id='com.hpplay.happycast:id/password_et']"
    # 登录按钮
    APP_loging_but = "//*[@resource-id='com.hpplay.happycast:id/btn_login']"
    # 设置按钮
    APP_setting_but = "//*[@resource-id='com.hpplay.happycast:id/mv_setting']"
    # 退出登录按钮
    APP_logout_but = "//*[@resource-id='com.hpplay.happycast:id/logout_tv']"
    # 确定退出
    APP_quit_but = "//*[@resource-id='com.hpplay.happycast:id/quit_define']"
    # 是否有公告的按钮
    APP_cement_but = "//*[@resource-id='com.hpplay.happycast:id/tips_window_btn']"
    # 用户登录状态
    APP_content_user = "//*[@resource-id='com.hpplay.happycast:id/vip_tv']"









