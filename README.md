# DentistMap

- [DentistMap](#dentistmap)
  - [使用の流れ](#使用の流れ)
  - [環境作成方法](#環境作成方法)
  - [最後に](#最後に)
  - [連絡先](#連絡先)


## 使用の流れ
1. 本リポジトリをgit cloneしてください。
2. 次にgit cloneしたディレクトリ内で、venvを使用します。
3. venv側のpythonにて必要なライブラリをpip installして、実行してください。(各環境を汚くしないための施策です。)

## 環境作成方法
本ファイルはvenvを使用し、環境を切り分けて実行しております。  
なお、本開発時に実行したvenvコマンドはこちらです。  
```
python3.12 -m venv env
```
ホストOSはWSL上のUbuntuにて行っております。  
windowsやmacでも同等のことはできると思いますので、各自対応してください。    

次にsourceを行います。(venv上のpythonを使用する為)  
```
source env/bin/activate
```
このあとから操作してください。  
なお終了時には
```
deactivate
```
を必ず実行してください。  

## 最後に
実行による責任は各自で請け負ってください。  
こちらでは損失や損害が発生しても責任は取りません。  

## 連絡先
X : https://twitter.com/datui2525  
E-mail : datutarousumile@gmail.com
