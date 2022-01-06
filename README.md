主要发布一些Python相关的项目

代码发布和上传

```
git config --global user.name "franc"
git config --global user.email "caifeiliu521@163.com"
```

创建 git 仓库:
```
mkdir python_programs
cd python_programs
git init
touch README.md
git add README.md
git commit -m "first commit"

git remote add origin git@gitee.com:gitfranc/python_programs.git
git push -u origin master

github 
git remote add origin git@gitee.com:gitfranc/python_programs.git
git push -u origin master
```
已有仓库?
```
cd existing_git_repo
git remote add origin git@gitee.com:gitfranc/python_programs.git
git push -u origin master

github
git remote add origin git@gitee.com:gitfranc/python_programs.git
git push -u origin master
```
