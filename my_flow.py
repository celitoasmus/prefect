from prefect import task, Flow
from prefect.storage import Git

@task
def get_data():
    return [1, 2, 3, 4, 5]

@task
def print_data(data):
    print("adjusted on purpose")
    print(data)
    
@task
def print_data2():
    print("blablabla")


with Flow("example") as flow:
    data = get_data()
    print_data(data)
    print_data2()

flow.storage = Git(
    repo="celitoasmus/prefect",
    flow_path="my_flow.py",
    repo_host="github.com"
)
