import pytest

from . import Call, Pipe


def call(*cmds, **kwargs):
    return Call(cmds, **kwargs)


@pytest.mark.timeout(5)
def test_chain():
    p = call("cat", "conftest.py") | call("grep", "-i", "def") | call("tee")
    p()

    print(p.out, p.err, p.returncode)
    assert p.returncode == 0


@pytest.mark.timeout(5)
def test_pipefail():
    p = call("false") | call("true")
    p()
    print(p.out, p.err, p.returncode)
    assert p.returncode == 1


@pytest.mark.timeout(5)
def test_pipefail_no_wait():
    pipe = call("false") | call("cat")
    pipe()
    print(pipe.out, pipe.err, pipe.returncode)
    assert pipe.returncode == 1


@pytest.mark.timeout(5)
def test_pipe_correct():
    p = call("echo", "-n", "3") | call("tee")
    p()
    print(p.out, p.err, p.returncode)
    assert p.out == b"3"
    assert p.err == b""
    assert p.returncode == 0


@pytest.mark.timeout(5)
def test_pipe_combination():
    c1 = call("echo", "-n", "hello world")
    c2 = call("false")
    c3 = call("true")
    c4 = call("tee", "/dev/stderr")

    p = Pipe([Pipe([Pipe([c1, c2]), c3]), c4])
    p()
    p.wait()
    assert p[0].returncode == 1
    assert p[1].returncode == 0
    assert p.returncode == 1

    assert p[0][0].returncode == 1
    assert p[0][0][0].returncode == 0


@pytest.mark.timeout(5)
def test_pipe_behavior():
    c1 = call("echo", "-n", "hello world")
    c2 = call("tee", "/dev/stderr")
    c3 = call("false")
    c4 = call("echo", "-n", "hello moon")
    c5 = call("tee")

    p1 = c1 | c2 | c3 | c4 | c5
    p2 = Pipe([c1, c2, c3, c4, c5]).clone()

    for p in [p1, p2]:
        p()
        p.wait()

        assert p[0].returncode == 0
        assert p[1].returncode == 0
        assert p[2].returncode == 1
        assert p[3].returncode == 0
        assert p[4].returncode == 0

        assert p.returncode == 1

        for c in p:
            # we can read only stderr since stdout is read by the next call
            assert c.err.strip() in [b"hello world", b""]

        assert p.out == b"hello moon"


@pytest.mark.timeout(5)
def test_pipe_with_false():
    p1 = call("bash", "-c", "sleep 1; echo 3") | call("tee") | call("false")
    p1()
    p1.wait()
    assert p1.returncode == -13  # SIGPIPE

    p2 = call("echo", "-n", "3") | call("tee") | call("false")
    p2()
    p2.wait()
    assert p2.returncode == 1  # no SIGPIPE since tee is fast enough
