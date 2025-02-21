#!/usr/bin/env python
# coding:utf-8
import torch

def main():
    print("runtime check")
    try :
        # PyTorchの動作確認
        x = torch.rand(5, 3)
    except Exception as e:
        print("NG PyTorch")
        print(e)
        return
    print("OK PyTorch")

if __name__ == "__main__":
    main()
