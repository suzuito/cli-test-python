# cli-test-python

## 開発環境を作る

```bash
pipenv install
```

## ユニットテストの実行

```bash
pipenv run pytest --cov=app --cov-report=html --cov-report=term --junitxml=./test.xml ./test_main.py
```

カバレッジを見る

```bash
open 
```
