import camelot
from github import Github
import os


directory = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(directory,'Input')
tables = camelot.read_pdf('{}/Direct Bill Commission Statement.pdf'.format(input_path),pages='all',flavor='stream')
data = tables[0]
filename='output.csv'
file_path = os.path.join(directory, filename)
data.to_csv(file_path,index=False)


df2 = df.to_csv(sep=',', index=False)
file_list = [df2]
file_names = ['Output.csv']


user = "dhaya6496"
password = "Dhaya6789"
g = Github(user,password)

def updategitfiles(file_names,file_list,userid,pwd,Repo,branch,commit_message =""):
    if commit_message == "":
        commit_message = "Data Updated - "+ datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    g = Github(userid,pwd)
    repo = g.get_user().get_repo(Repo)
    master_ref = repo.get_git_ref("heads/"+branch)
    master_sha = master_ref.object.sha
    base_tree = repo.get_git_tree(master_sha)
    element_list = list()
    for i in range(0,len(file_list)):
        element = InputGitTreeElement(file_names[i], '100644', 'blob', file_list[i])
        element_list.append(element)
    tree = repo.create_git_tree(element_list, base_tree)
    parent = repo.get_git_commit(master_sha)
    commit = repo.create_git_commit(commit_message, tree, [parent])
    master_ref.edit(commit.sha)
    print('Update complete')

updategitfiles(file_names,file_list,user,password,'sample','master')
