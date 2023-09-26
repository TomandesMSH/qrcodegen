import threading
import time
import sys
import qrcode

def loading_screen():
 
    animation_chars = "|/-\\"

    try:
        start_time = time.time()
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time >= 3:  
                break

            for char in animation_chars:
                sys.stdout.write("\r" + "Loading " + char)
                sys.stdout.flush()
                time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write("\rQR Code generator od tomandesa!\n")

if __name__ == "__main__":
    loading_thread = threading.Thread(target=loading_screen)
    loading_thread.start()



    loading_thread.join()

url = input ("Vlož URL adresu. ") 
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

data = url
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("qr.t.png")
print("Soubor s QR kodem byl pojmenovan qr.t.png (jakoze tomandes ty trumbero) a je ve stejné lokaci jako tento program.")

input("Stiskni Enter pro ukonceni programu")
print("Github.com/TomandesMSH")
time.sleep(1)
def loading_screen():
 
    animation_chars = "|/-\\"

    try:
        start_time = time.time()
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time >= 0.5: 
                break

            for char in animation_chars:
                sys.stdout.write("\r" + "Loading " + char)
                sys.stdout.flush()
                time.sleep(0.1) 
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write("\rvypinacka borci\n")

if __name__ == "__main__":
    loading_thread = threading.Thread(target=loading_screen)
    loading_thread.start()
sys.exit()
