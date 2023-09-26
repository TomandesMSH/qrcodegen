import threading
import time
import sys
import qrcode

def loading_screen():
    # Define the animation characters
    animation_chars = "|/-\\"

    try:
        start_time = time.time()
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time >= 3:  # Stop after 5 seconds (adjust as needed)
                break

            for char in animation_chars:
                sys.stdout.write("\r" + "Loading " + char)
                sys.stdout.flush()
                time.sleep(0.1)  # Adjust the sleep duration to control the animation speed
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write("\rQR Code generator od tomandesa!\n")

if __name__ == "__main__":
    loading_thread = threading.Thread(target=loading_screen)
    loading_thread.start()

    # Continue with your main program here...

    # Wait for the loading thread to finish (optional)
    loading_thread.join()

    # Add more code for your main program if needed



url = input ("Vlož URL adresu. ") 
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code
data = url
qr.add_data(data)
qr.make(fit=True)

# Create an Image object from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image file
img.save("qr.t.png")
print("Soubor s QR kodem byl pojmenovan qr.t.png (jakoze tomandes ty trumbero) a je ve stejné lokaci jako tento program.")

input("Stiskni Enter pro ukonceni programu")
print("Github.com/TomandesMSH")
time.sleep(1)
def loading_screen():
    # Define the animation characters
    animation_chars = "|/-\\"

    try:
        start_time = time.time()
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time >= 0.5:  # Stop after 5 seconds (adjust as needed)
                break

            for char in animation_chars:
                sys.stdout.write("\r" + "Loading " + char)
                sys.stdout.flush()
                time.sleep(0.1)  # Adjust the sleep duration to control the animation speed
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write("\rvypinacka borci\n")

if __name__ == "__main__":
    loading_thread = threading.Thread(target=loading_screen)
    loading_thread.start()
sys.exit()