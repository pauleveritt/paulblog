"""

Automatically re-build Sphinx docs while editing, serve docs on an
HTTP port, and also reload any browsers pointed to the docs.

"""

from livereload import shell

from kaybee_bulma.run_livereload import get_server

sphinx = "env3/bin/python3 env3/bin/sphinx-build -E -b html docs docs/_build"

if __name__ == '__main__':
    server = get_server()
    server.watch('docs/**', shell(sphinx),
                 ignore=lambda s: '_build' in s)
    server.serve(root='docs/_build', live_css=False)
