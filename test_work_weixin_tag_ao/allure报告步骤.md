###allure测试报告生成
####1-生成allure测试结果
pytest --alluredir=./result test_tag.py    
 
pytest test_tag.py --alluredir ./result2
#
####2-使用浏览器打开测试报告，生成最终的html
allure serve ./result                       #使用浏览器打开测试报告

allure generate ./result                    #生成html的目录（allure_report）

allure generate ./result2 -o result2        #指定路径

allure generate result --clean result/html -o result/html   #-o指定路径 --clean清除记录
#
####3-重新生成报告
pytest --alluredir=./result test_tag.py    #生成结果（此命令覆盖，追加勿用）

allure generate result --clean result/html -o result/html
#
####4-将两个测试文件生成测试报告
pytest test_a.py test_b.py --alluredir ./result4
（可以使用conftest.py文件对多个测试用例进行配置）

