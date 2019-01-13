import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()

def downloader(img_name, img_url):
	req = urllib.request.urlopen(img_url)
	img_content = req.read()

	with open(img_name, 'wb') as f:
		f.write(img_content)

def main():
	gevent.joinall([
		gevent.spawn(downloader, '5.jpg', "https://rpic.douyucdn.cn/live-cover/appCovers/2018/09/30/4043801_20180930193334_small.jpg"),
		gevent.spawn(downloader, '6.jpg', "https://rpic.douyucdn.cn/live-cover/roomCover/2019/01/09/22a4bacba6a182d54a097306cae3f52b_big.jpg"),
		gevent.spawn(downloader, '7.jpg', "https://rpic.douyucdn.cn/live-cover/appCovers/2019/01/08/6217770_20190108004245_small.jpg"),
		gevent.spawn(downloader, '8.jpg', "https://rpic.douyucdn.cn/asrpic/190113/5250742_6125323_116d6_2_1303.jpg"),
		gevent.spawn(downloader, '9.jpg', "https://rpic.douyucdn.cn/live-cover/appCovers/2018/12/29/1448245_20181229042517_small.jpg"),
		gevent.spawn(downloader, '10.jpg', "https://rpic.douyucdn.cn/asrpic/190113/6113690_5777969_0cced_2_1306.jpg"),
		gevent.spawn(downloader, '11.jpg', "https://rpic.douyucdn.cn/asrpic/190113/5230163_3942418_2bff3_2_1309.jpg")
	])


if __name__ == '__main__':
	main()