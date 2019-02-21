# Web Crawling Menggunakan Scrapy Framework 

## Definisi

*Web Crawler* merupakan sebuah program atau script yang menggunakan metode tertentu yang memiliki tujuan untuk mengumpulkan secara otomatis semua data/informasi yang berada pada suatu website. Proses dari *web crawler* mengunjungi tiap dokumen dari website ini lah yang disebut dengan *Web Crawling*.

## Fungsi

Tujuan utama dari *web crawler* adalah untuk mengumpulkan informasi-informasi yang ada dalam suatu halaman web. Contoh penggunaannya yang paling umum adalah *search engine* yang memiliki tujuan untuk menampilkan data/informasi yang relevan dengan permintaan atau *keyword* yang dicari oleh *user*.

## Tentang Scrapy

Scrapy merupakan framework untuk ekstraksi data dari website. Scrapy dibangun dengan menggunakan Python. Pada Scrapy terdapat scheduler yang mengatur bagaimana crawling nanti berjalan, lalu ada Spider yang akan melakukan scraping ke laman situs tertentu, ada downloader yang mengunduh situs yang kemudian akan di parsing oleh spider, dan terakhir ada item pipeline yaitu jalur untuk penyimpanan item atau database. 

## Web Crawling dengan Scrapy

Tools yang dibutuhkan :

- Python 2.7 atau Python 3

- Command Prompt

  

1. Install Scrapy Menggunakan Pip

   ```pyhton
   pip install scrapy
   ```

2. Scrapy Shell

   Setelah berhasil menginstall Scrapy silahkan coba masuk ke dalam Scrapy Shell. Kegunaan shell milik scrapy ini mirip dengan shell milik python yang bisa di gunakan untuk bereksperimen sebelum mulai menuliskan code.

   Perintah untuk masuk ke dalam shell adalah :

   ```
   scrapy shell
   ```

3. Membuat Project Baru Menggunakan Scrapy

   Setelah puas bermain main dengan menggunakan shell. Sekarang saatnya untuk memulai project baru.

   ```
   scrapy startproject indoxxi
   ```

   ![1](E:\KULIAH\SMT 6\WEB MINING\Week 1\1.PNG)

   ​								Contoh struktur project scrapy

   File settings.py memuat setting untuk project yang bisa dirubah rubah nantinya.

   Folder spiders memuat file file spider yang akan berisi code program dari web page yang akan diambil datanya.

   File pipelines.py memuat code program untuk menghubungkan dengan penyimpanan database.

4. Membuat File Spider Baru

   Setelah mengenal beberapa item penting yang ada dalam struktur project, sekarang waktunya untuk membuat file spider baru yang akan memuat code program web crawler

   ```python
   scrapy genspider data_xxi https://indoxxi.bz/21cineplex
   ```

   Setelah command genspider tambahkan nama file yang diinginkan lalu masukkan url dari website yang akan dikumpulkan datanya.

5. Edit File Spider

   Setelah generate file spider baru maka akan didapatkan file dengan format .py dalam folder **spider**. Pada settingan awal (default) dari program akan di dapatkan tampilan berikut :

    ![2](E:\KULIAH\SMT 6\WEB MINING\Week 1\2.PNG)

   Setelah itu anda bisa menambakan perintah program lain dalam def parse.

6. Export Data Crawling Menjadi CSV, JSON, atau Excel

   Setelah berhasil melakukan *crawling* data pada webpage maka hal selanjutnya yang akan dilakukan adalah menyimpannya ke dalam format lain seperti CSV, JSON, atau Excel yang lebih gampang untuk di import ke program atau pun ke dalam database.

   Bisa menggunakan perintah dasar dari scrapy

   ```
   scrapy crawl <spider name> -o file.csv -t csv
   ```

   Atau bisa dengan menambahan beberapa code ke dalam file **settings.py**

   ```
   #Export CSV
   FEED_FORMAT = "csv"
   FEED_URI = "xxi_data.csv"
   ```

   ![3](E:\KULIAH\SMT 6\WEB MINING\Week 1\3.PNG)



