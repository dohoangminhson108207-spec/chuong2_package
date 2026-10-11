# main.py
from Mypackage.sbpack2 import module2

def main():
    print("=== CHUONG TRINH QUY DOI NGOAI TE ===")
    s_usd = float(input("Nhap so tien USD: "))
    s_eur = float(input("Nhap so tien EUR: "))
    s_rub = float(input("Nhap so tien RUB: "))

    vnd_usd = module2.doi_usd_sang_vnd(s_usd)
    vnd_eur = module2.doi_eur_sang_vnd(s_eur)
    vnd_rub = module2.doi_rub_sang_vnd(s_rub)

    # Sử dụng hàm cộng ba số thực để tính tổng
    tong_vnd = module2.cong_ba_so(vnd_usd, vnd_eur, vnd_rub)

    print("\n--- KET QUA ---")
    print(f"Tien VND tu USD: {vnd_usd:,.0f} VND")
    print(f"Tien VND tu EUR: {vnd_eur:,.0f} VND")
    print(f"Tien VND tu RUB: {vnd_rub:,.0f} VND")
    print(f"Tong so tien VND sau quy doi: {tong_vnd:,.0f} VND")

if __name__ == "__main__":
    main()