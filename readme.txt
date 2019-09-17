git 演示

配置

git config --gloable user.name  name

git config -- gloable user.email email

初始化工作区--project目录下

git init
# 提交到暂存区index
git add *
git add file

# 查看git状态
git status

# 将缓存提交到仓库区

git commit [file] -m [msg]

# 查看文件不同
git diff file
# 找回备份文件
git checkout -- file




# 同步日志
git log