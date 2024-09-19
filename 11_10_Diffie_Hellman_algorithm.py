class DH_protocol:
    def DH_calculate(self, P, G):

        print("The value of P:", P)
        print("The value of G:", G)

        # a is the chosen Alise private key
        a = 4
        print("The private key a for Alice:", a)

        # Gets the generated key
        x = pow(G, a, P)

        # b is the chosen Bob private key
        b = 3
        print("The private key b for Bob:", b)

        # Gets the generated key
        y = pow(G, b, P)

        # Generating the secret key after the exchange of keys
        ka = pow(y, a, P)  # Secret key for Alice
        kb = pow(x, b, P)  # Secret key for Bob

        print("Secret key for Alice is:", ka)
        print("Secret key for Bob is:", kb)


# Both persons agree upon the public keys G and P
print("Input public key P:", end="")
P = int(input())
print("Input public key G:", end="")
G = int(input())
DH = DH_protocol()
DH.DH_calculate(P, G)