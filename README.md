# cloudmgr
```
git clone git@github.com:mason105/case8771388691.git  
cd ./case8771388691   
pip3 install -r ./requirements.txt  

chalice local  
```
then visit http://127.0.0.1:8000 
you got hello world, every thins is ok

ctrl - C close this command.
```
chalice deploy  
```
than visit the API deployed on Aws,Everything is fine.

------------------------------------------
the follwing shows how to repeat the problom
```
mv ./chalicelib/alibabacloud_ecs20140526_models.py ./chalicelib/alibabacloud_ecs20140526_models_working.py  
mv ./chalicelib/alibabacloud_ecs20140526_models_not_working.py ./chalicelib/alibabacloud_ecs20140526_models.py  
chalice local  
```
then visit http://127.0.0.1:8000 
you got hello world, everythins is still fine

However:
```
chalice deploy 
```
than visit the API deployed on Aws
you will get timeout error



----------------------------------------
so i think this difference between ./chalicelib/alibabacloud_ecs20140526_models.py and ./chalicelib/alibabacloud_ecs20140526_models_not_working.py. cause the problem. I think the the file size may casue the problem.

alibabacloud_ecs20140526_models_not_working.py. contains more class

|        | alibabacloud_ecs20140526_models   | alibabacloud_ecs20140526_models_not_working.py   |
|  ----  | ----  |----  |
| file Size  | 830k  |2.5M  |
| chalice local  | Worked | Worked |
| chalice deploy  | Worked |Not work |
|  ----  | ----  |----  |

