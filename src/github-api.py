import requests
import json

class RepoList():
  def __init__(self, user):
    self._user = user
    
  def request_api(self):
    response = requests.get(f'https://api.github.com/users/{self._user}/repos')
    
    if response.status_code == 200:
      return response.json()
    else:
      return response.status_code
    
  def show_repositories(self):
    repos = self.request_api()
    
    if type(repos) is not int:
      print(len(repos))
      
      for i in range(len(repos)):
        print(repos[i]['name'])
    else:
      print(repos)
      
repositorios = RepoList('edtroleis')
repositorios.show_repositories()