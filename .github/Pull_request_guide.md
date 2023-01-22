##  Follow this guide to submit your first Pull Request

- **1.** Start by forking the [**Driver-Snoozing-System**](https://github.com/Deep-ghosty/Driver-Snoozing-System) repository. Click on the <a href="https://github.com/Deep-ghosty/Driver-Snoozing-System/fork"><img src="https://i.imgur.com/G4z1kEe.png" height="21" width="21"></a> symbol at the top right corner.

- **2.** Clone your forked repository:

```bash
git clone https://github.com/<your-github-username>/Driver-Snoozing-System.git
```

**3.** Navigate to the new project directory:

```bash
cd Driver-Snoozing-System
```

**4.** Set upstream command:

```bash
git remote add upstream https://github.com/Deep-ghosty/Driver-Snoozing-System.git
```

**5.** Create a new branch:

```bash
git checkout -b YourBranchName
```
<i>or</i>
```bash
git branch YourBranchName
git switch YourBranchName
``` 

**6.** Sync your fork or local repository with the origin repository:

- In your forked repository click on "Fetch upstream"
- Click "Fetch and merge".

### Alternatively, Git CLI way to Sync forked repository with origin repository:

```bash
git fetch upstream
```

```bash
git merge upstream/main
```

### [Github Docs](https://docs.github.com/en/github/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github) for Syncing

**7.** Make your changes to the source code.

**8.** Stage your changes and commit:

⚠️ **Make sure** not to commit `package.json` or `package-lock.json` file

⚠️ **Make sure** not to run the commands ```git add .``` or ```git add *```. Instead, stage your changes for each file/folder

```bash
git add file/folder
```

```bash
git commit -m "<your_commit_message>"
```

**9.** Push your local commits to the remote repository:

```bash
git push origin YourBranchName
```

**10.** Create a [Pull Request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)!

**11.** **Congratulations!** You've made your first contribution! 🙌🏼

