# 超级管理员登入/登出 功能模块 #
 
---

相关数据表模型结构 SysUser

定义文件: migrate/check.go



**数据库表结构**

| 字段 | 定义 | 描述 |
| ---- | ---- | ----| 
|id|mint(8)	unsigned auto_increment primary|自增ID|
|uname|varchar(30) not null unique|管理员登录名|
|upass|varchar(32) not null|管理员HASH后密码(util.SysPass后)|
|Ustat|int unsigned not null,default:1,|用户状态|
|CreatedAt| | GORM自带|
|UpdatedAt| | GORM自带|
|DeletedAt|index | GORM自带|

---

功能需求部分，请实现后并测试无误后，用实际简单文档插入到这里，将需求文档逐渐压到最后，完成全部测试后，删除需求文档。

**功能需求列表：**

1. 超级后台登入(区别于用户登入)
2. 超级后台登出
3. 超级用户修改本人密码

**详情：**

- ### 用户登入 ###

		URI: /superadm/login
		METHOD: POST
		Format: JSON
			username: (string)用户名明文
			password: (string)前端md5后的用户输入密码，过滤首尾空格
返回

		Format: JSON
		
		登录成功:
			result: (int) 1
		登录失败:
			result: (int) 0
			reason: (string) 失败详情
服务器端状态

		成功:
			Session: 
				生成并存入以下信息	: SuperID,SuperName
前端操作

		登录成功:
			Redirect: 跳转至超级用户后台首页静态页面
		登录失败:
			Alert提示后清空用户密码框，让用户重新填写
后端逻辑提示

		1. 判断登录应按用户名取回记录，采用util.SysPass方式HASH后进行比对
		2. 所有前后端传输密码均应在前端md5一次


- ### 用户登出 ###

		URI: /superadm/logout
		METHOD: POST
		Format: JSON
			c: (int) 一个随机数，大于0
			c2: (int) c的二倍
返回

		Format: JSON

		成功:
			result: (int) 1
		失败:
			result: (int) 0
服务器端状态

		成功:
			Session: 
				销毁	: SuperID,SuperName
		失败:
			不进行任何动作
前端操作

		成功:
			Redirect: 跳转至超级用户登录页
		失败:
			无操作

- ### 超级用户修改本人密码 ###
	
		URI: /superadm/password
			METHOD: POST
			Format: JSON
				oldpass: md5过的旧密码 密码明文时过滤首尾空格 
				newpass: md5过的新密码 密码明文时过滤首尾空格
返回

		Format: JSON

		成功:
			result: (int) 1
		失败:
			result: (int) 0
前端操作

		成功:
			提示成功
		失败:
			提示失败
前端提示

		新密码在前端输入两次验证一致，仅传给后端一个新密码
后端逻辑提示

		1. 要判断旧密码是否正确
		2. 所有前后端传输密码均应在前端md5一次
		3. 新密码应采用util.SysPass()加盐hash后入库