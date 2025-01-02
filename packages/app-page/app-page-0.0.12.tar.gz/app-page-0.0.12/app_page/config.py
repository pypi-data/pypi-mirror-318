import os

def createPath(name):
  return os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", name)

tips_ui = createPath("tips.ui")
tipsBox_ui = createPath("tipsBox.ui")
MainWindow_ui = createPath("main.ui")
loading_icon = createPath("loading.gif")
small_page_icon = createPath("small_page.png")
maximize_page_icon = createPath("maximize_page.png")

# 定义软件当前版本
APP_VERSION = '1.0.0'
APP_TITLE = '小灰妙记'
APP_ICON_PATH = createPath('favicon.png')

IS_DEBUG = False        #生产环境，使用远程服务器

PING_HOST = 'greatnote.cn'
BASE_IP = '116.205.226.236'