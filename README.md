# pixelsorter

### Requiremets:
```
pip install Pillow
```
### Usage:
```
git clone https://github.com/oprince-dev/pixelsorter
cd pixelsorter
python3 pixelsorter.py [-h] Image [-m MODE] [-d DIRECTION] [-t THRESHOLD] [-r REVERSE] [-u UPPER]
```
### Examples:
```
python3 pixelsorter.py koi.jpg -d v -t 255 -r
```
![koi_Pv255r.jpg](https://github.com/oprince-dev/pixelsorter/blob/master/images/koi_Pv255r.jpg)
<br>

```
python3 pixelsorter.py street,jpg -d h -t 40 -r -u
```
![street_Ph40ru.jpg](https://github.com/oprince-dev/pixelsorter/blob/master/images/street_Ph40ru.jpg)
<br>
```
python3 pixelsorter.py tokyo.jpg -d v -t 50 -r -u
```
![tokyo_Pv50ru.jpg](https://github.com/oprince-dev/pixelsorter/blob/master/images/tokyo_Pv50ru.jpg)
