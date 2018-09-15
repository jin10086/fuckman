# 渣人识别

## 原理

通过手机号去各种约p软件测试。

如果提示**该手机号已经注册** 或者 **该手机号已经存在**，则表示ta在使用该软件.

![](media/momo.png)

## 对项目感兴趣？

- [你可以提交新的平台](https://github.com/jin10086/slagManMonitor/issues/new)
- [查看issue](https://github.com/jin10086/slagManMonitor/issues),可以帮忙添加新的平台监测代码(写之前记得先在issue内说下哦，以免重复)

### 如何添加新的平台代码
1. fork本项目
2. 在指定issue内认领任务
3. copy `apps/momo.py`代码，把他改成你要写的平台名字。如 `tantan.py`
4. `tantan.py`要求:
    - 一定要实现**run** 方法,输入的是一个手机号.
    - 日志 和 momo.py 一样
5. 写完测试没有问题后,在`apps/__init__.py` 导入你的类
6. pull request


## buy me a coffee

如果你觉得这个项目还不错，对你有一些帮助，可以请我喝杯咖啡，想必也是非常愉悦的事情。 😄

[buy-me-a-coffee](https://jin10086.github.io/buy-me-a-coffee/)

## 那么多软件从哪来的?

看下图水印...

![](media/apps.jpeg)


