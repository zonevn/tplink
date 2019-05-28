# tplink

tplink là một tiện ích cho phép điều khiển bộ định tuyến TP-Link từ Command Prompt

#### Thiết bị hổ trợ

TL-WR841N / TL-WR841ND và một số dòng khác của TP-Link

#### Tính năng

- Tự động kết nối Internet thông qua cấu hình PPPoE
- Kiểm tra tốc độ Internet bằng speedtest
#### Yêu cầu và Cài đặt

1. Cài đặt [Python 3](https://www.python.org/downloads/windows/)
2. Tải [tplink](https://github.com/zonevn/tplink/archive/master.zip) về và giải nén
3. Double click vào file `register.bat` trong thư mục tplink


#### Cách dùng

Khai báo Username/Password của PPPoE (do nhà mạng cung cấp). Chỉ cần khai báo lần đầu tiên, hệ thống sẽ tự động lưu trữ lại. 

command line:

```shell
$ tplink createprofile
Host:		# Đánh IP Address của Default Gateway
Account: 	# Gán Username/Password do nhà mạng cung cấp, ví dụ t008_gftth_name
Password:	
```

Ta kích hoạt kết nối internet bằng câu lệnh sau, hệ thống sẽ tự cấu hình thiết bị và khởi động lại bộ định tuyến . Với -u là user và -p là password để login,  -v là version của bộ định tuyến.

command line:

```shell
$ tplink addprofile -u admin -p admin -v 11
```

Kiểm tra tốc độ internet, sau khi gõ lệnh và chờ vài giây hệ thống sẽ trả kết quả

command line:

```shell
$ tplink runspeedtest
Ping: 22.427	
Download: 2935.69 Kb/s
Upload: 2594.04 Kb/s
```

Dùng lệnh -h hoặc --help sau dòng lệnh để xem cách dùng, ví dụ:

```shell
$ tplink showprofile -h
```

#### Các dòng lệnh

| Dòng lệnh     | Mô tả                                                        |
| ------------- | ------------------------------------------------------------ |
| createprofile | khai báo username/password của PPPoE; chỉ cần khai báo lần đầu tiên, hệ thống sẽ tự lưu lại |
| addprofile    | gán username/password, bộ định tuyến sẽ khởi động lại sau khi thiết lập thành công |
| showprofile   | xem thông tin đã được khai báo                               |
| runspeedtest  | kiểm tra tốc độ internet                                     |
| help          | liệt kê các dòng lệnh                                        |

