import json
from datetime import datetime

print("--- CHỨNG KHOÁN K: BẮT ĐẦU CẬP NHẬT DỮ LIỆU ---")

# Dữ liệu mô phỏng kết nối API TCBS/FireAnt (Sẽ liên kết API thực tế ở bước sau)
market_data = {
    "last_update": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    "vn_index": {
        "value": 1286.50,
        "change": 8.20,
        "percent": 0.64,
        "status": "up"
    },
    "market_breadth": {
        "up": 156,
        "reference": 75,
        "down": 106
    },
    "foreign_flow": "-240 Tỷ (Bán ròng)",
    "sentiment": "13 - Hoảng loạn"
}

# Lưu ra file data.json để trang web index.html đọc động
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(market_data, f, ensure_ascii=False, indent=4)

print("--- CẬP NHẬT DỮ LIỆU THÀNH CÔNG VÀO data.json ---")
