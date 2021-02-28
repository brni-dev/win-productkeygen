import random, string, time, colorama, sys
from colorama import Fore, Back, ansi, init
colorama.init(convert=True)

# App strings
appred = f"{Fore.RESET}[{Fore.LIGHTRED_EX}APP{Fore.RESET}]{Fore.LIGHTYELLOW_EX} "
appgreen = f"{Fore.RESET}[{Fore.LIGHTGREEN_EX}APP{Fore.RESET}]{Fore.LIGHTYELLOW_EX} "
appneutral = f"{Fore.RESET}[APP]{Fore.LIGHTYELLOW_EX} "

def main():
    """Main function"""
    c = 0
    try:
        iteration = int(input(f"\n{appgreen}How many random keys to create?{Fore.RESET} "))
        _time = float(input(f"{appgreen}How much time to write every key?{Fore.RESET} "))
    except Exception as e:
        print(f"\n{appred}Error! {e}{Fore.RESET}\n")
        time.sleep(2)
        sys.exit("")
    filename = input(f"{appgreen}File to write to:{Fore.RESET} ")
    while iteration < 0:
        print("\n{appred}Error! Please specify a valid amount of keys to create!{Fore.RESET}\n")
        iteration = int(input(f"\n{appgreen}How many random keys to create?{Fore.RESET} "))
    while str(_time).startswith("-"):
        print("\n{appred}Error! Please specify a valid amount of time to iterate over each key!{Fore.RESET}\n")
        _time = float(input(f"{appgreen}How much time to write every key?{Fore.RESET} "))
    temp = string.ascii_uppercase + string.digits
    productKeys = open(f"{str(filename)}.txt","w+")
    productKeys.write("")
    print(f"\n{appgreen}Reset the current {Fore.LIGHTMAGENTA_EX}{str(filename)}.txt{Fore.LIGHTYELLOW_EX} file! Writing the key/s to it...\n")
    time.sleep(2)
    productKeys.writelines(f"------------------------------------------------\n          Generated {str(iteration)} random key/s!\n------------------------------------------------\n\n")
    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]
    for _ in range(iteration):
        key = ""
        c += 1
        for _ in range(25):
            key += str(random.choice(temp)) 
        genkey = "-".join(chunks(key, 5))
        productKeys.writelines(f"{genkey}\n")
        print(f"{Fore.RESET}{Fore.LIGHTGREEN_EX}GENERATED KEY:{Fore.RESET} {genkey}{Fore.RESET} ({Fore.LIGHTMAGENTA_EX}{str(c)}{Fore.RESET})")
        time.sleep(_time)
    print(f"\n{appgreen}Finished writing {Fore.LIGHTMAGENTA_EX}{str(iteration)}{Fore.LIGHTYELLOW_EX} random key/s to {Fore.LIGHTMAGENTA_EX}{str(filename)}.txt{Fore.LIGHTYELLOW_EX}!{Fore.RESET}")
    time.sleep(2)
    print(f"{appgreen}Exiting...{Fore.RESET}\n")
    time.sleep(1)

# Runs main() function
if __name__ == "__main__":
    main()
