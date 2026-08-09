### GitHubのmain branchから自分のローカル環境にダウンロードする方法
```bash
cd DataScience Competition
git fetch
git merge origin main
```

---
### ローカル環境で書いたものをGitHubの自分のbranchにアップロードする方法
```bash
cd DataScienceCompetition
git add .
git commit -m "変更内容を書く"
git push origin okawa
```

---
### branchの作成方法
```bash
cd DataScienceCompetition
git switch main
git pull origin main
git branch 新しいブランチ名
git switch 新しいブランチ名
git merge main
git push -u origin 新しいブランチ名
```

---
### VS code上の表記
- ●：変更が含まれるフォルダ（未保存・未コミットの変更が存在する階層）
- M：Modified：Gitで管理されているファイルのうち、前回コミットした状態から内容が編集・保存された
- U：Untracked：新しく作成されたファイル
- A：Added：規作成され、ステージング（git add）されたファイル
- D：Deleted：削除されたファイル
