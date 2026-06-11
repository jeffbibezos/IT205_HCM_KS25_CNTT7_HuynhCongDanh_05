works_list = [
    {"id": "TS001", "task": "Design App", "name": "Danh", "complete_days": 10, "actual_days": 14, "date_difference": 4, "status": "Quá hạn"},
    {"id": "TS002", "task": "Design App", "name": "B", "complete_days": 1, "actual_days": 1, "date_difference": 0, "status": "Hoàn thành sớm"},
    {"id": "TS003", "task": "Design App", "name": "C", "complete_days": 23, "actual_days": 14, "date_difference": -9, "status": "Hoàn thành sớm"},
]


def caculated_date_difference(actual_days, complete_days):
    date_difference = actual_days - complete_days
    return date_difference


def classify(date_difference):
    days = date_difference

    if days <= 0:
        status = "Hoàn thành sớm"
    elif days == 0:
        status = "Bình thường"
    elif days <= 3:
        status = "Cần tăng tốc"
    else:
        status = "Quá hạn"

    return status


def print_table(works):
    if (len(works) == 0):
        print("Hiện tại danh sách đang trống")
    
    print("-" * 125)
    print(f"{'ID':<5} | {'Task':<20} | {'Name':<20} | {'Complete Days':<15} | {'Actual Days':<15} | {'Date Difference':<15} | {'Status':<20} ")
    print("-" * 125)
    for i in range(len(works)):
        print(f"{works[i].get("id"):<5} | {works[i].get("task"):<20} | {works[i].get("name"):<20} | {works[i].get("complete_days"):<15} | {works[i].get("actual_days"):<15} | {works[i].get("date_difference"):<15} | {works[i].get("status"):<20} ")
    print("-" * 125)


def add_task():
    print("--- Thêm mới công việc ---")
    while True:
        id_input = input("Nhập mã mới: ").strip().upper()
        if id_input == "":
            print("Ô nhập liệu không được để trống")
        isValid = False
        for i in range(len(works_list)):
            if id_input == works_list[i].get("id"):
                print("Mã đã tồn tại vui lòng nhập mã khác")
                isValid = True
        if isValid == False: 
            break

    while True:
        task_input = input("Nhập tên công việc: ").strip()
        if task_input == "":
            print("Ô nhập liệu không được để trống")
        else:
            break
    
    while True:
        name_input = input("Nhập tên người thực hiện: ").strip()
        if name_input == "":
            print("Ô nhập liệu không được để trống")
        else:
            break

    while True:
        complete_days_input = input("Nhập số ngày hoàn thành dự kiến: ").strip()
        if complete_days_input == "":
            print("Ô nhập liệu không được để trống")
        elif not complete_days_input.isdigit():
            print("Phải là 1 số nguyên dương")
        else:
            complete_days_input = int(complete_days_input)
            break
    
    while True:
        actual_days_input = input("Nhập số ngày hoàn thành thực tế: ").strip()
        if actual_days_input == "":
            print("Ô nhập liệu không được để trống")
        elif not actual_days_input.isdigit():
            print("Phải là 1 số nguyên dương")
        else:
            actual_days_input = int(actual_days_input)
            break

    date_difference_input = caculated_date_difference(actual_days_input, complete_days_input)

    status_input = classify(date_difference_input)

    new_task = {
        "id": id_input, 
        "task": task_input, 
        "name": name_input, 
        "complete_days": complete_days_input, 
        "actual_days": actual_days_input, 
        "date_difference": date_difference_input, 
        "status": status_input
    }

    works_list.append(new_task)

    print(f"Đã thêm mới công việc với ID là {id_input}")


def update_task():
    print("--- Chỉnh sửa công việc ---")
    print("Để dừng việc chỉnh sửa hãy nhập 1 ký tự bất kì")
    while True:
        id_input = input("Nhập mã cần chỉnh sửa: ").strip().upper()
        if id_input == "":
            print("Ô nhập liệu không được để trống")
        isValid = False
        for i in range(len(works_list)):
            if id_input == works_list[i].get("id"):
                print(f"Đã tìm thấy mã công việc {id_input}")

                while True:
                    name_input = input("Nhập lại tên người thực hiện: ").strip()
                    if name_input == "":
                        print("Ô nhập liệu không được để trống")
                    else:
                        break

                while True:
                    complete_days_input = input("Nhập lại số ngày hoàn thành dự kiến: ").strip()
                    if complete_days_input == "":
                        print("Ô nhập liệu không được để trống")
                    elif not complete_days_input.isdigit():
                        print("Phải là 1 số nguyên dương")
                    else:
                        complete_days_input = int(complete_days_input)
                        break
                
                while True:
                    actual_days_input = input("Nhập lại số ngày hoàn thành thực tế: ").strip()
                    if actual_days_input == "":
                        print("Ô nhập liệu không được để trống")
                    elif not actual_days_input.isdigit():
                        print("Phải là 1 số nguyên dương")
                    else:
                        actual_days_input = int(actual_days_input)
                        break

                date_difference_input = caculated_date_difference(actual_days_input, complete_days_input)

                status_input = classify(date_difference_input)

                works_list[i] = {
                    "id": works_list[i].get("id"), 
                    "task": works_list[i].get("task"), 
                    "name": name_input, 
                    "complete_days": complete_days_input, 
                    "actual_days": actual_days_input, 
                    "date_difference": date_difference_input, 
                    "status": status_input
                }

                print(f"Đã chỉnh sửa công việc với ID là {id_input}")
                            
                isValid = True
        
        if isValid == False:
            print(f"Không tìm thấy mã {id_input}")
            break

def delete_task():
    print("--- Xóa công việc ---")
    while True:
        id_input = input("Nhập mã công việc cần xóa: ").strip().upper()
        if id_input == "":
            print("Ô nhập liệu không được để trống")
        isValid = False
        found_index = 0
        for i in range(len(works_list)):
            if id_input == works_list[i].get("id"):
                found_index = i
                isValid = True

        if isValid == True:
            del works_list[found_index]
            print(f"Đã xóa công việc với ID là {id_input}")
            break
        if isValid == False:
            print("Không tìm thấy mã để xóa")
            break


def search_task():
    print("--- Tìm kiếm công việc ---")
    while True:
        choice = input("""
1. Tìm kiếm theo id
2. Tìm kiếm theo tên nhân viên
3. Thoát chức năng tìm 
>> Nhập chức năng (1-3): """)
        match choice:
            case "1":
                while True:
                    id_input = input("Nhập mã cần tìm: ").strip().upper()
                    if id_input == "":
                        print("Ô nhập liệu không được để trống")
                    isValid = False
                    found_index = 0
                    for i in range(len(works_list)):
                        if id_input == works_list[i].get("id"):
                            found_index = i

                            print(f"Đã tìm thấy công việc có mã {id_input}")
                            isValid = True
                    if isValid == True:
                        print(works_list[found_index])
                    if isValid == False: 
                        print(f"Không tìm thấy công việc có mã {id_input}")
                        break
            case "2":
                while True:
                    name_input = input("Nhập tên cần tìm: ").strip()
                    if name_input == "":
                        print("Ô nhập liệu không được để trống")
                    isValid = False
                    found_index = 0
                    for i, value in enumerate(works_list):
                        if name_input in value:
                            found_index = i

                            print(f"Đã tìm thấy công việc có tên {name_input}")
                            isValid = True
                    if isValid == True:
                        print(works_list[found_index])
                    if isValid == False: 
                        print(f"Không tìm thấy công việc có tên {name_input}")
                        break
            case "3":
                print("Thoát chương trình")
                break
            case _:
                print("Vui lòng nhập đúng chức năng")
def main():       
    while True:
        choice = input("""
============= PROJECT MANAGER =============
1. Hiển thị danh sách công việc
2. Thêm mới công việc
3. Cập nhật tiến độ thực tế
4. Xóa công việc khỏi dự án
5. Tìm kiếm công việc
6. Thống kê trạng thái tiến độ 
7. Phân loại tiến độ tự động
8. Thoát chương trình
==========================================
>> Nhập lựa chọn của bạn (1-8): """)
        match choice:
            case "1":
                print("--- Danh Sách Công Việc ---")
                print_table(works_list)
            case "2":
                add_task()
            case "3":
                update_task()
            case "4":
                delete_task()
            case "5":
                search_task()
                pass
            case "6":
                
                pass
            case "7":
                
                pass
            case "8":
                print("Thoát chương trình")
                break
            case _:
                print("Vui lòng nhập đúng chức năng!")


