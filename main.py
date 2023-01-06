import heapq

f = open("010-15.in", "r")  # Lese Datei ein
fl = f.readline().split()
# Erfasse Anzahl der Sitze und Anzahl der Parteien aus der ersten Zeile.
no_seats = int(fl[1])
no_parties = int(fl[0])

parties = []  # Quotient Stimmen Sitze ID
counter = 0

parties = [0 for g in range(1, no_parties + 1)]
# Erstelle Liste der Laenge n mit Nullen
for line in f:
    app_line = int(line.strip())
    parties[counter] = [-app_line, app_line, 0, counter]
    counter += 1
    # Fülle Liste "parties" mit Quotient, Stimmen, Sitzen und ID auf.
    # Quotient negieren, da es bei Python nur MinHeap gibt und wir MaxHeap
    # brauchen.
heapq.heapify(parties)
# Wandle "parties" in einen Heap um
# Vergleiche in Heap-Funktionen beziehen sich immer auf das erste Element aus
# einer Liste.
while no_seats > 0:
    # Wiederhole solange es verbleibende Sitze gibt:
    party_max = heapq.heappop(parties)
    # Gebe kleinsten Quotienten von "parties" in "party_max".
    party_max[2] += 1
    # vergebe einen Sitz
    party_max[0] = -party_max[1] / (party_max[2] + 1)
    # Quotient = Anzahl der Stimmen/ (Aktuelle Anzahl an Sitzen + 1)
    heapq.heappush(parties, party_max)
    # Fuege "party_max" wieder in "parties" ein.
    no_seats -= 1
    # Nimm vergebenen Sitz aus der Anzahl verbleibender Sitze heraus.

for party in parties:
    party.reverse()
    # Kehre Liste "party" um, sodass Reihenfolge: ID, Sitze, Stimmen, Quotient
    # ist, damit die Liste in der richtigen Reihenfolge wieder ausgegeben
    # werden kann.
heapq.heapify(parties)
# Wandle "parties" erneut in Heap um, diesmal sortiert nach der ID
h = open("sitze_output.txt", "a")
for i in range(0, no_parties):
    h.write(str(heapq.heappop(parties)[1]) + "\n")
    # Erstelle .txt Dokument aufsteigend nach ID sortiert und gebe Anzahl der
    # Sitze aus.
h.close()
