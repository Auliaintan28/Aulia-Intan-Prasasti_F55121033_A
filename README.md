# Aulia-Intan-Prasasti_F55121033_A
Final Project PAA 2
ANALYSIS ALGORITHM
A. Bubble Sort & Insertion Sort
Untuk menganalisis algoritma Bubble Sort dan Insertion Sort dalam kasus terbaik (best case), terburuk (worst case), dan kasus rata-rata (average case), kita perlu mempertimbangkan kompleksitas waktu keduanya.

Algoritma Bubble Sort:
- Worst case: Jika elemen-elemen dalam array tidak berurutan dan harus dilakukan penukaran pada setiap iterasi, maka kompleksitas waktu Bubble Sort adalah O(n^2).
- Best case: Jika elemen-elemen dalam array sudah terurut dengan benar, sehingga tidak perlu dilakukan penukaran, maka kompleksitas waktu Bubble Sort adalah O(n).
- Average case: Dalam kasus rata-rata, kompleksitas waktu Bubble Sort juga adalah O(n^2), karena penukaran masih perlu dilakukan pada sebagian besar iterasi.

Algoritma Insertion Sort:
- Worst case: Jika elemen-elemen dalam array tidak berurutan secara terbalik, sehingga setiap elemen harus dipindahkan ke posisi yang benar secara bertahap, maka kompleksitas waktu Insertion Sort adalah O(n^2).
- Best case: Jika elemen-elemen dalam array sudah terurut dengan benar, sehingga tidak ada elemen yang perlu dipindahkan, maka kompleksitas waktu Insertion Sort adalah O(n).
- Average case: Dalam kasus rata-rata, kompleksitas waktu Insertion Sort juga adalah O(n^2), karena sebagian besar elemen masih harus dipindahkan ke posisi yang benar.

Dalam kasus rata-rata, kedua algoritma memiliki kompleksitas waktu yang sama (O(n^2)), namun dalam kasus terbaik, Insertion Sort memiliki keunggulan dengan kompleksitas waktu O(n) dibandingkan dengan Bubble Sort yang masih membutuhkan O(n^2). Oleh karena itu, dalam kasus terbaik, Insertion Sort lebih efisien.
Namun, dalam kasus terburuk, baik Bubble Sort maupun Insertion Sort memiliki kompleksitas waktu yang sama (O(n^2)), sehingga keduanya memiliki performa yang sama buruknya.
Dalam kasus rata-rata, kedua algoritma memiliki kompleksitas waktu yang sama (O(n^2)), sehingga performanya juga serupa dalam kasus ini.
Pilihan algoritma tergantung pada karakteristik data yang akan diurutkan. Jika data hampir terurut atau memiliki jumlah elemen yang sangat sedikit, Insertion Sort dapat memberikan performa yang lebih baik. Namun, untuk data yang lebih acak dan ukuran yang lebih besar, algoritma pengurutan yang lebih efisien seperti Quick Sort atau Merge Sort biasanya lebih disukai.

B. TSP & Dijkstra
Algoritma TSP (Traveling Salesman Problem):

- Worst case:
    Dalam kasus terburuk, algoritma TSP memerlukan perhitungan jarak untuk semua kemungkinan permutasi node pada grafik lengkap. Oleh karena itu, kompleksitas waktu algoritma TSP adalah O(n!), di mana n adalah jumlah node dalam grafik. Ini karena ada n! kemungkinan permutasi node yang harus dievaluasi untuk mencari solusi optimal. Dalam kasus ini, algoritma TSP memerlukan waktu yang sangat lama, terutama saat jumlah node meningkat.
- Best case:
    Dalam kasus terbaik, algoritma TSP menerima grafik yang sudah terurut dengan benar sehingga tidak perlu memeriksa semua kemungkinan permutasi. Dalam hal ini, kompleksitas waktu algoritma TSP dapat menjadi O(1), karena solusi optimal langsung ditemukan tanpa perlu melakukan perhitungan tambahan. Namun, dalam praktiknya, kasus terbaik ini jarang terjadi.
- Average case:
    Dalam kasus rata-rata, kompleksitas waktu algoritma TSP masih merupakan O(n!). Ini karena, pada umumnya, algoritma TSP harus mengevaluasi banyak kemungkinan permutasi node sebelum menemukan solusi optimal. Meskipun ada beberapa optimasi dan pendekatan heuristik yang dapat digunakan untuk mengurangi jumlah permutasi yang harus diperiksa, kompleksitas waktu rata-rata tetap sangat tinggi.

Algoritma Dijkstra:

- Worst case:
    Dalam kasus terburuk, di mana semua jarak antara node dalam grafik adalah maksimum dan tidak ada jalur langsung antara node sumber dan tujuan, kompleksitas waktu algoritma Dijkstra adalah O((V + E) log V), di mana V adalah jumlah node (vertice) dan E adalah jumlah sisi (edge) dalam grafik. Dalam kasus ini, algoritma Dijkstra harus mengevaluasi semua sisi dan menghitung jarak terpendek dari node sumber ke semua node lainnya.
- Best case:
    Dalam kasus terbaik, di mana node tujuan berdekatan dengan node sumber atau langsung terhubung dengannya, kompleksitas waktu algoritma Dijkstra dapat menjadi O(V), di mana V adalah jumlah node dalam grafik. Dalam hal ini, algoritma Dijkstra langsung menemukan jalur terpendek tanpa perlu melihat sisi tambahan.
- Average case:
    Dalam kasus rata-rata, kompleksitas waktu algoritma Dijkstra tetap O((V + E) log V), karena harus mengevaluasi semua sisi dan menghitung jarak terpendek di antara mereka. Meskipun beberapa optimasi dapat digunakan untuk mempercepat algoritma Dijkstra, kompleksitas waktu rata-rata tetap bergantung pada jumlah node dan sisi dalam grafik.

Pada kedua algoritma, baik TSP maupun Dijkstra, kompleksitas waktu bergantung pada karakteristik dan struktur grafik yang digunakan. Dalam kasus praktis, keduanya dapat memerlukan waktu yang signifikan, terutama saat jumlah node atau sisi meningkat. Oleh karena itu, untuk masalah dengan grafik besar, diperlukan penggunaan optimasi atau pendekatan heuristik untuk meningkatkan efisiensi dan kinerja algoritma.
