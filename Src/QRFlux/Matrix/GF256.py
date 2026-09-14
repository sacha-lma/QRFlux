from __future__ import annotations


def GF256(OctetA: int, OctetB: int) -> int:
    Resultat = 0
    for _ in range(8):
        if OctetB & 1:
            Resultat ^= OctetA
        BitDeGaucheActif = OctetA & 0x80
        OctetA = (OctetA << 1) & 0xFF
        if BitDeGaucheActif:
            OctetA ^= 0x1D
        OctetB >>= 1
    return Resultat