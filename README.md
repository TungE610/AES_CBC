## AES_128_CBC
:point_right:Ngôn ngữ lập trình : Python <br>
<br>
:point_right: Thư viện sử dụng : crypto/pycryptodome, binascii, base64
<br>
<br>
*Cách cài đặt thư viện pycryptodome : pip/pip3 install pycryptodome*
<br>
<br>
## ENCRYPTION
<br>
# Các bước encrypt :
<br>
<br>
:triangular_flag_on_post: Khai báo và import các module cần thiết trong các thư viện. 
<br>
<br>

:triangular_flag_on_post: Chọn secret key . 
<br>
<br>
:triangular_flag_on_post: Sinh IV dưới dạng hex-string ngẫu nhiên dùng secrets . 
<br>
<br>

:triangular_flag_on_post: Chọn secret key dưới dạng tương tự. 
<br>
<br>

:triangular_flag_on_post: Nhập PlainText dạng raw . 
<br>
<br>
:triangular_flag_on_post: Encode và padding cho plainText theo tiêu chuẩn PKCS#7  .
<br>
<br>
:triangular_flag_on_post: Mã hoá AES bằng thư viện có sẵn .
<br>
<br>
:checkered_flag: Decode để xuất ra cipherText .
<br>
<br>
## DECRYPTION
<br>
# Các bước decrypt :
<br>
<br>
:triangular_flag_on_post: encode và dùng AES trong thư viện có sẵn để decypt bản mã  .
<br>
<br>
:checkered_flag: unpadding và xuất ra bản rõ  .






