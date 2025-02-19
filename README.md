Menggunakan Odoo versi 14 dan depends ke modul contacts

API CRUD ditandai dengan hashtag #CREATE, #READ, #UPDATE, dan #DELETE di dalam folder controller

RATE LIMIT ditandai dengan hashtag #RATE LIMIT di dalam folder model untuk function dan folder controller untuk eksekusi
catatan untuk rate limit, saat ini di set limit request tidak dapat lebih dari 2 kali dalam 1 menit

SECURITY ditandai dengan hashtag #SECURITY di dalam folder model untuk function dan folder controller untuk eksekusi
catatan untuk security, dibutuhkan API key yang dapat digenerate melalui My Profile yang ada di pojok kanan atas > masuk ke tab Account Security > Developer API Keys > klik New API Key untuk generate
setelah mendapatkan API key, pada saat request API, tambahkan di dalam Headers, key Authorization dengan value API key yang didapat
