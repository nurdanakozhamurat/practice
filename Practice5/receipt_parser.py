import re
import json

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()


prices = re.findall(r"\d[\d ]*,\d{2}", text)

clean_prices = [p.replace(" ", "") for p in prices]


product_names = re.findall(r"\d+\.\n(.+)", text)


total_match = re.search(r"ИТОГО:\n([\d ]+,\d{2})", text)
total_amount = total_match.group(1).replace(" ", "") if total_match else None


datetime_match = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4}\s*\d{2}:\d{2}:\d{2})", text)
datetime_value = datetime_match.group(1) if datetime_match else None


payment_match = re.search(r"(Банковская карта|Наличные)", text)
payment_method = payment_match.group(1) if payment_match else None


data = {
    "products": product_names,
    "prices": clean_prices,
    "total": total_amount,
    "date_time": datetime_value,
    "payment_method": payment_method
}

print(json.dumps(data, indent=4, ensure_ascii=False))