import tkinter as tk
import random
from tkinter import messagebox

class Application(tk.Frame):
    # 丁半情報
    l = [
        {
            'name': '丁',
            'value': 0,
        },
        {
            'name': '半',
            'value': 1,
        },
    ]

    # プレイヤーの点数情報
    score = 500
    # プレイヤーが勝つために必要な点数
    winScore = 1000
    # プレイヤーが負ける場合に必要な点数
    loseScore = 0
    # プレイヤーの丁半選択情報
    variable = None
    # scale Widget情報
    scale = None
    # label Widget情報(現在の点数の表示情報)
    label = None

    # ボタンを選択した場合に実行する関数
    def competeCPU(self):
        # ランダムに0 or 1を選択
        randNum = random.randrange(len(self.l))
        # プレイヤーがかけた点数を取得する。
        betScore = self.scale.get()
        # プレイヤーが勝利したかどうか判定する。
        isWinPlayer = randNum == int(self.variable.get())

        # 点数の精算を行う。
        self.score = self.score + (betScore * 2) if isWinPlayer else self.score - betScore

        if self.score >= self.winScore:
            messagebox.showinfo("プレイヤーの勝利", "プレイヤーの点数が" + str(self.winScore) + "点を超えました。プレイヤーの勝利です。")
            # Windowを閉じる。
            self.master.destroy()
            return

        if self.score <= self.loseScore:
            messagebox.showinfo("プレイヤーの負け", "プレイヤーの点数が" + str(self.loseScore) + "点になりました。プレイヤーの敗北です。")
            # Windowを閉じる。
            self.master.destroy()
            return

        text = 'プレイヤーの勝利!?\n' if isWinPlayer else 'CPUの勝利!?\n'
        # Widgetの値の書き換えを行う。
        self.label.configure(text=text + '現在の得点 : ' + str(self.score))
        self.scale.configure(to=self.score)

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("400x300")
        # Windowへタイトルをつける。
        self.master.title('丁半を当てるゲーム')

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)

        # Windowを親要素とした場合に、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # font : フォントの設定
        # fontについて : https://kuroro.blog/python/RZNjLl36upkumxwkTRWl/
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        self.label = tk.Label(frame, text='現在の得点 : ' + str(self.score), font=('', 30))
        # frame Widget(Frame)を親要素とした場合に、label Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.label.pack(pady=5)



        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame2 = tk.Frame(self.master)
        # Windowを親要素とした場合に、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame2.pack(pady=10)

        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # bg : 背景色の設定
        # 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label = tk.Label(frame2, text='丁か半か選択してください', bg='red')
        # frame Widget(Frame)を親要素とした場合に、label Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        label.pack(pady=5)

        # 現在選択されているラジオボタンの値を文字列変数として扱う。
        # StringVarについて : https://kuroro.blog/python/K53voPjJuKFfYrjmP8FP/
        self.variable = tk.StringVar()
        # set() : 初期値として丁の値を設定する。
        self.variable.set(self.l[0]['value'])

        # frame Widget(Frame)を親要素として、radiobutton Widgetを作成する。
        # variable : 現在選択中のラジオボタンの値を設定。文字列変数(self.variable)として値を持たせることで、可変として扱い、その他のラジオボタンへ値を共有して選択の状態を管理できる。
        # value : ラジオボタン自身が持つ値の設定。0とする。
        # text : ラジオボタンを説明するテキスト。丁とする。
        # Radiobuttonについて : https://kuroro.blog/python/ztJbt5uabbTBMCGcljHc/
        radiobutton = tk.Radiobutton(frame2, variable=self.variable, value=self.l[0]['value'], text=self.l[0]['name'])

        # frame Widget(Frame)を親要素とした場合に、radiobutton Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        radiobutton.pack(side=tk.LEFT)

        # frame Widget(Frame)を親要素として、radiobutton Widgetを作成する。
        # variable : 現在選択中のラジオボタンの値を設定。文字列変数(self.variable)として値を持たせることで、可変として扱い、その他のラジオボタンへ値を共有して選択の状態を管理できる。
        # value : ラジオボタン自身が持つ値の設定。1とする。
        # text : ラジオボタンを説明するテキスト。半とする。
        # Radiobuttonについて : https://kuroro.blog/python/ztJbt5uabbTBMCGcljHc/
        radiobutton = tk.Radiobutton(frame2, variable=self.variable, value=self.l[1]['value'], text=self.l[1]['name'])

        # frame Widget(Frame)を親要素とした場合に、radiobutton Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        radiobutton.pack(side=tk.RIGHT)



        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame3 = tk.Frame(self.master)
        # Windowを親要素とした場合に、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame3.pack()

        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # bg : 背景色の設定
        # 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label = tk.Label(frame3, text='かける点数を選択してください', bg='red')
        # frame Widget(Frame)を親要素とした場合に、label Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        label.pack()

        # frame Widget(Frame)を親要素として、scale Widgetを作成する。
        # orient : scale Widgetを水平方向へ表示する。
        # from_ : scale Widgetの値の下限を設定する。
        # to : scale Widgetの値の上限を設定する。
        # Scaleについて : https://kuroro.blog/python/DUvG7YaE2i6jLwCxdPXJ/
        self.scale = tk.Scale(frame3, orient=tk.HORIZONTAL, from_=1, to=self.score)
        # frame Widget(Frame)を親要素とした場合に、scale Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.scale.pack()

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # command : ボタンを選択した場合に実行する関数を設定。self.competeCPUとする。
        # Buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        button = tk.Button(frame3, text='勝負する', command=self.competeCPU)
        # frame Widget(Frame)を親要素とした場合に、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        button.pack(pady=10)

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    # Windowを生成する。
    # Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
