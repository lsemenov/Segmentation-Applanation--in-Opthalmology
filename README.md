<div align="center">


<img width="20%" src="https://github.com/lsemenov/Segmentation-Applanation--in-Opthalmology/blob/master/demo/Mtuci_logo.png" />



</div>

## Приложение для сегментации медицинских офтальмологических изображений
Приложение определяет контур аппланации. Аппланация – область роговицы, находящаяся под уплощением. В дальнейшем информация о границах аппланации используется для сигнализирования хирургу о возможных границах операции. 
Основной эффект, который планируется достичь с помощью приложения, состоит в более качественном оказании медицинских услуг по коррекции зрения.

1. **Модель глубокого обучения (CNN U-net)** архитектура U-net обеспечивает очень хорошую производительность в биомедицинских сегментациях.
Для обучения необоходимы размеченый датасет 
датасет медицинских изображений
<br>
<div align="center">


<img width="24%" src="https://github.com/lsemenov/Segmentation-Applanation--in-Opthalmology/blob/master/demo/data1.png" />
<img width="28%" src="https://github.com/lsemenov/Segmentation-Applanation--in-Opthalmology/blob/master/demo/mask1.png" />


</div>
<br>

2. **Веб приложение на основе Python с использованием Flask** располагается на Yandex Cloud Compute http://158.160.54.241/. 
Требуется загрузить изображение и воспользоваться функционалом "сегментирования", на выходе приложение определяет область аппланации ввиде наложенной маски на исходное изображение.

<br>
<div align="center">


<img width="24%" src="https://github.com/lsemenov/Segmentation-Applanation--in-Opthalmology/blob/master/demo/result1.png" />


</div>
<br>

### Развертываниe

<details>
  <summary>Windows installation guides</summary>
 
  **For windows users we offer to compete with our trained RL agent. Main goal is to collect a reward for running up to the stones at the frame for the same number of steps. Good luck, have fun!**
  
  #### *Первичный запуск*
  __1. В командной строке CMD: dowland or clone this GitHub repository__
  
  __2. Создайте проект в PyCharm или создайте виртуальное окружение и установите содержимое файла requirements.txt__
  
  ```
  python create -n survivio_venv python=3.8
  python activate survivio_venv
  python -m pip install -r requirements.txt
  ```
  
  __3. Запустите приложение__
  ```
  python app.py
  ```
  
  #### *Использование*
  __1. Активируйте виртуальное окружение__
  ```
  python activate survivio_venv
  ``` 

  __2. Запустите приложение__
  ```
  python app.py
  ```
</details>

<details>
  <summary>Yandex Cloud Compute installation guides</summary>
  
  #### *Первичный запуск*
  __1. Создайте виртуальную машину в сервисе Yandex Cloud Compute с параметрами:__
  * CPU or GPU
  * RAM - 2Gb
  * HDD or SSD - 15Gb
  * Ubuntu 20-22
  
  
  __2. Подключитесь к виртуальной машине Yandex Cloud: в командной строке__
  
  ```
  ssh -i path_to_public_key/pub_key username@xx.xx.xx.xx 
  
  path_to_public_key - путь для ключа ssh
  username - пользователь с правами администратора
  xx.xx.xx.xx - выделенный публичный адрес
  
  sudo git clone repository

  ```
  
  __3. Установите docker-compose для Ubuntu__
  <br>
 Инструкция по установки Docker-compose: [ссылка](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-ru)
 
 __4. Создайте образ и запустите контейнер__
  
  
   ```
   cd Segmentation-Applanation--in-Opthalmology
   sudo docker-compose up -d

  ```
  
 __5. В адресной строке переходите xx.xx.xx.xx:80__
  
    #### *Использование*
    
  __1. Подключитесь к виртуальной машине Yandex Cloud: в командной строке__
  
  ```
  ssh -i path_to_public_key/pub_key username@xx.xx.xx.xx 
  
  path_to_public_key - путь для ключа ssh
  username - пользователь с правами администратора
  xx.xx.xx.xx - выделенный публичный адрес
  
  sudo git clone repository

  ```
  
  __2. Запустите контейнер с приложением__
  
  
   ```
   cd Segmentation-Applanation--in-Opthalmology
   sudo docker-compose up -d
  ```
  __3. В адресной строке переходите xx.xx.xx.xx:80__
  
</details>

### Команда
1. Alexey Semenov (CV, WEB) tg: @moon_resident
