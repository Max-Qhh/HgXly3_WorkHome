###allure���Ա�������
####1-����allure���Խ��
pytest --alluredir=./result test_tag.py    
 
pytest test_tag.py --alluredir ./result2
#
####2-ʹ��������򿪲��Ա��棬�������յ�html
allure serve ./result                       #ʹ��������򿪲��Ա���

allure generate ./result                    #����html��Ŀ¼��allure_report��

allure generate ./result2 -o result2        #ָ��·��

allure generate result --clean result/html -o result/html   #-oָ��·�� --clean�����¼
#
####3-�������ɱ���
pytest --alluredir=./result test_tag.py    #���ɽ����������ǣ�׷�����ã�

allure generate result --clean result/html -o result/html
#
####4-�����������ļ����ɲ��Ա���
pytest test_a.py test_b.py --alluredir ./result4
������ʹ��conftest.py�ļ��Զ�����������������ã�

