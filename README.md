<<<<<<< HEAD
# �й�ֱ�ӵ���jetson nano I2C�ӿ�����PCA9685�������˵��
~~��������⣬����ָ��~~
## jetson nano40����˵��
```doc
    jetson Nano�ϴ���40�����ţ��ֱ��в�ͬ�Ĺ��ܣ�������Ҫ�����˵�����е�I2C�ӿڣ�Jetson Nano����2��I2C�ӿڣ�һ���ӿ�ս�������ţ��ֱ���
    SDA,SCL����������λ�ֱ�������0��27��28 ����1��3��5 �ֱ��Ӧ��һ�����ߣ������������ѡ��5�ֹ���ģʽ��������˵��һ�£�SDA�������ߣ�
    �ں����Ե�ַ������Ϣʱ����Ҫ�õ��ߣ�SCL�ǿ����ߣ�Ҳ��ʱ���ߣ����ڿ������ڣ������ϣ���Ϊһֱ��ʾ��������1�ĵ�ַ�����ѡ��������0
    ��PCA9685�������ϵ�SDA��jetson nano �ϵ�27��I2C_1_SDA��������SCL��28��I2C_1_SCL���໥����Ȼ��VCC����3.3V�ĵ�Դ�ӿڣ�GEN�ӵ�
    �����ϵ�˵�����������ˡ�
```
![ʾ��ͼƬ](img/����1.jpg)  <br />
![ʾ��ͼƬ](img/����2.jpg)  <br />

## �����Լ�ʹ�÷���
```doc
    ����ɻ������ߺ󣬻���Ҫ�ҵ�һ��5-10V����ӵ�Դ���������������߹���������������ע����Բ��ܷ��ӣ���������û�б������Ƶģ����Ӻ������𻵡�
    �ҵ���ӵ�Դ������������VCC GEN���𵽹������ã�������С���������������Ԫ��������Ҫ��ӵ�Դ���ܹ��������ˣ�������׼����������ˣ�Ȼ�����
    ���ã���ŷ��������⣬������Կ��̼ҵ���Ƶ��������ϸ���ˣ�������Щ���Ӻú�����ѡ���������ϵ�16��PWM�ӿ��е����������Ӻã�����סλ�ã�������
    �Ǵ����jetson�豸���⡣

```

## jetson�豸����
---
    ���ȣ�������Ҫ��jetson��ϵͳ��һЩ�����������Լ���¼ϵͳ��I2C��Ĭ���ں������еģ�Ҳ����Ĭ�Ϲرյĵģ���Ҫ�ֶ�������
    ͨ���նˣ��� ʹ��vim ���뵽/etc/modprobe.d/blacklist.conf �У�ע�͵� blacklist i2c_i801 
---
![ʾ��ͼƬ](img/����I2C_1.png)  <br />

    Ȼ�󱣴��˳�����Ȼ��ͨ�� vim ���뵽/etc/modules �У��ڵ������׷��i2c-dev ����� <br />

![ʾ��ͼƬ](img/����I2C_2.png)  <br />

    �����ն������룬 sudo reboot ���������¾������I2C�����á�
    ������һЩ��Ҫ�Ŀ�İ�װ
    sudo apt-get install i2c-tools//���������鿴I2C����ͨ���ĵ�ַ��������I2C�Ƿ�ɹ������ϡ�
    sudo apt-get install python3-smbus //��������Ҫ�Ŀ⣬ֱ���漰�����Ʋ���
    sudo apt-get install libi2c-dev
    �����װ�������⣬�����޷��ҵ���������࣬���������Դ
    �� cp /etc/apt/sources.list /etc/apt/sources.list.bak ����ԭ�����ļ�
    ��cd /etc/apt/sources.list���뾵��Դ�ļ��У������и��ǵ�ԭ���ݣ������Ƽ����ǰ���Դ
    deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
    deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
    deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
    deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
    deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
---
    i2c-tools ������
    i2cdetect �C �����о� I2C bus ���������װ�� 
    i2cdump �C ��ʾװ�������� register ��ֵ 
    i2cget �C ��ȡװ����ĳ�� register ��ֵ 
    i2cset �C д��װ����ĳ�� register ��ֵ
---

## ����
---

ͨ��sudo i2cdetect -y -r 0�����Բ鿴jetson����0�Ƿ�ɹ����ӣ���ΪPCA9685Ĭ�ϵ�ַ��0x40��0x70�������ȷ�����£�����Կ�����������ʾ�� <br />
![ʾ��ͼƬ](img/��ַλ.png)  <br />
�������˵������û�����⣬���û����ʾ��ַ����Ҫ����Ƿ��в������

---

## ʹ��
������ʹ�����⣬ʲô����û�����Ϳ���ֱ��ʹ��python����������PWM�����������Ҫ������������Դ�������һ�����������ڲ�Ҳ�����ע�ͣ���������Ҫ�Ŀ�ģ�֮ǰ��װ��smbus�����ר����������I2C��һ���⣬�ڣ�ʹ��ǰ������ȥ�鿴�ٷ���PCA9685�ĵ�ַλ<br />
������Ҫ���ǲ���ģʽλ __MODE1 ��������ѡģʽλ1Ҳ���ǵ�ַ0x00 ��ʹ�øüĴ�����ʱ��Ҫע�⣺���δֹͣ����PWM����ͽ�����뵽˯��ģʽ����ô���������ͨ������һ�ֶ�������ߵ�ƽ������ܻ�Ӱ�������豸��ʹ�ã�һ��Ҫע�⣬�Լ�������PWMƵ��(дPRESCALE�Ĵ���)��ʱ��Ҫ������ΪSleepģʽ <br />
Ȼ����Ҫ������(ռ�ձ�)���üĴ�����ַ��һ��PWM�ڣ���4����ַ���п���LED0_ON_L,LED0_ON_H,LED0_OFF_L,LED0_OFF_H���ĸ���ͬ����һ��PWM�ڣ�����Ҳ��Ĭ�ϵ�һ���ڣ��ĸ���ַλ�ֱ���0x06��0x07��0x08,0x09������ֻ���¼��һλ��ַ�Ϳ��ԣ���Ϊ�������ǽ����ŵ���λ��ַ�� <br />
�����ĸ�ͨ���Ĵ�����ԭ��ͼ: <br />
![ʾ��ͼƬ](img/��ַλ.png)  <br />
![ʾ��ͼƬ](img/��ַλ.png)  <br />
�������������ã�����ʹ�õ������ã���Ҫ�Լ���������Ƶ�ʣ���ʹ�õ��������ڿ��Դﵽ1500us���ϾͿ�����������ŷ�����ˣ���˿���ʹ�����ƶ�������ã���
�������ó�50hz������Χ��0.5-2.5ms֮�䣬ֻҪ����1.5ms���ǵ�ŷ��Ŀ��������ھ�������������С�������޷�������
���������(Ƶ��)���üĴ�����PRE_SCALE ��ַλ�ǣ�0xFE�� <br />
ʣ�µ���ӵĵ�ַ��Ϊ�˺���������Ҫ�õ��Ĳ�����ӵģ��ֽ׶β�û��ʵ�ʵ����á�<br />
����˵������ŷ������õĹ���ԭ��������ٷ��ֲ�鿴���򵥵�˵�����㿪�������ڼ��ǲ�����������ŷ��ģ���Ҫ���ùرպ�ſ��Կ�����ͬ��
��ŷ�Ҳ����Ҫ���ùرպ���ܿ��������ҵ�ŷ�������ʱ�䲻�˹����������ŷ��ᷢ�ȵ����𺦣��������Ӧ�����̹رա�<br />
����������������������鿴



=======
待加工
>>>>>>> 39402eb8bdf41c57514cbee21bc2e431d9e7fa3b
