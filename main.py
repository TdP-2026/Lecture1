from gestionale.vendite.ordini import Ordine, RigaOrdine, OrdineConSconto
from gestionale.core.prodotti import Prodotto, crea_prodotto_standard, ProdottoRecord
from gestionale.core.clienti import Cliente, ClienteRecord

print("=======================================================")

    def __init__(self, name: str, price: float, quantity: int, supplier = None):
        self.name = name
        self._price = None
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

    def valore_netto(self):
        return self._price*self.quantity
p1 = Prodotto("Ebook Reader", 120.0, 1, "AAA")
p2 = crea_prodotto_standard("Tablet", 750)

print (p1)
print (p2)
print("=======================================================")

c1 = Cliente("Mario Rossi", "mail@mail.com", "Gold")

cliente1 = ClienteRecord("Mario Rossi", "mariorossi@example.com", "Gold")
p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20)

ordine = Ordine([RigaOrdine(p1,2), RigaOrdine(p2, 10)], cliente1)
ordine_scontato = OrdineConSconto([RigaOrdine(p1,2), RigaOrdine(p2, 10)], cliente1, 0.1)

    @property
    def price(self):    #equivalente al getter
        return self._price

    @price.setter   #possibile solo dopo aver definito un getter
    def price(self, value):
        if value < 0:
            raise ValueError("Attenzione, prezzo non valido")
            pass
        self._price = value

myproduct1 = Prodotto(name = "Laptop", price = 1200.0, quantity=12, supplier="ABC")
print(ordine)
print("Numero di righe nell'ordine: ", ordine.numero_righe())
print("Totale netto: ", ordine.totale_netto())
print("Totale lordo (IVA 22%): ", ordine.totale_lordo(0.22))

print(ordine_scontato)
print("Totale netto sconto: ", ordine_scontato.totale_netto())
print("Totale lordo scontato: ", ordine_scontato.totale_lordo(0.22))

print("-------------------------------------------------------------------")

myproduct2 = Prodotto("Mouse", 10, 25, "CDE")
print(f"Nome prodotto: {myproduct2.name} - prezzo: {myproduct2.price}")

print(f"valore lordo di prodotto 1 {myproduct1.valore_lordo()}")
Prodotto.aliquota_iva = 0.24
print(f"Valore lordo di prodotto 1 {myproduct1.valore_lordo()}")

#Scrivere una classe Cliente che abbia i campi "nome", "email", "categoria" ("Gold", "Silver", "Bronze").
#vorremmo che questa classe avesse un metodo che chiamiamo "descrizione"
# che deve restituire una stringa formattata ad esempio
#"Cliente Fulvio Bianchi (Gold) - fulvio@google.com"

#Si modifichi la classe Cliente in modo tale che la proprietà categoria sia protetta e che accetti solo
# le categorie Gold, Silver, Bronze
class Cliente:
    def __init__(self, nome, mail, categoria):
        self.nome = nome
        self.mail = mail
        self._categoria = None
        self._categoria = categoria

    def descrizione(self): #to_string
        # "Cliente Fulvio Bianchi (Gold) - fulvio@google.com"
        return f"Cliente {self.nome} ({self.categoria}) - {self.mail}"

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, value):
        if value != "Gold" or value != "Silver" or value != "Bronze":
            raise ValueError("Categoria non valida, inserire solo Gold, Silver o Bronze")
            pass
        self._categoria = value

c1 = Cliente("Mario Bianchi", "mario.bianchi@polito.it", "Gold")
print(c1.descrizione())
#Nel package gestionale, scriviamo un modulo fatture.py che contenga:
# - una classe Fattura che contiene un Ordine, un numero_fattura e una data
# - un metodo genera_fattura() che restituisce una stringa formattata con tutte le info della fattura
