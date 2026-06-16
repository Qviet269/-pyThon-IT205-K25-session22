from miniproject.shipping_system import  calculate_final_shipping

def test_calculate_final_shipping_distance_fare():
    """Kiểm tra xem hệ thống có cộng thêm 10,000đ phụ thu đường xa (>=20km) không."""
  

    result = calculate_final_shipping(3.5, 25, "express")
    
    if result == 47000:
        print("-> test_calculate_final_shipping_distance_fare: ĐẠT (PASSED)")
    else:
        print(f"-> test_calculate_final_shipping_distance_fare: THẤT BẠI (FAILED) - Tính ra {result}")


def test_invalid_distance_exception():
    """Kiểm tra xem hệ thống có chặn và ném ra lỗi khi khoảng cách âm không."""
    try:
        calculate_final_shipping(2.0, -5, "standard")
        print("-> test_invalid_distance_exception: THẤT BẠI (FAILED) - Không chặn khoảng cách âm")
    except ValueError:
        print("-> test_invalid_distance_exception: ĐẠT (PASSED) - Đã chặn lỗi chính xác")


if __name__ == "__main__":
    print("\n========== ĐANG CHẠY KIỂM THỬ TỰ ĐỘNG ==========")
    test_calculate_final_shipping_distance_fare()
    test_invalid_distance_exception()
    print("================================================\n")