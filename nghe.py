import speech_recognition as sr 
while True :
    r = sr.Recognizer()  # thêm một bản ghi âm
    with sr.Microphone() as source :  #truy cập micro
        print("Bạn nói đi tôi đang nghe nè :")
        print("....")
        audio = r.record(source, duration=5) # nghe, để tránh bị đơ máy mình cho 5s 1 lần
    try :
        message = r.recognize_google(audio,language='vi-VN')  # dịch ra văn bản mình chọn ở đây là ngôn ngữ tiếng việt
        print("Bạn nói : {}".format(message))
        if "bye" in message :
            break #nếu có từ bye trong đoạn hội thoại thid kết thúc vòng lặp
    except:
        print("Tôi không nghe được bạn nói rõ hơn xíu đi nè!:") 
