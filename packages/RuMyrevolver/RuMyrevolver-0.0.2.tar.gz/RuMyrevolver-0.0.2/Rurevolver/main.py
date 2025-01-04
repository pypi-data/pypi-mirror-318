import random
import time


class russianr:
    def __init__(self, blank_ammunition: int = 5, live_ammunition: int = 1):
        self.bln_ammo = blank_ammunition
        self.live_ammo = live_ammunition

    def shot(self) -> int:
        print("Spinning a revolver drum...")
        print("""
             ,========.
            //  |  |  \\
           ||  ---|---  ||
           ||  ---|---  ||
           ||  ---|---  ||
             \\  |  |  //
             '========'
        """)
        time.sleep(3)
        if random.randint(self.live_ammo, self.bln_ammo+self.live_ammo) <= self.live_ammo and self.live_ammo > 0:
            self.live_ammo -= 1
            print("Boom!")
            return 0
        elif self.bln_ammo > 0:
            self.bln_ammo -= 1
            print("Booh... There was no shot fired!")
            return 1
        else:
            print("... I think we're out of ammo.")
            return 2

    def reload(self, blank_ammunition: int = 5, live_ammunition: int = 1) -> None:
        self.bln_ammo = blank_ammunition
        self.live_ammo = live_ammunition

    def see(self) -> tuple[int, int]:
        print(f"{self.live_ammo} live rounds left.\n{self.bln_ammo} blank rounds left.")
        return self.live_ammo, self.bln_ammo



if __name__ == "__main__":
    print("Hello! This is example how works my game")
    print("Creating class Roulette")
    time.sleep(3)
    Roulette = russianr()
    print("Shooting...")
    time.sleep(3)
    if not Roulette.shot():
        print("Oh... u died... try it again!")
        exit(0)
    print("\n\nYou're still alive, great, let's see what rounds are left in the drum.")
    Roulette.see()
    time.sleep(3)
    print("\n\nIt's clear. Now, let's reload the revolver.")
    Roulette.reload()
    time.sleep(1)
    print("\nThat's the end of the lesson, good luck!")
    exit(0)