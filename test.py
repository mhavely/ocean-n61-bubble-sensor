import github from Github

## Uploading to GitHub
git clone https://github.com/mhavely/ocean-n61-bubble-sensor.git

def main():
    # Step 1: Create a Github instance:
    g = Github("usrname", "passwd")
    repo = g.get_user().get_repo('mathematics')

    # Step 2: Prepare files to upload to GitHub
    files = ['mathematics/numerical_analysis/regression_analysis/simple_regression_analysis.py', 'mathematics/numerical_analysis/regression_analysis/simple_regression_analysis.png']

    # Step 3: Make a commit and push
    commit_message = 'Add simple regression analysis'

    tree = repo.get_git_tree(sha)
    repo.create_git_commit(commit_message, tree, [])
    repo.push()

if __name__ == '__main__':
    main()