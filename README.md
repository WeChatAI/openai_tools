# 微信对话开放平台开发辅助工具
微信AI团队，深圳腾讯科技股份有限公司

### 准确率评估：calculateAccuracy.py

**使用方法**

python calculateAccuracy.py \<APPID> \<TOKEN> \<EncodingAESKey> \<InputFile>

**参数**
1. APPID，TOKEN，EncodingAESKey可从平台申请获取（机器人设置->服务接入->其他接入方式->开放接口申请）；
2. InputFile：测试文件，多行，每行为一个测试样例（一个测试样例包括用户query和其应命中的意图，二者用TAB字符隔开）。
