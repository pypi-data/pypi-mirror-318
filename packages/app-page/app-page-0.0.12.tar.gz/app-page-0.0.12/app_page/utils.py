import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtWidgets import QWidget

def loadUI(filePath, target=None):
  ui_file = QFile(filePath)
  if not ui_file.open(QIODevice.ReadOnly):
    print(f"cannot open {filePath}")
    sys.exit(-1)
  if target:
    return QUiLoader(target).load(ui_file)
  else:
    return QUiLoader().load(ui_file)


def setWidgetStyle(widget:QWidget, style:dict|list, id=None, cover:bool = False):
  
  if isinstance(style, list):
    style = cascading_styles(*style)
  
  config = {"styleSheetList":[]}
  try:
    if not cover:
      config["styleSheetList"] = widget.styleSheet().split('\n')
  except:
    pass

  if id:
    ret = f'#{id}'+'{'+ ";".join([key+":"+style[key] for key in style.keys()]) + '}'
  else:
    ret = ";".join([key+":"+style[key] for key in style.keys()])
  config["styleSheetList"].append(ret)
  style_str = '\n'.join(config["styleSheetList"])
  widget.setStyleSheet(style_str)

def cascading_styles(*args):
  """
  级联样式
  """
  style = {}
  for arg in args:
    if isinstance(arg, dict):
      for key in arg.keys():
        style[key] = arg[key]
    else:
      pass
  return style


def layout_clear(layout):
  while layout.count():
    child = layout.takeAt(0)
    if child.widget() is not None:
      # print("delete widget", child.widget())
      child.widget().deleteLater()
    elif child.layout() is not None:
      # layout_clear(child.layout())
      print("delete layout", child.layout())
      child.layout().deleteLater()