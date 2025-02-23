import numpy as np
import matplotlib.pyplot as plt


def plot_3d_graph(X, Y, Z, filename='output1.png', title='3D plot at 2D and Color', ):
    # 3Dグラフを作成
    plt.figure(figsize=(10, 8))
    plt.scatter(X, Y, c=Z, cmap='bwr')
    plt.colorbar(label='Output')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(title)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlim(-1.1, 1.1)
    plt.ylim(-1.1, 1.1)
    plt.savefig(filename)
    plt.close()


def plot_3d_graph2(X, Y, Z, T, filename='output2.png', title1='title1', title2='title2'):
    # 2つのグラフを並べて表示
    plt.figure(figsize=(15, 6))  # 横長の画像サイズに変更
    plt.subplot(1, 2, 1)
    plt.scatter(X, Y, c=Z, cmap='bwr')
    plt.colorbar(label='Output')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(title1)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlim(-1.1, 1.1)
    plt.ylim(-1.1, 1.1)

    plt.subplot(1, 2, 2)
    plt.scatter(X, Y, c=T, cmap='bwr')
    plt.colorbar(label='Output')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(title2)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlim(-1.1, 1.1)
    plt.ylim(-1.1, 1.1)

    plt.savefig(filename)
    plt.close()


def plot_2d_Result_lossAndAccuracyGraph(trainResule, filename='Result_lossAndAccuracy.jpeg', title='Loss and Accuracy'):
    # train, val, testのlossとAccuaryをグラフにしたい。
    # データの形式は{'epoch': 200, 'train': {'loss': 0.004981628507375717, 'accuracy': 0.525}, 'val': {'loss': 0.020840523143609364, 'accuracy': 0.5}, 'test': {'loss': 0.005032957345047038, 'accuracy': 0.5162590701424349}}
    # 左Y軸にLoss, 右Y軸にAccuracyとして、X軸をepoch数とする。
    # 判例は表示して、Accuracyは点線にする。
    # データ整形
    def _extraction(key1, key2):
        return [d[key1][key2] for d in trainResule]
    data = {
        'train_loss': _extraction('train', 'loss'),
        'val_loss': _extraction('val', 'loss'),
        'test_loss': _extraction('test', 'loss'),
        'train_accuracy': _extraction('train', 'accuracy'),
        'val_accuracy': _extraction('val', 'accuracy'),
        'test_accuracy': _extraction('test', 'accuracy'),
        'epoch': [d['epoch'] for d in trainResule]
    }

    # グラフ描画
    plt.figure(figsize=(10, 8))
    ax1 = plt.gca()
    ax2 = ax1.twinx()
    ax1.plot(data['epoch'], data['train_loss'],
             label='train loss', color='blue')
    ax1.plot(data['epoch'], data['val_loss'], label='val loss', color='orange')
    ax1.plot(data['epoch'], data['test_loss'],
             label='test loss', color='green')
    ax2.plot(data['epoch'], data['train_accuracy'],
             label='train accuracy', color='blue', linestyle='dashed')
    ax2.plot(data['epoch'], data['val_accuracy'],
             label='val accuracy', color='orange', linestyle='dashed')
    ax2.plot(data['epoch'], data['test_accuracy'],
             label='test accuracy', color='green', linestyle='dashed')
    # ax2の凡例を下に右に300pxずらす
    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax1.legend(h1+h2, l1+l2, loc='lower left')
    ax1.set_xlabel('epoch')
    ax1.set_ylabel('Loss')
    ax2.set_ylabel('Accuracy')
    # ax2のy軸を0-1に設定
    ax2.set_ylim(0, 1)

    plt.title(title)
    # plt.legend()
    plt.savefig(filename)


def main():
    # Example usage
    X = 2 * np.random.rand(100) - 1
    Y = 2 * np.random.rand(100) - 1
    Z = np.random.rand(100)

    plot_3d_graph(X, Y, Z)
    T = np.random.rand(100)
    plot_3d_graph2(X, Y, Z, T)


if __name__ == "__main__":
    main()
