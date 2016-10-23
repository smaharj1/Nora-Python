

from Google import Google
import random

DemoURLs = [
    "http://compass.xbox.com/assets/23/0d/230dc52a-8f0e-40bf-bbd1-c51fdb8371e3.png?n=Homepage-360-UA_Upgrade-big_1056x594.png",
    "https://upload.wikimedia.org/wikipedia/commons/4/47/Soylent_2.0_2016.JPG",
    "https://tctechcrunch2011.files.wordpress.com/2015/08/tesla_model_s.jpg?w=738",
    "https://i.kinja-img.com/gawker-media/image/upload/s--6ERv6sIr--/18mjutor80kqxjpg.jpg",
    "http://media.bestofmicro.com/4/0/442080/original/Samsung-UHD.jpg",
    "http://lgcdn.baseballmonkey.com/80A850/magento/media/catalog/product/cache/5/small_image/600x/9df78eab33525d08d6e5fb8d27136e95/h/o/homerun-mizuno-baseball-glove-311808-pro-limited-edition-gmp300.jpg",
    "http://weknowyourdreams.com/images/scooter/scooter-08.jpg",
    "https://upload.wikimedia.org/wikipedia/en/8/8a/Coldplay_-_Ghost_Stories.png",
    "https://www.taylorguitars.com/sites/default/files/styles/multi_column_guitar_three/public/responsive-guitar-detail/Taylor-214ce-SB-DLX-fr-2014.png?itok=h5-4e-YW",
    "http://www.swstrings.com/image/GP-120?imageSize=4&index=0",
    "https://upload.wikimedia.org/wikipedia/en/2/2c/Skittles-Wrapper-Small.jpg",
    "http://images.asos-media.com/inv/media/3/1/1/0/3930113/black/image1xl.jpg",
    "https://images-na.ssl-images-amazon.com/images/I/71TtQbuOTgL._SL1000_.jpg"
]

g = Google()
print(g.SearchImage(random.choice(DemoURLs)))

