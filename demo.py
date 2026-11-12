#hêleeeeeeeeeeeeeeeeeeeeeeeeeeeee
tasks = []
while True:
    print("1) Thêm  2) Xem kết quả cũ   3) Xóa bỏ  4) Thoát ra ")
    c = input("> ").strip()
    if c == "1":
        tasks.append(input("Công việc: ").strip());
        print("Đã thêm 1 nội dung .")
        print ("vui lòng bạn kiểm tra lại công việc")
    
    elif c == "2":
        if tasks:
            for i, t in enumerate(tasks, 1):
                print(i, t)
        else:
            print("Không có công việc.")
    elif c == "3":
        i = int(input("Chỉ số: ") or 0)
        if 1 <= i <= len(tasks):
            tasks.pop(i-1); print("Đã xóa.")
        else:
            print("Chỉ số không hợp lệ.")
    elif c == "4":
        break
    else:
        print("Thử lại từ 1-4.")
