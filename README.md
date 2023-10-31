# 基于Mixamo插件来实现自动绑定动作 #

## 去Mixamo官网下载动作 ##
*如果是A-Pose，需要先上传一个A动作的模型*
* 1.Upload Character

*如果是T-Pose 则直接下载*
* 2.Animations选择动作下载(Format：Fbx for unity(.fbx)/Skin： Without Skin)

## 下载完后请用ReadFileList.py来获取模型和动作的List名字 ##
* 1.在folder_path中选择需要读取的文件地址
* 2.将读取的personList和action分别填入Auto.py的List中
* 3.修改读取和输出的地址

## 导入Mixamo插件 ##
### 插件地址：https://substance3d.adobe.com/plugins/mixamo-in-blender/ ###
* 详细见Blender插件导入方法
* 用Blender中的script或者.sh来运行Auto.py