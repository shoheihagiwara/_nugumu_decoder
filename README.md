# _nugumu_decoder
ンヌグムの文字化けを直すツール

## 使い方例
decode_nugumu.py を実行して、デコードしたい文字列を入れてくください。
上の方から、正解だと思われる可能性が高いデコード結果を表示します。

```sh
$ python3 decode_nugumu.py
文 字 化け を 直す 文 字 列 を い れ て  く ださ い: 縺薙ｓ縺ｫ縺｡縺ｯ縲ゅヰ繝ｼ繝繝ｫ繝ｦ繝ｼ繝繝ｼ繝舌?縺ｮ繝ｳ繝後げ繝?縺ｧ縺吶?ゆｻ頑律縺ｯ縲蜑阪?螳ｶ縺ｫ陦後縺ｦ縺ｿ縺溘縺ｨ諤昴縺ｾ縺吶?
cp932 -> utf_8: こんにちは。バー�ルユー�ーバ�?のンヌグ�?です�?�今日は�前�?家に行�てみた�と思�ます�?
cp932 -> euc_jp: �����������＜����������若���������若���若���?�����潟����違�?��с���?�篁���ャ��������?絎吟��茵�窿����帥��窿�����窿�障���?
utf_8 -> euc_jp: 膰肴��鐔�膰削繍膰削宗膰削蒐膰蚊����亥��鐔主��膵�鐔�膵�鐔�膵�鐔主��膵�鐔主�����?膰削舟膵�鐔括��緇����膵�?膰削洲膰阪��?���鐔脂��緇�膰削蒐膰画�����?��鰹酋膰削繍���緇�膰削拾膰削戎膰堺��膰削秀茫ゆ�雁減鐔丞減���?
euc_jp -> cp932: 裔ﾆ螢瘤ｫ裔治裔識裄､螂緕ｼ裙裙辞裙示裙湿裙裙湿裙ﾀ�?裔式裙宍裙ｸ螟ｲ裙?裔而裔ﾒ�?､謗ｻｴ靜ｧ裔識裄鳬ｺ�?�ｰ叱裔辞ｸ裹瘤ｦ裔質裔ﾞ裹瘤ｨ�獺裹瘤ｾ裔ﾒ�?
euc_jp -> utf_8: ������Ꭻ�Ꭱ�Ꭿ�����㎼���㎫�㎦�㎼���㎼����?�Ꭾ�㎳��夲��?�Ꭷ����?�掻��Χ�Ꭿ�����?갎��Ꭻ���Ꭶ�Ꮏ�����Ꭸ�����Ꮎ����?
utf_8 -> cp932: 邵ｺ阮呻ｽ鍋ｸｺ�ｽｫ邵ｺ�ｽ｡邵ｺ�ｽｯ邵ｲ繧�繝ｰ郢晢ｽｼ郢晉ｹ晢ｽｫ郢晢ｽｦ郢晢ｽｼ郢晉ｹ晢ｽｼ郢晁��?邵ｺ�ｽｮ郢晢ｽｳ郢晏ｾ後￡郢�?邵ｺ�ｽｧ邵ｺ蜷ｶ?繧��ｽｻ鬆大ｾ狗ｸｺ�ｽｯ邵ｲ陷鷹亂?陞ｳ�ｽｶ邵ｺ�ｽｫ髯ｦ蠕檎ｸｺ�ｽｦ邵ｺ�ｽｿ邵ｺ貅倡ｸｺ�ｽｨ隲､譏ｴ邵ｺ�ｽｾ邵ｺ蜷ｶ?
~ $


```
