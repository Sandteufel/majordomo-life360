# majordomo-life360
ВАЖНО!
 По факту это костыли, которые позволяют путем запуска из крона скрипта на python вытянуть из life360 нужные данные о друзьях. Официально сервис не имеет api, но оно есть и как долго будет работать не понятно.

данные которые по средстам этого api вытягиваются:

В самом скрипте life360toMJD.py нужно внести данные:
1. Ваш логин и пароль на сервис life360 (строчки 15 и 16)
2. адрес сервера, на котором крутится сервер (если скрипт запускается на другом сервере)
 или оставить как есть локалхост

 Да, вопросы защиты логина/пароля не рассматриваются, так как сервер с majordomo крайне уязвим и должен быть закрыт в локальной сети.
