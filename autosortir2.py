import os
import webbrowser  # Import webbrowser untuk membuka WhatsApp
from datetime import datetime
from colorama import Fore, init

# Inisialisasi colorama
init(autoreset=True)

def clear_screen():
    os.system('clear')  # Hanya menggunakan 'clear' untuk Termux

def list_txt_files():
    """Mengembalikan daftar file .txt dalam direktori saat ini."""
    return [f for f in os.listdir() if f.endswith('.txt')]

def auto_sortir(file_path):
    """Mengurutkan data dalam file yang dipilih dan menyimpannya ke file baru."""
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        data = [line.strip() for line in lines if line.strip()]
        seen_usernames = set()  # Nglacak user biar nggak dobel
        data_unique = []

        for entry in data:
            username = entry.split('|')[0]  # Kemungkinan user sama
            if username not in seen_usernames:
                seen_usernames.add(username)
                data_unique.append(entry)

        # Kolom ke 3 buat patokan ukuran (Followers)
        data_sorted = sorted(data_unique, key=lambda x: int(x.split('|')[2]) if len(x.split('|')) >= 6 else float('inf'))

        # Menyimpan hasil ke file baru dengan timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f'data_sorted_{timestamp}.txt'

        # Hapus file jika sudah ada
        if os.path.exists(output_file):
            os.remove(output_file)

        with open(output_file, 'w') as file:
            for entry in data_sorted:
                file.write(entry + '\n')

        print(Fore.GREEN + f"\nData telah diurutkan dan disimpan ke '{output_file}'\n")

    except Exception as e:
        print(Fore.RED + f"Error: {str(e)}")

def hapus_data(file_path):
    """Menghapus file yang dipilih."""
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(Fore.GREEN + f"File '{file_path}' telah dihapus.")
        else:
            print(Fore.RED + "File tidak ditemukan.")
    except Exception as e:
        print(Fore.RED + f"Error: {str(e)}")

def open_whatsapp():
    """Membuka WhatsApp dengan nomor yang ditentukan."""
    phone_number = "083114591479"
    webbrowser.open(f"https://wa.me/{phone_number}")

def main():
    clear_screen()

    # Tampilan Pertama
    print(Fore.CYAN + r"""
                                      ╔═══════════════════╗
                                      ║  ███████╗ ======  ║
                                      ║  ╚══███╔╝ ====    ║
                                      ║    ███╔╝ ===      ║ 
                                      ║   ███╔╝  ===      ║
                                      ║  ███████╗====     ║
                                      ║  ╚══════╝=======  ║
                                      ║       Z_Store     ║
                                      ╚═══════════════════╝   
     ╔═══════════════════════════════════════╗     ╔═══════════════════════════════════════╗
     ║>>>Tools Bantuan Untuk Sortir Hasil<<< ╠══╦══╣  >>>Tools Ini Hanya Supord |.txt|<<<  ║   
     ╚═══════════════════════════════════════╝  ║  ╚═══════════════════════════════════════╝
                          ╔═════════════════════╩═════════════════════╗                        
                          ║>> User|Pass|Follwrs|Follwng|Post|Cookie <<║
                          ╚═══════════════════════════════════════════╝       
""")

    input(Fore.WHITE + "Baca Baru Enter...")

    # Tampilan Kedua
    print(Fore.CYAN + "====================================")
    print(Fore.CYAN + " Menu nya masih ini jangan ktawa :(             ")
    print(Fore.CYAN + "====================================")
    print(Fore.YELLOW + "1. Auto Sortir")
    print(Fore.YELLOW + "2. Toko Z_Store (Chat WA)")

    action_choice = input(Fore.WHITE + "pilih tuh..: ")

    if action_choice == '1':
        txt_files = list_txt_files()
        if not txt_files:
            print(Fore.YELLOW + "heee file nya kaga ada.")
            return

        print(Fore.CYAN + "===============================")
        print(Fore.CYAN + "      cuma ini file kamu   ")
        print(Fore.CYAN + "===============================")
        for idx, file in enumerate(txt_files):
            print(Fore.WHITE + f"{idx + 1}. {file}")

        choice = input(Fore.WHITE + "yang mana nih yang gw sortir? ")
        try:
            file_index = int(choice) - 1
            if 0 <= file_index < len(txt_files):
                file_path = txt_files[file_index]
                auto_sortir(file_path)
            else:
                print(Fore.RED + "kagak ada paok.")
        except ValueError:
            print(Fore.RED + "masukin angkanya aja.")
    
    elif action_choice == '2':
        open_whatsapp()  # Panggil fungsi untuk membuka WhatsApp
    else:
        print(Fore.RED + "Pilihan tidak valid.")

if __name__ == "__main__":
    main()