import json
from datetime import datetime
import urllib.request

print("--- CHỨNG KHOÁN K: BẮT ĐẦU CẬP NHẬT REALTIME ---")

try:
    url = "https://apistock.tcbs.com.vn/stock-insight/v1/market/index-overview?indices=VNINDEX"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as response:
        res_data = json.loads(response.read().decode('utf-8'))
        data_item = res_data.get('data', [{}])[0]
        vni_val = data_item.get('indexValue', 169.40)
        vni_change = data_item.get('change', 2.50)
        vni_percent = data_item.get('percentChange', 1.50)
        
        market_data = {
            "last_update": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "vn_index": {
                "value": f"{vni_val:,.2f}",
                "change": f"{vni_change:+,.2f}",
                "percent": f"{vni_percent:+,.2f}"
            },
            "total_value": "13,807.3 Tỷ",
            "foreign_flow": "-240 Tỷ (Bán ròng)",
            "market_breadth": {
                "up": str(data_item.get('up', 156)),
                "reference": str(data_item.get('equal', 75)),
                "down": str(data_item.get('down', 106))
            },
            "sentiment": "Tích cực / Hồi phục"
        }
except Exception as e:
    print(f"Lỗi API, dùng dữ liệu dự phòng: {e}")
    market_data = {
        "last_update": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "vn_index": {
            "value": "169.40",
            "change": "+2.50",
            "percent": "+1.50"
        },
        "total_value": "13,807.3 Tỷ",
        "foreign_flow": "-240 Tỷ (Bán ròng)",
        "market_breadth": {
            "up": "156",
            "reference": "75",
            "down": "106"
        },
        "sentiment": "Tích cực / Hồi phục"
    }

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(market_data, f, ensure_ascii=False, indent=4)

print("--- HOÀN TẤT CẬP NHẬT data.json ---")
