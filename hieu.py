while True:
    message=input("nhap lời bạn muốn nói với bot : ")
    if "hello" in message or "hi" in message : #nếu có chữ hello hoặc trong câu bạn nhập thì bot sẽ trả lời chào bạn
        bot_nghi= "bot nói : Chào bạn ! Hôm nay bạn cảm thấy thế nào ?"
    elif "vui" in message or "tốt" in message :
        bot_nghi = "wow, Tôi ước này nào bạn cũng được như vậy !"
    elif "buồn" in message or "chán" in message :
        bot_nghi = "Tôi xin lỗi nếu tôi làm bạn buồn , tôi có thể làm bạn vui hơn được không ?"
    elif "được" in message or "ok" in message :
        bot_nghi  = "tôi mở nhạc cho bạn nghe nhé !"
    elif "mở nhạc" in message or "mở đi" in message :
        url = "http://api.mp3.zing.vn/api/streaming/audio/ZW7W9A9C/320"
        import webbrowser
        webbrowser.open(url, new = 2)
    elif "tên gì" in message or "là ai" in message : 
        bot_nghi= "Tôi là trợ lý ảo của anh Son đẹp trai !"
    elif "ở đâu" in message :
        bot_nghi = "tôi ở trong tim bạn nè!"
    elif " bạn làm được gì" in message :
        bot_nghi = "Tôi có thể làm nhiều việc lắm nhưng giờ tôi chỉ chat với bạn thôi!" 
    elif "bye" in message or "tạm biệt" in message :
        bot_nghi = "tạm biệt bạn"
        print(bot_nghi)
        break
    else :
        bot_nghi = "tôi chưa đủ thông minh để hiểu bạn nói gì, Tôi đang học để thông minh hơn"
    print(bot_nghi)

