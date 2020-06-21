#主函数
import besideH
import chinaAllprovince
import dataSource
import Hubei

print('正在获取数据……')
dataSource.saveData()   # 将源数据储存在datasource中
print('已将获取数据存储……')
print('正在保存全国省份源数据……')
chinaAllprovince.getChinaallpro()   # 保存全国省地区数据
print('已保存数据……')
print('正在保存湖北省份数据……')
Hubei.getHubei()    # 保存湖北数据
print('已保存湖北省份数据……')
print('正在保存非湖北省各市数据……')
besideH.getBesideHu()   # 保存非湖北数据
print('已保存非湖北各省份数据……')




