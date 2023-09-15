from tkinter import *

# window oluşturalım
window = Tk()
window.title("BMI Uygulaması")
# window.minsize(width=600, height=450)
window.config(padx=10, pady=10)

# Label1
weight_label = Label(text="Enter your weigth (Kg)")
weight_label.pack()
# entry for weight
weight_entry = Entry(width=40)
weight_entry.pack()



# Label2
height_label = Label(text="Enter your height (cm)")
height_label.pack()
# entry for height
height_entry = Entry(width=40)
height_entry.pack()

def calculate():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    print(height, weight)
    # Eğer entry'lerden birisi girilmedi ise lütfen değerleri giriniz yazdıralım.
    if height_entry.get() == "" or weight_entry.get()=="":
        result_label.config(text="Lütfen 2 değeri de giriniz.")
    else:
        # BMI hesaplamak için kg/m2 olması gerekiyor
        bmi = weight / ( (height/100)**2 )
        result_label.config(text=f"bmi değeriniz:{bmi}")
        # bmi sonucuna göre zayıfsın, normalsin vb. ifadeleri label'da göstermek için
        result = ""
        if bmi<16:
            result = "Çok zayıfsın"
        elif bmi>=16 and bmi<17:
            result = "Kabul edilebilir Zayıfsın"
        elif bmi>=17 and bmi<18.5:
            result ="Hafif Zayıfsın"
        elif bmi>=18.5 and bmi<25:
            result = "Normalsin"
        elif bmi>=25 and bmi<30:
            result = "Aşırı Kilolusun"
        else:
            result = "Obezite"
        result_label.config(text=f"Merhabalar, BMİ sonucuna göre {result}")

# Hesaplama Butonu
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.pack()

# İşlem sonuçlarını göstermek için bir tane daha label alalım :)
result_label = Label(text="")
result_label.pack()


window.mainloop()