# アノテーションチェッカー

## 概要
```
Pythonのアノテーションを参考に関数の引数チェックを行います。
PEP484等に準じ書いてるつもりです。
```

## 問題点
> Note that this PEP still explicitly does NOT prevent other uses of annotations, nor does it require (or forbid) any particular processing of annotations, even when they conform to this specification. 
[引用元](https://www.python.org/dev/peps/pep-0484/#abstract)

現在禁止してるので警告に変更するべきかもしれない

## install
```bash
pip install chk-args
```

## 使用方法
```py
from chk_args import chk_args

@chk_args
def example(arg_1:int):
	return arg_1

example(5)
#result->5

example("a")
#result->TypeError("The type of argument (arg_1) is int.")

```

