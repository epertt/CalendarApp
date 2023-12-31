from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def setup(ctx):
    ctx.run("python3 src/setup.py", pty=True)
    
@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task(coverage_report)
def display_coverage_report(ctx):
    ctx.run("xdg-open htmlcov/index.html")
