@rule("a.txt")
def build(target):
    print(run(["echo", "hello", "world"], stdout=True).stdout)
    print(run("echo hello", stdout=True).stdout)
    print(run("echoxx hello2", stdout=True, shell=True, check=False).stdout)
    print(">>>>>>>>>>>>")
    print(capture("echo hello"))
    print(run("echo", ["hello", ["world"]]).stdout)
    print(run("echo", ["hello", ["world"]]).stdout)
    print(run(["echo", ["hello", ["world"]]], stdout=True).stdout)
        