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
    

print(data)

print("--------------------------------------------------------------------------------")
print('Minggu ke-\t Jumlah SMS\t Menit telepon ke sesama operator(menit)\t Menit telepon ke operaator lain(menit)\t Total pulsa (Rp)\t Kuota sosmed (kb)\t Kuota lainnya (kb)\t Tagihan kuota terpakai (Rp)\t Tagihan/minggu')

for i in range(0,len(data)):
    print(data[i][0],'\t', data[i][1], '\t',data[i][2], '\t',data[i][3], '\t',data[i][4], '\t',data[i][5], '\t',data[i][6], '\t',data[i][7], '\t',data[i][8])
    i += 1

print("--------------------------------------------------------------------------------")
   
with open(nama_file, 'w') as outf:
    header = ['Minggu ke-','Jumlah SMS','Menit telepon ke sesama operator(menit)','Menit telepon ke operaator lain(menit)','Total pulsa (Rp)','Kuota sosmed (kb)','Kuota lainnya (kb)','Tagihan kuota terpakai (Rp)','Tagihan/minggu']
    writer = csv.DictWriter(outf, fieldnames=header)
    writer.writeheader()
    
   
