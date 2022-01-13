# NHD_SIGNIN

- 基于Github Actions
- 每天北京时间12：00进行自动签到
- 可用[Server酱](https://sc.ftqq.com/)进行结果推送

## 使用说明

fork本项目到自己的仓库。

在secrets里添加五个仓库，分别取名为：
- WEBVPNACCOUNT
- WEBVPNPASSWORD
- NHDACCOUNT
- NHDPASSWORD
- SCKEY

启用action。

可以通过点击star测试项目。

## 各仓库的作用

### webvpn

由于NHD非ipv6外网无法访问，因此需要我们登录webvpn，在WEBVPNACCOUNT与WEBVPNPASSWORD两个仓库内分别输入校园网账号与密码。

### NHD

在NHDACCOUNT与NHDPASSWORD两个仓库内分别输入nexus hd账号、密码。如果你有多个账号需要签到，可以将他们用!（注意是半角字符）间隔，实现多账号签到。

例如，账号A用户名为abc，密码为123；账号B用户名为def，密码为456。那么你应该如下填写仓库内容：
- NHDACCOUNT
  - abc!def
- NHDPASSWORD
  - 123!456

### SCKEY（可选择）

作用是进行微信推送，在该仓库内填写上方Server酱网站得到的SCKEY即可。
