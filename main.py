class FitnessTracker:
    def __init__(self):
        self.kunlik_qadamlar = []
        self.kunlik_masofa = []
        self.kunlik_kaloriya = []

    def qo'sh(self, qadamlar, masofa, kaloriya):
        self.kunlik_qadamlar.append(qadamlar)
        self.kunlik_masofa.append(masofa)
        self.kunlik_kaloriya.append(kaloriya)

    def haftalik_statistika(self):
        haftalik_qadamlar = sum(self.kunlik_qadamlar[-7:])
        haftalik_masofa = sum(self.kunlik_masofa[-7:])
        haftalik_kaloriya = sum(self.kunlik_kaloriya[-7:])
        return haftalik_qadamlar, haftalik_masofa, haftalik_kaloriya

    def oylik_statistika(self):
        oylik_qadamlar = sum(self.kunlik_qadamlar[-30:])
        oylik_masofa = sum(self.kunlik_masofa[-30:])
        oylik_kaloriya = sum(self.kunlik_kaloriya[-30:])
        return oylik_qadamlar, oylik_masofa, oylik_kaloriya

    def statistika(self):
        print("Haftalik statistika:")
        haftalik_qadamlar, haftalik_masofa, haftalik_kaloriya = self.haftalik_statistika()
        print(f"Qadamlar: {haftalik_qadamlar}")
        print(f"Masofa: {haftalik_masofa} km")
        print(f"Kaloriya: {haftalik_kaloriya}")

        print("\nOylik statistika:")
        oylik_qadamlar, oylik_masofa, oylik_kaloriya = self.oylik_statistika()
        print(f"Qadamlar: {oylik_qadamlar}")
        print(f"Masofa: {oylik_masofa} km")
        print(f"Kaloriya: {oylik_kaloriya}")

tracker = FitnessTracker()
tracker.qo'sh(1000, 5, 200)
tracker.qo'sh(1200, 6, 250)
tracker.qo'sh(1500, 7, 300)
tracker.statistika()
```

Bu kodda biz FitnessTracker classini yaratdik, unda qadamlar, masofa va kaloriya kabi ma'lumotlarni saqlaydi. Qo'sh() metodida biz kunlik ma'lumotlarni qo'shib boramiz, haftalik va oylik statistikani hisoblash uchun haftalik_statistika() va oylik_statistika() metodlarini yaratdik. Statistika() metodida biz haftalik va oylik statistikani chiqarib boramiz.
