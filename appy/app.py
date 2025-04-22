from flask import Flask, render_template, request

app = Flask(__name__)

yemekler = {
    # TÜRKİYE
    ("turkiye", "vegan", "firin"): ("Zeytinyağlı Enginar", "enginar.jpg"),
    ("turkiye", "vegan", "kizartma"): ("Baharatlı Balkabağı", "balkabagi.jpg"),
    ("turkiye", "vegan", "haslama"): ("Kuru Dolma", "sarma.jpg"),
    ("turkiye", "vejetaryen", "firin"): ("Fırında Karnabahar", "karnabahar.jpg"),
    ("turkiye", "vejetaryen", "kizartma"): ("Mantar Sote", "mantar.jpg"),
    ("turkiye", "vejetaryen", "haslama"): ("Balkabağı Çorbası", "corba.jpg"),
    ("turkiye", "pesketaryen", "firin"): ("Fırında Uskumru", "uskumru.jpg"),
    ("turkiye", "pesketaryen", "kizartma"): ("Karides Güveç", "karides.jpg"),
    ("turkiye", "pesketaryen", "haslama"): ("Balık Buğulama", "bugulama.jpg"),
    ("turkiye", "hepcil", "firin"): ("Fırında Kuzu İncik", "kuzu.jpg"),
    ("turkiye", "hepcil", "kizartma"): ("İçli Köfte", "iclikofte.jpg"),
    ("turkiye", "hepcil", "haslama"): ("Hünkar Beğendi", "begendi.jpg"),

    # İTALYA
    ("italya", "vegan", "firin"): ("Ribollita", "ribollita.jpg"),
    ("italya", "vegan", "kizartma"): ("Pasta Aglio e Olio", "olio.jpg"),
    ("italya", "vegan", "haslama"): ("Pasta Pomodoro", "pomodoro.jpg"),
    ("italya", "vejetaryen", "firin"): ("Pizza Margherita", "pizza.jpg"),
    ("italya", "vejetaryen", "kizartma"): ("Gnocchi al Pesto", "gnocchi.jpg"),
    ("italya", "vejetaryen", "haslama"): ("Polenta Gorgonzola", "polenta.jpg"),
    ("italya", "pesketaryen", "firin"): ("Branzino al Forno", "branzino.jpg"),
    ("italya", "pesketaryen", "kizartma"): ("Gamberi alla Busara", "gamberi.jpg"),
    ("italya", "pesketaryen", "haslama"): ("Insalata di Polpo", "polpo.jpg"),
    ("italya", "hepcil", "firin"): ("Lasagna Bolognese", "lasagna.jpg"),
    ("italya", "hepcil", "kizartma"): ("Fettuccine Alfredo", "fettuccine.jpg"),
    ("italya", "hepcil", "haslama"): ("Pollo alla Cacciatora", "pollo.jpg"),

    # POLONYA
    ("polonya", "vegan", "firin"): ("Pierogi", "pierogi.jpg"),
    ("polonya", "vegan", "kizartma"): ("Placki Ziemniaczane", "placki.jpg"),
    ("polonya", "vegan", "haslama"): ("Kopytka", "kopytka.jpg"),
    ("polonya", "vejetaryen", "firin"): ("Bigos", "bigos.jpg"),
    ("polonya", "vejetaryen", "kizartma"): ("Twaróg", "twarog.jpg"),
    ("polonya", "vejetaryen", "haslama"): ("Śledź", "sledz.jpg"),
    ("polonya", "pesketaryen", "firin"): ("Karp", "karp.jpg"),
    ("polonya", "pesketaryen", "kizartma"): ("Pstrąg Wędzony", "pstrag.jpg"),
    ("polonya", "pesketaryen", "haslama"): ("Śledź Haşlama", "sledz.jpg"),
    ("polonya", "hepcil", "firin"): ("Karp Wigilijny", "wigilia.jpg"),
    ("polonya", "hepcil", "kizartma"): ("Kotlety Mielone", "kotlet.jpg"),
    ("polonya", "hepcil", "haslama"): ("Bigos Etli", "bigos.jpg")
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sonuc', methods=['POST'])
def sonuc():
    ulke = request.form['ulke']
    tarz = request.form['tarz']
    pisirme = request.form['pisirme']
    secim = yemekler.get((ulke, tarz, pisirme))
    if secim:
        yemek, gorsel = secim
    else:
        yemek = None
        gorsel = None
    return render_template('sonuc.html', yemek=yemek, gorsel=gorsel)

if __name__ == '__main__':
    app.run(debug=True)