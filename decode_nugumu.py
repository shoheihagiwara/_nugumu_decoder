#!/usr/bin/env python3

import re

# エンコーディング方法を適当にいくつか定義
enc_list = ['cp932', 'euc_jp', 'utf_8']

# 文字化けを直す対象の文字列をユーザーから受け取る（ンヌグム風にw）
target = input('文 字 化け を 直す 文 字 列 を い れ て  く ださ い: ')

# 文字化けを直してみる
result = [] 
for encode_code in enc_list:
  encoded_target = target.encode(encoding=encode_code, errors='replace')
  for decode_code in enc_list:
    if encode_code == decode_code:
      continue;
    decoded_string = encoded_target.decode(decode_code, 'replace')
    result.append((decoded_string, f"{encode_code} -> {decode_code}: {decoded_string}"))

# ただ、完璧には直らないので、直ってそうなものを優先して表示する。
# ひらがなカタカナの割合が多いものが直ってそうなものっぽいので、ひらがなカナタナの割合が多い順に並びかえて出力する
sorted_result_list = sorted(result, reverse=True, key= lambda elem: len(re.sub(r'[^あ-んア-ン]', '', elem[0])) / len(elem[0]) )
for _, answer in sorted_result_list:
  print(answer)
