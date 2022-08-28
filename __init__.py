#from nonebot.plugin import PluginMetadata

from .__main__ import *  # type:ignore

__zx_plugin_name__ = "BAWiki"
__plugin_usage__ = """
usage:
    碧蓝档案Wiki插件
    指令：
        ba日程表
        ba学生图鉴
        ba新学生
        baL2D
        ba羁绊
""".strip()
__plugin_des__ = '碧蓝档案Wiki插件'
__plugin_type__ = ('一些工具',)
__plugin_author__ = 'lgc2333'
__plugin_cmd__ = ['ba日程表', 'ba学生图鉴', 'ba新学生', 'baL2D', 'ba羁绊']
__plugin_settings__ = {
    "level": 5,  # 群权限等级，请不要设置为1或999，若无特殊情况请设置为5
    "default_status": True,  # 进群时的默认开关状态
    "limit_superuser": False,  # 开关插件的限制是否限制超级用户
    "cmd": __plugin_cmd__,  # 命令别名，主要用于帮助和开关
    "cost_gold": 0,  # 该功能需要花费的金币
}
__version__ = "0.3.0"
'''
__plugin_meta__ = PluginMetadata(
    name="BAWiki",
    description="碧蓝档案Wiki插件",
    usage="见下表",
    extra={
        "menu_data": [
            {
                "func": "日程表",
                "trigger_method": "指令",
                "trigger_condition": "ba日程表",
                "brief_des": "查看活动日程表",
                "detail_des": "查看当前未结束的卡池、活动以及起止时间",
            },
            {
                "func": "学生图鉴",
                "trigger_method": "指令",
                "trigger_condition": "ba学生图鉴",
                "brief_des": "查询学生详情",
                "detail_des": "访问对应学生Wiki页面并截图，支持部分学生别名\n"
                              "指令示例：<ft color=(238,120,0)>ba学生图鉴 白子</ft>；<ft color=(238,120,0)>ba学生图鉴 xcw</ft>",
            },
            {
                "func": "新学生导航",
                "trigger_method": "指令",
                "trigger_condition": "ba新学生",
                "brief_des": "快速查询当期UP学生",
                "detail_des": "快速查询各日服、国际服当前UP学生简介与国际服下期预测UP",
            },
            {
                "func": "Live2D预览",
                "trigger_method": "指令",
                "trigger_condition": "baL2D",
                "brief_des": "查看学生的Live2D看板",
                "detail_des": "查看指定学生的Live2D回忆大厅预览图（可能为gif），支持部分学生别名\n"
                              "可以用这些指令触发："
                              "<ft color=(238,120,0)>bal2d</ft>；<ft color=(238,120,0)>baL2D</ft>；"
                              "<ft color=(238,120,0)>balive2d</ft>；<ft color=(238,120,0)>baLive2D</ft>\n"
                              "指令示例：<ft color=(238,120,0)>bal2d xcw</ft>",
            },
            {
                "func": "羁绊查询",
                "trigger_method": "指令",
                "trigger_condition": "ba羁绊",
                "brief_des": "查询学生解锁L2D需求的羁绊等级",
                "detail_des": "使用学生名称查询该学生解锁L2D看板需求的羁绊等级以及L2D预览，"
                              "或者使用羁绊等级级数查询哪些学生达到该等级时解锁L2D看板\n"
                              "使用学生名称查询时支持部分学生别名\n"
                              "可以用这些指令触发："
                              "<ft color=(238,120,0)>ba羁绊</ft>；<ft color=(238,120,0)>ba好感度</ft>\n"
                              "指令示例：<ft color=(238,120,0)>ba羁绊 xcw</ft>；<ft color=(238,120,0)>ba羁绊 9</ft>",
            },
        ],
        "menu_template": "default",
    },
)
'''
