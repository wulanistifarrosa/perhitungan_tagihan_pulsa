import csv
        break
    
    minggu = input("Untuk minggu ke: ")
    total_sms = int(input("Jumlah SMS : "))
    menit_tlp_sama = float(input("Jumlah menit telepon anda ke sesama operator: "))
    menit_tlp_lain = float(input("Jumlah menit telepon anda ke lain operator: "))
    total_kuota_sosmed = float(input("Jumlah kuota terpakai untuk sosial media (kb): "))
    total_kuota_lainnya = float(input("Jumlah kuota terpakai untuk lainnya (kb): "))
    totalkuota1 = total_kuota_sosmed + total_kuota_lainnya
    totalkuota2 = 5*totalkuota1
    totalpulsatlp = 250*menit_tlp_sama + 500*menit_tlp_lain
    pulsasms = 150*total_sms
    totalpulsa = pulsasms + totalpulsatlp
    total_tagihan = totalkuota2 + totalpulsa
    
    data.append([minggu,total_sms,menit_tlp_sama,menit_tlp_lain,totalpulsa,total_kuota_sosmed,total_kuota_lainnya,totalkuota2,total_tagihan])
 
