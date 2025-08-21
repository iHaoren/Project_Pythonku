print("Selamat datang di quiz komputer saya! ^_____^")

playing = input("Apakah kamu ingin bermain? ")

if playing.lower() != "ya":
    quit() 
    
print("Okey! mari kita mulai.. :) ")

# skor
score = 0

# pertanyaan 1
answer = input("Apa kepanjangan dari CPU? ")
if answer.lower() == "central processing unit":
    print("Selamat...jawaban kamu benar :)!")
    score += 1
else:
    print("Yahh...maaf jawabanmu salah :( yang benar adalah central processing unit" )

# pertanyaan 2
answer = input("Apa kepanjangan dari GPU? ")
if answer.lower() == "graphics processing unit":
    print("Selamat...jawaban kamu benar :)!")
    score += 1
else:
    print("Yahh...maaf jawabanmu salah :( yang benar adalah graphics processing unit")
    
# pertanyaan 3
answer = input("Apa kepanjangan dari RAM? ")
if answer.lower() == "random access memory":
    print("Selamat...jawaban kamu benar :)!")
    score += 1
else:
    print("Yahh...maaf jawabanmu salah :( yang benar adalah random access memory")

# pertanyaan 4
answer = input("Apa kepanjangan dari PSU? ")
if answer.lower() == "power supply":
    print("Selamat...jawaban kamu benar :) !")
    score += 1
else:
    print("Yahh...maaf jawabanmu salah :( yang benar adalah power supply")
    
# pertanyaan 5
answer = input("Apa fungsi utama dari SSD? ")
if answer.lower() == "menyimpan data" or answer.lower() == "penyimpanan data":
    print("Selamat...jawaban kamu benar :)!")
    score += 1
else:
    print("Yahh...maaf jawabanmu salah :( yang benar adalah menyimpanan data")

# pertanyaan 6
answer = input("Sistem operasi manakah yang dibuat oleh Microsoft? ")
if answer.lower() == "windows":
    print("Selamat...jawaban kamu benar :)!")
    score += 1
else:
    print("Yahh...maaf jawabanmu salah :( yang benar adalah windows")

# pertanyaan 7
answer = input("Apa kepanjangan dari BIOS? ")
if answer.lower() == "basic input output system":
    print("Selamat...jawaban kamu benar :) !")
    score += 1
else:
    print("Yahh...maaf jawabanmu salah :( yang benar adalah basic input output system")

# pertanyaan 8
answer = input("Port manakah yang biasanya digunakan untuk monitor? (hdmi / vga / usb) ")
if answer.lower() == "hdmi" or answer.lower() == "vga":
    print("Selamat...jawaban kamu benar :)!")
    score += 1
else:
    print("Yahh...maaf jawabanmu salah :( yang benar adalah hdmi atau vga")

# pertanyaan 9
answer = input("Komponen komputer manakah yang berfungsi untuk menampilkan gambar ke layar? ")
if answer.lower() == "gpu" or answer.lower() == "graphics card":
    print("Selamat...jawaban kamu benar :)!")
    score += 1
else:
    print("Yahh...maaf jawabanmu salah :( yang benar adalah gpu atau graphics card")

# pertanyaan 10
answer = input("Perangkat keras apa yang digunakan untuk mengetik di komputer? ")
if answer.lower() == "keyboard":
    print("Selamat...jawaban kamu benar :)!")
    score += 1
else:
    print("Yahh...maaf jawabanmu salah :( yang benar adalah keyboard")
    
print("Skor kamu adalah " + str(score) + " dari jawaban yang benar!!^_____^")
print("Skor kamu adalah " + str((score / 4) * 100) +  "%.")