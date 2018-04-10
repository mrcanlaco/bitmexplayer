import time
#load thư viện bitmex
import bitmex


#Tạo kết nối tới server bằng API

client = bitmex.bitmex()

count = 0
i = 0
while (count<10):
	#load bảng orderbook - cả ask và bid
	result = client.Quote.Quote_get(symbol="XBTUSD", reverse=True, count=1).result()

	#lấy thông số của lệnh mua/bán ở trên cùng
	#result[0][0]['bidPrice']
	#result[0][0]['bidSize']
	#result[0][0]['askPrice']

	#chọn điểm vào
	entryPrice = result[0][0]['bidPrice']


	#thực hiện lệnh 
	#nếu long (mua trước) thì orderQty >0
	#nếu Short (bán trước) thì orderQty <0

	API_KEY = 'XQQrfPXxNNKZchClwn-6xN00'
	API_SECRET = 'SSCHQ70EK2-dQTwAH1V_vyjotoOX6D1bBkf7a5uScn8grC8w'
	client = bitmex.bitmex(api_key=API_KEY, api_secret=API_SECRET)
	client.Order.Order_new(symbol='XBTUSD', orderQty=100, price=entryPrice).result()

	#test trong vòng 10 lệnh
	
	j = 0
	#biến check xem đã đóng được cặp lệnh chưa, True là vẫn phải check tiếp, False là không cần check nữa
	check = True
	while (check):
	#for i in range(repeat):

	#xác định thời gian
		localtime = time.asctime( time.localtime(time.time()) )

	#check giá mới	
		j= j +1 
		result = client.Quote.Quote_get(symbol="XBTUSD", reverse=True, count=1).result()
		newPrice = result[0][0]['bidPrice']

	#so sánh giá mới và giá cũ. Nếu đạt target thì sẽ chốt lời
		deta = newPrice - entryPrice

		if deta>5 or deta <-5: 
			pass
			client.Order.Order_new(symbol='XBTUSD', orderQty=-100, price=newPrice).result()
			check=False
			i = i + 1

		print (localtime, " Entry Price:",entryPrice," New Price:",newPrice,"Change:",deta,"Check giá lần:",j)
	#chờ 5s sau rồi check lại
		time.sleep(10) 


	print ("==>Số lệnh đã done: ",i)
	
	count = count + 1

	#nếu chạy ở chế độ live thực thì dùng lệnh này
	#client = bitmex.bitmex(test=False, api_key=<API_KEY>, api_secret=<API_SECRET>)
