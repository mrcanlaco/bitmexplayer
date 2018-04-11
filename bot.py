#load thư viện thời gian
import time
#load thư viện bitmex
import bitmex


#Tạo kết nối tới server bằng API
client = bitmex.bitmex()

#nếu chạy ở chế độ live thực thì dùng lệnh này
#client = bitmex.bitmex(test=False, api_key=<API_KEY>, api_secret=<API_SECRET>)


#test trong vòng 10 cặp lệnh
#count là biến đến số cặp lệnh đã mở-đóng thành công
count = 0
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

	# j là biến để xác định xem đã kiểm tra giá mới newPrice bao nhiêu lần	
	j = 0
	#biến check xem đã đóng được cặp lệnh chưa, True là vẫn phải check tiếp, False là không cần check nữa
	check = True
	while (check):
	#for i in range(repeat):

	#xác định thời gian
		localtime = time.asctime( time.localtime(time.time()) )

	#check giá mới	
		result = client.Quote.Quote_get(symbol="XBTUSD", reverse=True, count=1).result()
		newPrice = result[0][0]['bidPrice']
		j= j +1 
	#so sánh giá mới và giá cũ. 
		deta = newPrice - entryPrice
	#Nếu đạt target +5  thì sẽ chốt lời hoặc lỗ quá -5 thì cắt lỗ
		if deta>5 or deta <-5: 
			pass
			#thực hiện lệnh bán
			client.Order.Order_new(symbol='XBTUSD', orderQty=-100, price=newPrice).result()
			check=False
			count = count + 1
		#in ra thông tin
		print (localtime, " Entry Price:",entryPrice," New Price:",newPrice,"Change:",deta,"Check giá lần:",j)
	
		#chờ 10s sau rồi check lại
		time.sleep(10) 


	print ("==>Số cặp lệnh đã hoàn thành: ",count)
	
	
