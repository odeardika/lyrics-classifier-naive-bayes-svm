import pyperclip
# pyperclip.copy('The text to be copied to the clipboard.')

def func(value):
    return (' '.join(value.splitlines())).replace(',',' ')

text = """
Aku tak mengerti apa yang kurasa
Rindu yang tak pernah begitu hebatnya
Aku mencintaimu lebih dari yang kau tahu
Meski kau takkan pernah tahu
Aku persembahkan hidupku untukmu
Telah kurelakan hatiku padamu
Namun kau masih bisu, diam seribu bahasa
Dan hati kecilku bicara
Baru kusadari
Cintaku bertepuk sebelah tangan
Kau buat remuk seluruh hatiku
Semoga waktu akan mengilhami
Sisi hatimu yang beku
Semoga akan datang keajaiban
Hingga akhirnya kau pun mau
Aku mencintaimu lebih dari yang kau tahu
Meski kau takkan pernah tahu
Baru kusadari
Cintaku bertepuk sebelah tangan
Kau buat remuk seluruh hatiku
Baru kusadari
Cintaku bertepuk sebelah tangan
Kau buat remuk seluruh hatiku
Baru kusadari baru kusadari)
Cintaku bertepuk sebelah tangan (bertepuk sebelah tangan)
Kau buat remuk seluruh hatiku
Seluruh hatiku
"""
pyperclip.copy(func(text))

