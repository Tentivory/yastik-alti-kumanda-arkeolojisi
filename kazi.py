#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yastık altı kumanda arkeolojisi.

Gercekten calisir. Bilimsel degildir. Ciddiymish gibi davranir.
"""

from __future__ import annotations

import argparse
import random
import sys

KATMANLAR = [
    "ust yastik kilifi (Gec Carsaf Cagi)",
    "ekmek kirintisi aluvyonu",
    "tek corap, esi baska evrende",
    "eski fis, yeni umut, ayni voltaj",
    "koltuk dikisi fay hatti",
    "uzaktan kumanda efsanesi (henuz eser degil)",
    "gercek kumanda, pili supheli",
    "ikinci kumanda, birincinin muhalefeti",
    "anahtarlik, yanlis medeniyet",
    "bosluk. bosluk da buluntudur.",
]


def kazi(katman: int, tohum: int | None) -> int:
    rng = random.Random(tohum)
    print("TentiAS Yastikalti Kazi Dairesi")
    print("ruhsat: koltuk / sit alani: yastik / patates: yok")
    print("-" * 42)
    bulunan = False
    for i in range(1, katman + 1):
        ad = KATMANLAR[(i - 1) % len(KATMANLAR)]
        sans = rng.random()
        if i >= 5 and sans > 0.62:
            print(f"katman {i}: KUMANDA. kanal hafizasi silinmis, egemenlik saglam.")
            bulunan = True
            break
        if "kumanda" in ad and i >= 7 and sans > 0.4:
            print(f"katman {i}: {ad} -> eser numarasi YA-{rng.randint(100, 999)}")
            bulunan = True
            break
        print(f"katman {i}: {ad}. tutanak tutuldu, kimse memnun degil.")
    if not bulunan:
        print("sonuc: kumanda bulunamadi. koltuk ifade vermeyi reddetti.")
        return 1
    print("sonuc: yayin devam eder. arkeolog kanala dokunmaz, sadece kazar.")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Yastik alti kumanda arkeolojisi")
    p.add_argument("--katman", type=int, default=6, help="kac katman kazilacak")
    p.add_argument("--tohum", type=int, default=None, help="rastgelelik tohumu")
    a = p.parse_args()
    if a.katman < 1:
        print("katman sifirin altinda kazilmaz. orasi baska bakanlik.")
        return 2
    return kazi(a.katman, a.tohum)


if __name__ == "__main__":
    sys.exit(main())
