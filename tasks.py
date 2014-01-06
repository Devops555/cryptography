import os
import re

import invoke


def update_version(filename, identifier, version):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path) as f:
        contents = f.read()
    contents = re.sub(
        r"^{} = .*?$".format(identifier),
        '{} = "{}"'.format(identifier, version),
        contents
    )
    with open(path, "w") as f:
        f.write(contents)


@invoke.task
def release(version):
    """
    ``version`` should be a string like '0.4' or '1.0'.
    """
    # This checks for changes in the repo.
    invoke.run("git diff-index --quiet HEAD")

    update_version("cryptography/__about__.py", "__version__")
    update_version("docs/conf.py", "version")
    update_version("docs/conf.py", "release")

    invoke.run("git commit -am 'Bump version numbers for release.'")
    invoke.run("git push")
    invoke.run("git tag -s {}".format(version))
    invoke.run("git push --tags")

    invoke.run("python setup.py sdist bdist_wheel")
    invoke.run("twine upload -s dist/cryptography-{}*".format(version))
