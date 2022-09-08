<h1 align="center"> 
    File Sharing Bot   
</h1>

<img align="center" fit="fill" alt="IMG" src="https://i.ibb.co/TbgRB3b/20220324-004130.jpg"/>

<h3 align="center"> 
    Telegram Bot File Sharing dengan 3 Force Subs Channel/Group
</h3>


<h2 align="center"> 
  Deploy Bot Di Virtual Private Server (VPS) 
</h2>

```console
debian@user:~$ sudo apt update && sudo apt upgrade -y
debian@user:~$ sudo apt install git -y && sudo apt install screen -y
debian@user:~$ screen -R BotFiles
debian@user:~$ sudo apt install python3-pip
debian@user:~$ git clone https://github.com/Xyren-1140/Mahasiswa-Ui
debian@user:~$ cd Mahasiswa-Ui
debian@user~$ pip3 install -r requirements.txt
debian@user:~$ cp contoh_config.env config.env

# <isi nilai yang ada di file config.env dengan cara nano config.env di terminal>
# <Setelah semua nilai terisi silahkan save file dengan cara ctrl+s lalu ctrl+x>

root@user:~$ python3 main.py

#Apabila Bot Berhasil diaktifkan Silahkan Close Screen dengan cara menekan ctrl+ad
```
 

<h2 align="center"> 
   Deploy Bot Di Heroku
</h2>


<h1>
    <p align="center">
        <a href="https://github.com/Mythia-X/Mahasiswa-Ui">
            <img src=https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)</br>
        </a>
    </p>
</h1>


### Credits

- Thanks To Dan For His Awsome [Libary](https://github.com/pyrogram/pyrogram)
- Thanks To [CodeXBotz](https://github.com/CodeXBotz/File-Sharing-Bot)
- Our Support Group Members

### Licence
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)  

[File-Sharing-Bot](https://github.com/CodeXBotz/File-Sharing-Bot) is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. 

##
