def GF256(octet_a, octet_b):
    resultat = 0
    for _ in range(8):
        if octet_b & 1:
            resultat ^= octet_a
        bit_de_gauche_actif = octet_a & 0x80
        octet_a = (octet_a << 1) & 0xFF
        if bit_de_gauche_actif:
            octet_a ^= 0x1D
        octet_b >>= 1
    return resultat