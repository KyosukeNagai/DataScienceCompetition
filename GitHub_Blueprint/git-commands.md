# GitHubのmain branchから自分のローカル環境にダウンロードする方法

> cd DataScience Competition
> git fetch
> git merge origin main

# ローカル環境で書いたものをGitHubの自分のbranchにアップロードする方法

> cd DataScienceCompetition
> git add .
> git commit -m "変更内容を書く"
> git push origin okawa

# branchの作成方法

> cd DataScienceCompetition
> git switch main
> git pull origin main
> git branch 新しいブランチ名
> git switch 新しいブランチ名
> git merge main
> git push -u origin 新しいブランチ名