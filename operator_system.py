import time

operators = [
    {"id": 1, "name": "Ahmet Y.", "machine": "Ekskavatör", "price_per_hour": 1500, "is_available": True},
    {"id": 2, "name": "Mehmet T.", "machine": "Beko Loder", "price_per_hour": 1200, "is_available": False},
    {"id": 3, "name": "Can S.", "machine": "Mini Kepçe", "price_per_hour": 900, "is_available": True},
]

def show_operators():
    print("\n--- 🚜 ŞANTİYE SAHASI: MÜSAİT İŞ MAKİNELERİ ---")
    for op in operators:
        status = "✅ MÜSAİT" if op['is_available'] else "❌ MEŞGUL"
        print(f"ID: {op['id']} | {op['machine']} ({op['name']}) | Saatlik: {op['price_per_hour']} TL | Durum: {status}")

def book_operator():
    show_operators()
    try:
        choice = int(input("\nKiralamak istediğiniz makinenin ID numarasını girin: "))
        hours = int(input("Kaç saatlik çalışma planlıyorsunuz? "))
        

        selected_op = next((op for op in operators if op["id"] == choice), None)

        if not selected_op:
            print("⚠️ Hata: Geçersiz ID girdiniz.")
            return

        if not selected_op["is_available"]:
            print(f"⚠️ Üzgünüz, {selected_op['name']} şu an başka bir şantiyede çalışıyor.")
        else:
            total_cost = selected_op["price_per_hour"] * hours
            print(f"\n⌛ Rezervasyon işleniyor...")
            time.sleep(1)
            print(f"✅ Onaylandı! {selected_op['name']} yönlendiriliyor.")
            print(f"💰 Toplam Tahmini Ücret: {total_cost} TL")

            selected_op["is_available"] = False
            
    except ValueError:
        print("⚠️ Lütfen geçerli bir sayı giriniz.")


if __name__ == "__main__":
    while True:
        print("\n--- KEPÇEKAPIMDA OPERASYON MERKEZİ ---")
        print("1. Makineleri Listele")
        print("2. Rezervasyon Yap")
        print("3. Çıkış")
        
        menu_choice = input("Seçiminiz: ")
        
        if menu_choice == "1":
            show_operators()
        elif menu_choice == "2":
            book_operator()
        elif menu_choice == "3":
            print("Sistem kapatılıyor. İyi çalışmalar!")
            break
        else:
            print("Geçersiz seçim.")