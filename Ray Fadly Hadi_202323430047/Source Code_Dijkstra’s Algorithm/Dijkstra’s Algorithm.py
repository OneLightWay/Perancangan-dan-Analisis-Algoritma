def dijkstra(G, a):
    n = len(G)  # Jumlah simpul
    
    L = [float('inf')] * n  # Inisialisasi array jarak dengan nilai tak terhingga
    '''
    for i <- 1 to n
        L(vi) <- infinite
    endfor
    '''    
    L[a] = 0  # Jarak dari a ke a adalah 0
    S = set()  # Himpunan solusi untuk mencatat simpul-simpul yang sudah dipilih
    lintasan = {a: [a]} # Penyimpanan untuk vertex yang dilalui

    for k in range(n):
        u = None
        minimum = float('inf')
        # Pilih simpul yang belum terdapat di dalam S dan memiliki L(u) minimum
        for i in range(n):
            if i not in S and L[i] < minimum:
                u = i
                minimum = L[i]

        if u is None:
            break

        S.add(u)  # Masukkan u ke dalam S

        # Update jarak yang baru dari a ke v
        for v in range(n):
            if v not in S and G[u][v] != 0 and L[u] + G[u][v] < L[v]:
                # Jarak dari a ke u ditambah bobot sisi dari u ke v lebih kecil dari jarak a ke v
                L[v] = L[u] + G[u][v]  # Update jarak dari a ke v
                lintasan[v] = lintasan[u] + [v] # Update lintasan yang dilalui dari a ke v

    return L, lintasan

# Contoh penggunaan
G = [
    [0, 4, 2, 0, 0],
    [0, 0, 0, 5, 0],
    [0, 1, 0, 8, 10],
    [0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0]
]
vertex_awal = 0
panjang_lintasan, shortest_paths = dijkstra(G, vertex_awal)

print("===== Penyelesaian =====")
for vertex, lintasan in shortest_paths.items():
    print("Panjang shortest-path:", panjang_lintasan[vertex], "\tdengan lintasan: ", "->".join(chr(ord('A') + p) for p in lintasan))
g = len(G)

print("\n===== Hasil =====")
print("Lintasan terpendek yang didapat\t: ", "->".join(chr(ord('A') + p) for p in shortest_paths[g-1]))
print("Panjang Lintasan \t\t: ", panjang_lintasan[g-1])