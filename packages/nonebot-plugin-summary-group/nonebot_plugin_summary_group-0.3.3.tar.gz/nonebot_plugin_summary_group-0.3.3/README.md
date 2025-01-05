# nonebot_plugin_summary_group

## 📖 介绍

基于Nonebot2，使用Gemini分析群聊记录，生成讨论内容的总结。

## 💿 安装

使用nb-cli安装插件

```shell
nb plugin install nonebot_plugin_summary_group
```

使用pip安装插件

```shell
pip install nonebot_plugin_summary_group
```

## ⚙️ 配置

在机器人文件夹的`env`文件中添加下表中配置项。

|       配置项       | 必填  |       默认       |      说明      |
| :----------------: | :---: | :--------------: | :------------: |
|     gemini_key     |  是   |       None       | gemini接口密钥 |
|   summary_model    |  否   | gemini-1.5-flash | gemini模型名称 |
|       proxy        |  否   |       None       |    代理设置    |
| summary_max_length |  否   |       2000       |  总结最大长度  |
| summary_min_length |  否   |        50        |  总结最小长度  |
| summary_cool_down  |  否   |        0         |  总结冷却时间  |

## 🕹️ 使用

**总结 [消息数量]** ：生成该群最近消息数量的内容总结

**总结 [@群友] [消息数量]** ：生成指定群友相关内容总结

注：默认总结消息数量范围50~2000，使用无冷却时间
