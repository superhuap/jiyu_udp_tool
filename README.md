# 此工具食用指南
---
## 这是个神马东西？
你可能已经知道了极域电子教室的学生端没有对数据包的发送者做身份验证。
所以使用此工具可以在机房里面猥琐欲为！

---
## 感谢以下作者

1. [zhiyiYo](https://github.com/zhiyiYo) PyQt-Fluent-Widgets的作者
2. [ht0Ruial](https://github.com/ht0Ruial) 编写数据包发送脚本的作者
---
## 如何食用？

1. 安装好依赖库。
```pip install "PyQt-Fluent-Widgets[full]" -i https://pypi.org/simple/```
- 我知道。在机房内要么没有python环境，要么没有wifi安装依赖库。
- 所以使用pyinstaller打包好的exe程序就好了！
2. 准备好一个txt文件放入一些ip，就像这样。
```
10.35.96.1 
10.35.96.5 
10.35.96.7
10.35.96.*
```
3. 打开软件，应该像下面一样。
![](/show/message.PNG)

4. 打开设置。
![](/show/setting.PNG)

5. 选择存放ip的txt文件。
6. 返回消息发送页面或命令发送页面。
7. 点击加载ip，就像下面一样。
![](/show/ip.PNG)
8. 为所欲为！！！！
---

# 功能介绍
- ## 消息发送
  - 以教师的身份发送消息
- ## 命令发送
  - 关机和重启 （废话）
  - 打开共享文件夹，启动smb共享（默认用户名=Administrator 默认密码=1）
  - 自定义输入shell命令
# 注意事项
- 设置页面参数建议动一下，提交一下
- 如果软件崩溃了可以提交issue
# 免责声明
- 如果你被发现或被举报与项目作者没有关系。