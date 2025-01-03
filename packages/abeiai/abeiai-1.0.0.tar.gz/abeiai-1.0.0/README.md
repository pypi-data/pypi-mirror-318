# 阿贝智能开放平台的SDK

阿贝智能在应用过程中，踏遍了全世界各种资源，筛选了一批优秀的资源，计划陆续开放出来，让开发者更便捷的接入。

# 快速开始

## 安装

```bash
pip install abeiai
```

使用举例

```python
from abeiai.v1 import AbeiAI

ab = AbeiAI()
ab.set_app_id('xxx')
ab.set_app_secret('xxx')

# 查询价格方案
ab.group()
# 查消费
ab.history('xxx')
# 查充值记录
ab.recharge()
# 查信息
ab.app()
# 画图，字典内容见API文档
ab.draw({})
```

## 使用方式

具体参数内容见文档，请注意参数的格式。

传送门：[接口文档对照](https://abeiai123.feishu.cn/wiki/HPaAw7izuibperk2aSHcSMClnJh)

文档里有联系方式。

# 版本历史

1.0.0 首次发布

