
# Praktikum 26
# Tipe data Dictionary

student = {
    "nama" : "Faqih",
    "umur" : 26,
    "tinggi" : 177.6,
    "hobi" : ["Olahraga" , "Jalan-Jalan"],
    "kontak" : {
        "website" : "faqihkeren.com",
        "email" : "faqihkeren.com"
    }  
}
print("Nama : ", student.get('nama') )
print("Umur :" , student.get('umur'))
print("Tinggi : " , student.get('tinggi'))
print("Hobi : ", student.get('hobi'))
print("Kontak : " , student.get('kontak') )
