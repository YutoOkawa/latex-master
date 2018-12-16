"""latexのソースコード自動入力プログラム(table)
caption、cel部入力に対応
表のcaption、行数、列数を入力して表のソースコードを生成
その後、クリップボードにコピーする、ペーストすることで使用可能
インテントはスペースキー4個分としている
"""

import pyperclip

def caption(table_text):
	"""captionの入力
	"""
	print("captionを入力してください。",end="")

	#captionの入力
	caption_text = input()
	table_text = table_text + "    \\caption{"+caption_text+"}\n"
	return table_text

def tabular(table_text):
	"""列数の入力
	列指定中央揃え'c'のみ(c以外も実装予定)
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
		#インテント
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
	#\begin{table}で開始、一応centeringも
	table_text = "\\begin{table}[!h]\n    \centering\n"

	#captionの入力
	table_text = caption(table_text)

	#列数の入力、同時に列数も取得
	table_text,row_number = tabular(table_text)

	#行数の入力、セル部の入力
	table_text= input_cel(table_text,row_number)

	#\end{tabular}の入力 \begin{tabular}はtabular()内で入力済み
	table_text = table_text + "    \\end{tabular}\n"

	#\end{table}の入力
	table_text = table_text + "\\end{table}"

	#クリップボードにコピー
	pyperclip.copy(table_text)
	print("クリップボードにコピーしました。")

if __name__ == "__main__":
	main()
