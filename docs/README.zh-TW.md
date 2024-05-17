# payload dumper of online

這是一個修改版的 payload dumper ，除了具有它原先支援的功能，還支援以下功能：

1. 從包含 payload.bin 的 zip 歸檔中直接提取分區，而無需解壓縮。
2. 從來自網路的包含 payload.bin （的 zip 歸檔）的 url （如 OTA 更新位址）直接提取分區，而無需下載整個檔案。
3. 支援 MIUI 和 HyperOS OTA 更新包。 (使用 CDN)

借助該腳本，你只需要少量的時間和存儲空間就能從 OTA 更新包或地址中提取你想要的分區，尤其是比較小的分區，如 boot, init_boot, vbmeta 等。

未來展望：也許可以讓它支援提取系統分區中的部分檔案？

## 用法

```bash
pip install git+https://github.com/lokey0905/payload-dumper
payload_dumper --partitions <partitions you need> <file path or url>
payload_dumper --list <file path or url>
```
---

# payload dumper

轉儲 Android 更新鏡像中的 `payload.bin` 映像。 由於使用了多線程，效能比其他工具有明顯提升。

## Installation

### Requirements

- Python3
- pip

## Usage

### 轉儲整個 `payload.bin` 文件

```bash
payload_dumper payload.bin
```

### 轉儲特定分割區

使用逗號分隔的要轉儲的分區清單：
```bash
payload_dumper --partitions boot,dtbo,vendor payload.bin
```


### 使用 OTA 修補舊鏡像

假設舊分區位於名為 `old/` 的目錄中：
```bash
payload_dumper --diff payload.bin
```