from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79991112123"),
    Smartphone("Huawei", "nova 11 Pro", "+79992221213"),
    Smartphone("Xiaomi", "13 Pro", "+79993132321"),
    Smartphone("ASUS", "Zenfone 10", "+79994142432"),
    Smartphone("POCO", "F5 Pro", "+79995453543")
]

for phone in catalog:
    phone.infoPhone()    
