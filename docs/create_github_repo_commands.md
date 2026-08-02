# Create the GitHub repository

Suggested repository name:

```text
ai-assisted-statistical-programming
```

After creating an empty repository on GitHub, run these commands locally from the repository folder:

```bash
git init
git add .
git commit -m "Initial companion code and prompt library release"
git branch -M main
git remote add origin git@github.com:YOUR-ACCOUNT/ai-assisted-statistical-programming.git
git push -u origin main
git tag -a v1.0.0 -m "First companion release for the first edition"
git push origin v1.0.0
```

Replace `YOUR-ACCOUNT` with the GitHub account or organization you choose.
