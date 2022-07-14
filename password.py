password = 'a123456'
a = 0
while a < 3 :
	a = a + 1
	pwd = input('請輸入密碼')
	if pwd == password:
		print('登錄成功')
		break
	else :
		print('密碼錯誤')
		if a < 3:
			print('還有', 3-a, '次機會')
		else: 
			print('沒機會嘗試了')