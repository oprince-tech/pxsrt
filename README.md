# pixelsorter

### Requiremets:
```
pip install Pillow
```
### Usage:
```
git clone https://github.com/oprince-dev/pixelsorter.git
cd pixelsorter
python3 pixelsorter.py [-h] Image [-m MODE] [-d DIRECTION] [-t THRESHOLD] [-r] [-u]
```
### Notes:
|Option  |Description|
|--------|------------------------------|
|Image   |Place file you wish to sort in the Images folder|
|-m      |Mode (1/L/P) [defaults to P]|
|-d      |Direction (v or h) [defaults to h]|
|-t      |Threshold (value between 0 and 255) [defaults to 255]|
|-r      |Reverse (reverse the order pixels are sorted)|
|-u      |Upper (target the lighter pixels to sort)|

### Examples:
*Before images can be found in the Images folder*
```
python3 pixelsorter.py tokyo.jpg -d v -t 50 -r -u
```
![tokyo_Pv50ru.jpg](../blob/master/images/tokyo_Pv50ru.jpg)
___

```
python3 pixelsorter.py koi.jpg -d v -t 255 -r
```
![koi_Pv255r.jpg](https://github.com/oprince-dev/pixelsorter/blob/master/images/koi_Pv255r.jpg)
___

```
python3 pixelsorter.py street,jpg -d h -t 40 -r -u
```
![street_Ph40ru.jpg](https://github.com/oprince-dev/pixelsorter/blob/master/images/street_Ph40ru.jpg)
___

```
python3 pixelsorter.py sakura.jpg -t 255 -r
```
![tokyo_Pv50ru.jpg](https://github.com/oprince-dev/pixelsorter/blob/master/images/sakura_Ph255r.jpg)
