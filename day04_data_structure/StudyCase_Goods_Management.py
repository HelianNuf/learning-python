# Study Case: Basic System for noted items stock

# List → Incoming Item History
# Set → Item Category (Unique)
# Dictionary → Item Name & Stock
# Tuple → Item Data (Unchanged)

stock_items = {
    "Book": 10,
    "Pen": 25,
    "Eraser": 5
}

category = {"Stationery"}

incoming = ["Book", "Pen", "Eraser"]

info_store = ("Store Goods", "2025")


print("=== ITEMS STOCK ===")
for item, stock in stock_items.items():
    print(f"{item} : {stock}")

print("\nKategori Barang :", category)
print("Barang Masuk    :", incoming)
print("Info Toko       :", info_store)