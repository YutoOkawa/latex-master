"""latexのソースコード自動入力プログラム(table)
caption、cel部入力に対応
表のcaption、行数、列数を入力して表のソースコードを生成
その後、クリップボードにコピーする、ペーストすることで使用可能
インテントはスペースキー4個分としている
"""

import pyperclip

def caption(table_text):
	"""
	caption部の文字列を入力する。

	Parameters
	----------
	teble_text : String
		出力する表のソースコード

	Returns
	-------
	table_text : String
		caption{}を付け足した表のソースコード

	"""
	print("captionを入力してください。",end="")

	#captionの入力
	caption_text = input()
	table_text = table_text + "    \\caption{"+caption_text+"}\n"
	return table_text

def tabular(table_text):
	"""
	表の列の数を入力し、列指定を行う。

	Parameters
	----------
	table_text : String
		captionが入力された表のソースコード

	Returns
	-------
	table_text : String
		\begin{tabular}と表の指定子が追加されたソースコード

	row_number : int
		列の数

	Notes
	-----
	列指定は中央揃え'c'のみ(c以外も実装予定)
	"""

	#インテントと\begin{tabular}の入力
	table_text = table_text + "    \\begin{tabular}{|"

	#列数の入力
	while True:
		print("表の列数を入力してください。",end="")
		try:
			row_number = int(input())
			break
		except ValueError:
			print('error')
			continue

	#列指定の入力
	for i in range(row_number):
		table_text = table_text + "c|"

	#\hlineの入力
	table_text = table_text + "} \\hline\n"
	return table_text,row_number

def input_cel(table_text,row_number):
	"""cel部の入力
	行数を入力し、その後全てのセルの内容を入力する
	"""

	#行数の入力
	while True:
		print("表の行数を入力してください。",end="")
		try:
			line_number = int(input())
			break
		except ValueError:
			print('error')
			continue

	#セル部の入力
	for i in range(line_number):
		#インテントの入力
		table_text = table_text + "       "

		#セルの入力
		for k in range(row_number):
			print(str(i+1)+'行'+str(k+1)+'列目のものを入力してください。',end="")
			cel_text = input()
			table_text = table_text + ' ' + cel_text + ' &'

		#'&'が一つ分多いのでカット
		table_text = table_text[:-1]

		#改行と\hlineの入力
		table_text = table_text + "\\\\ \\hline\n"
	return table_text

def main():
	table_text = "\\begin{table}[!h]\n    \centering\n"

	table_text = caption(table_text)

	table_text,row_number = tabular(table_text)

	table_text= input_cel(table_text,row_number)

	table_text = table_text + "    \\end{tabular}\n"

	table_text = table_text + "\\end{table}"

	#クリップボードにコピー
	pyperclip.copy(table_text)
	print("クリップボードにコピーしました。")

if __name__ == "__main__":
	main()
