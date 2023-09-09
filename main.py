meem = {"LOL": "komik bir şeye verilen cevap", 
        "CRINGE": "garip ya da utandırıcı bir şey"
        }

while True:
    
    kelime = input("Öğrenmek istediğin terim:")
        
    if kelime in meem.keys():
        print(meem[kelime])
            
    else:
        print("Terim yok!")
