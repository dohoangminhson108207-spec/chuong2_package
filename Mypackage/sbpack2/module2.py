# module2.py
from Mypackage.sbpack1 import module1

# Các hàm quy đổi ra VND
def doi_usd_sang_vnd(n):
    return n * module1.USD

def doi_eur_sang_vnd(n):
    return n * module1.EUR

def doi_rub_sang_vnd(n):
    return n * module1.RUB

# Các hàm cộng số thực
def cong_hai_so(a, b):
    return a + b

def cong_ba_so(a, b, c, d=0): # Hoặc định nghĩa cộng 3 số trực tiếp
    return a + b + c